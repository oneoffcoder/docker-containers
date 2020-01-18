from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os
import pprint
import sys

import torch
import torch.nn.parallel
import torch.backends.cudnn as cudnn
import torch.optim
import torch.utils.data
import torch.utils.data.distributed
import torchvision.transforms as transforms

import _init_paths
from config import cfg
from config import update_config
from core.loss import JointsMSELoss
from core.function import validate
from utils.utils import create_logger

import dataset
import models

from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
import numpy as np
import logging
from utils.transforms import get_affine_transform
from utils.transforms import affine_transform
from utils.transforms import fliplr_joints
import cv2
import pathlib
from utils.vis import save_batch_heatmaps
from PIL import Image
from core.inference import get_max_preds
from json_tricks import dump, dumps, load, loads, strip_comments
from o import Overlay, args2params

class CustomDataset(Dataset):

    def __init__(self, cfg, cuts_dir, transform=None):
        self.transform = transform
        self.img_files = sorted([str(f) for f in pathlib.Path(cuts_dir).glob('**/*.jpg')])

    def __len__(self):
        return len(self.img_files)

    def __getitem__(self, idx):
        im_path = self.img_files[idx]

        input = Image.open(im_path)
        im_width, im_height = input.size

        if self.transform:
            input = self.transform(input)

        meta = {
            'path': im_path,
            'width': im_width,
            'height': im_height
        }

        return input, meta

def parse_args(args):
    parser = argparse.ArgumentParser(description='Train keypoints network')
    # general
    parser.add_argument('--cfg',
                        help='experiment configure file name',
                        required=True,
                        type=str)

    parser.add_argument('opts',
                        help="Modify config options using the command-line",
                        default=None,
                        nargs=argparse.REMAINDER)

    parser.add_argument('--modelDir',
                        help='model directory',
                        type=str,
                        default='')
    parser.add_argument('--logDir',
                        help='log directory',
                        type=str,
                        default='')
    parser.add_argument('--dataDir',
                        help='data directory',
                        type=str,
                        default='')
    parser.add_argument('--prevModelDir',
                        help='prev Model directory',
                        type=str,
                        default='')

    parser.add_argument('--circle', help='annotate with circles?', type=int, required=False, default=1)
    parser.add_argument('--label', help='annotate with labels?', type=int, required=False, default=1)
    parser.add_argument('--line', help='annotate with lines?', type=int, required=False, default=1)
    parser.add_argument('--circle_radius', help='circle radius', type=int, required=False, default=20)
    parser.add_argument('--circle_thickness', help='circle thickness', type=int, required=False, default=10)
    parser.add_argument('--label_font_scale', help='label font scale', type=int, required=False, default=3)
    parser.add_argument('--label_thickness', help='label thickness', type=int, required=False, default=8)
    parser.add_argument('--line_thickness', help='line thickness', type=int, required=False, default=5)

    args = parser.parse_args(args)
    return args

def save_debug_images(config, input, output, prefix):
    if config.DEBUG.SAVE_HEATMAPS_PRED:
        fname = f'{prefix}.jpg'
        save_batch_heatmaps(input, output, fname)

def save_prediction(config, input, output, prefix, metas):
    fname = f'{prefix}.json'
    
    batch_size = output.size(0)
    num_joints = output.size(1)
    heatmap_height = output.size(2)
    heatmap_width = output.size(3)

    preds, maxvals = get_max_preds(output.detach().cpu().numpy())

    d = {}
    for i in range(batch_size):
        batch_key = f'batch_{i}'
        
        fpath = metas['path'][i]
        im_width = metas['width'].detach().cpu().numpy()[i]
        im_height = metas['height'].detach().cpu().numpy()[i]

        d[batch_key] = {}
        d[batch_key]['pred'] = {
            'width': heatmap_width,
            'height': heatmap_height,
            'joints': { }
        }

        d[batch_key]['input'] = {
            'path': fpath,
            'width': im_width,
            'height': im_height
        }

        for j in range(num_joints):
            joint_key = f'joint_{j}'

            x = int(preds[i][j][0])
            y = int(preds[i][j][1])

            d[batch_key]['pred']['joints'][joint_key] = [x, y]

    with open(fname, 'w') as f:
        dump(d, f, indent=2)

    return d

def save_inspection(prefix, preds):
    def format_joint_key(k):
        return int(k.replace('joint_', ''))

    def get_coords(d):
        p = d['pred']
        i = d['input']

        p_width = p['width']
        p_height = p['height']

        x = [(format_joint_key(k), v[0]) for k, v in p['joints'].items()]
        y = [(format_joint_key(k), v[1]) for k, v in p['joints'].items()]

        x = [(tup[0], tup[1] / p_width) for tup in x]
        y = [(tup[0], tup[1] / p_height) for tup in y]

        x = sorted(x, key=lambda tup: tup[0])
        y = sorted(y, key=lambda tup: tup[0])

        coords = [(xp[1], yp[1]) for xp, yp in zip(x, y)]

        i_width = i['width']
        i_height = i['height']

        coords = [(tup[0] * i_width, tup[1] * i_height) for tup in coords]
        coords = [(int(tup[0]), int(tup[1])) for tup in coords]

        return coords

    def get_image(image_path):
        image = Image.open(image_path).convert('RGB')
        image = np.array(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        return image
    
    def annotate_circles(image, coords, radius=20, color=[0, 0, 255], thickness=10):
        for coord in coords:
            cv2.circle(image, coord, radius, color, thickness)

    def annotate_labels(image, coords, font=cv2.FONT_HERSHEY_SIMPLEX, 
        font_scale=3, 
        colors=[[255, 0, 0], [0, 255, 0], [0, 0, 255]], 
        thickness=8):

        for point, coord in enumerate(coords):
            color = colors[point % len(colors)]
            p_text = f'{point}'
            cv2.putText(image, p_text, coord, font, font_scale, color, thickness, cv2.LINE_AA)

    def annotate_lines(image, coords, color=[0, 0, 255], thickness=5):
        points = {i: coord for i, coord in enumerate(coords)}
        lines = [
            (0, 1), (1, 2), (2, 6),
            (5, 4), (4, 3), (3, 6),
            (6, 7), (7, 8), (8, 9),
            (10, 11), (11, 12), (12, 7),
            (15, 14), (14, 13), (13, 7)
        ]

        for line in lines:
            pt1 = points[line[0]]
            pt2 = points[line[1]]

            cv2.line(image, pt1, pt2, color, thickness)

    fname = f'{prefix}.jpg'

    for batch, d in preds.items():
        coords = get_coords(d)

        image_path = d['input']['path']
        image = get_image(image_path)

        annotate_circles(image, coords)
        annotate_labels(image, coords)
        annotate_lines(image, coords)

        cv2.imwrite(fname, image)

def predict(config, dataset_loader, model, output_dir, tb_log_dir, writer_dict=None):
    print(f'output_dir = {output_dir}, tensorboard_log_dir = {tb_log_dir}')
    
    debug_dir = f'{output_dir}/debug'
    annots_dir = f'{output_dir}/annots'
    inspect_dir = f'{output_dir}/inspect'

    os.makedirs(debug_dir, exist_ok=True)
    os.makedirs(annots_dir, exist_ok=True)
    os.makedirs(inspect_dir, exist_ok=True)

    model.eval()

    with torch.no_grad():
        for i, (inputs, metas) in enumerate(dataset_loader):
            outputs = model(inputs)

            debug_prefix = '{}_{}'.format(os.path.join(debug_dir, 'inference'), i)
            annots_prefix = '{}_{}'.format(os.path.join(annots_dir, 'inference'), i)
            inspect_prefix = '{}_{}'.format(os.path.join(inspect_dir, 'inference'), i)

            save_debug_images(config, inputs, outputs, debug_prefix)
            preds = save_prediction(config, inputs, outputs, annots_prefix, metas)
            save_inspection(inspect_prefix, preds)

    return debug_dir, annots_dir, inspect_dir

def load_model(cfg):
    model = eval('models.'+cfg.MODEL.NAME+'.get_pose_net')(cfg, is_train=False)
    model.load_state_dict(torch.load(cfg.MODEL.PRETRAINED), strict=False)
    model = torch.nn.DataParallel(model, device_ids=cfg.GPUS).cuda()
    return model

def get_data_loader(cfg):
    resize = transforms.Resize(size=(256, 256))
    normalize = transforms.Normalize(
        mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
    )
    data_transforms = transforms.Compose([resize, transforms.ToTensor(), normalize])

    dataset = CustomDataset(cfg, cfg.DATASET.CUTS, data_transforms)
    data_loader = torch.utils.data.DataLoader(
        dataset,
        batch_size=cfg.TEST.BATCH_SIZE_PER_GPU*len(cfg.GPUS),
        shuffle=False,
        num_workers=cfg.WORKERS,
        pin_memory=True
    )
    return data_loader

def main(args):
    update_config(cfg, args)

    logger, final_output_dir, tb_log_dir = create_logger(cfg, args.cfg, 'predict')

    logger.info(pprint.pformat(args))
    logger.info(cfg)

    cudnn.benchmark = cfg.CUDNN.BENCHMARK
    torch.backends.cudnn.deterministic = cfg.CUDNN.DETERMINISTIC
    torch.backends.cudnn.enabled = cfg.CUDNN.ENABLED

    model = load_model(cfg)
    data_loader = get_data_loader(cfg)

    _, poses_dir, _ = predict(cfg, data_loader, model, final_output_dir, tb_log_dir)
    annots_dir = cfg.DATASET.ANNOTS
    final_dir = cfg.DATASET.FINAL

    params = args2params(args)
    overlay = Overlay(params)
    overlay.do_overlays(annots_dir, poses_dir, final_dir)


if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    main(args)
