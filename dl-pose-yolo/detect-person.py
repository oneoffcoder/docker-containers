from __future__ import division

from models import *
from utils.utils import *
from utils.datasets import *

import os
import sys
import time
import datetime
import argparse

from PIL import Image

import torch
from torch.utils.data import DataLoader
from torchvision import datasets
from torch.autograd import Variable

from json_tricks import dump, dumps, load, loads, strip_comments
import cv2
import numpy as np

def get_annotations(img_path, detections, current_dim, classes):
    def get_clazz(detection):
        _, _, _, _, _, _, pred = detection
        return classes[int(pred)]

    def is_person_prediction(detection):
        clazz = get_clazz(detection)
        return clazz == 'person'

    def get_coords(detection):
        x1, y1, x2, y2, _, _, cls_pred = detection

        x1, y1 = x1.detach().cpu().numpy().item(), y1.detach().cpu().numpy().item()
        x2, y2 = x2.detach().cpu().numpy().item(), y2.detach().cpu().numpy().item()

        w = x2 - x1
        h = y2 - y1

        return {
            'x1': x1,
            'y1': y1,
            'x2': x2,
            'y2': y2,
            'w': w,
            'h': h,
            'center': {
                'x': w / 2.0,
                'y': h / 2.0
            }
        }

    img = np.array(Image.open(img_path))
    original_shape = img.shape[:2]

    detections = rescale_boxes(detections, current_dim, original_shape)

    return {
        'path': img_path,
        'boxes': [get_coords(d) for d in detections if is_person_prediction(d)]
    }

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--image_folder", type=str, default="data/samples", help="path to dataset")
    parser.add_argument('--annot_folder', type=str, default='annot', help='path to save annotations')
    parser.add_argument('--inspect_folder', type=str, default='inspect', help='path to annotated images')
    parser.add_argument('--cut_folder', type=str, default='cut', help='path to cut images')
    parser.add_argument("--model_def", type=str, default="config/yolov3.cfg", help="path to model definition file")
    parser.add_argument("--weights_path", type=str, default="weights/yolov3.weights", help="path to weights file")
    parser.add_argument("--class_path", type=str, default="data/coco.names", help="path to class label file")
    parser.add_argument("--conf_thres", type=float, default=0.8, help="object confidence threshold")
    parser.add_argument("--nms_thres", type=float, default=0.4, help="iou thresshold for non-maximum suppression")
    parser.add_argument("--batch_size", type=int, default=1, help="size of the batches")
    parser.add_argument("--n_cpu", type=int, default=0, help="number of cpu threads to use during batch generation")
    parser.add_argument("--img_size", type=int, default=416, help="size of each image dimension")
    parser.add_argument("--checkpoint_model", type=str, help="path to checkpoint model")
    return parser.parse_args()

def get_device():
    return torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def get_tensor_type():
    return torch.cuda.FloatTensor if torch.cuda.is_available() else torch.FloatTensor

def get_model(opt):
    device = get_device()
    model = Darknet(opt.model_def, img_size=opt.img_size).to(device)

    if opt.weights_path.endswith(".weights"):
        model.load_darknet_weights(opt.weights_path)
    else:
        model.load_state_dict(torch.load(opt.weights_path))

    model.eval()

    return model

def get_data_loader(opt):
    return DataLoader(
        ImageFolder(opt.image_folder, img_size=opt.img_size),
        batch_size=opt.batch_size,
        shuffle=False,
        num_workers=opt.n_cpu,
    )

def do_predictions(opt):
    model = get_model(opt)
    dataloader = get_data_loader(opt)

    paths = []
    predictions = []

    print("\nPerforming object detection:")
    prev_time = time.time()

    tensor_type = get_tensor_type()

    with torch.no_grad():
        for batch_i, (img_paths, input_imgs) in enumerate(dataloader):
            input_imgs = Variable(input_imgs.type(tensor_type))

            detections = model(input_imgs)
            detections = non_max_suppression(detections, opt.conf_thres, opt.nms_thres)

            current_time = time.time()
            inference_time = datetime.timedelta(seconds=current_time - prev_time)
            prev_time = current_time
            print("\t+ Batch %d, Inference Time: %s" % (batch_i, inference_time))

            paths.extend(img_paths)
            predictions.extend(detections)

    return paths, predictions

def convert_predictions(paths, predictions, opt):
    classes = load_classes(opt.class_path)
    current_dim = opt.img_size

    return [get_annotations(path, detections, current_dim, classes) 
        for path, detections in zip(paths, predictions) if detections is not None]

def get_output_filename(a, odir, ext, suffix=None):
    path = a['path']
    base_name = os.path.basename(path)
    fstem, fext = os.path.splitext(base_name)

    if suffix is None:
        fname = f'{fstem}.{ext}'
    else:
        fname = f'{fstem}-{suffix}.{ext}'

    opath = f'{odir}/{fname}'
    return opath

def get_image(image_path):
    image = Image.open(image_path).convert('RGB')
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    return image

def save_images(annotations, opt):
    def annotate(ipath, annots, color=[0, 0, 255], thickness=5):
        image = get_image(ipath)

        for box in annots['boxes']:
            start, end = (int(box['x1']), int(box['y1'])), (int(box['x2']), int(box['y2']))
            cv2.rectangle(image, start, end, color, thickness)

        return image

    os.makedirs(opt.inspect_folder, exist_ok=True)

    for a in annotations:
        ipath = a['path']
        image = annotate(ipath, a)

        opath = get_output_filename(a, opt.inspect_folder, 'jpg')
        cv2.imwrite(opath, image)

    print(f'saved annotated images to "{opt.inspect_folder}" directory')

def save_annotations(annotations, opt):
    os.makedirs(opt.annot_folder, exist_ok=True)

    for a in annotations:
        fname = get_output_filename(a, opt.annot_folder, 'json')
        with open(fname, 'w') as f:
            dump(a, f, indent=2)

    print(f'saved annotations to "{opt.annot_folder}" directory')

def save_cuts(annotations, opt):
    os.makedirs(opt.cut_folder, exist_ok=True)

    for a in annotations:
        ipath = a['path']
        im = cv2.imread(ipath)

        for i, b in enumerate(a['boxes']):
            x, y = int(b['x1']), int(b['y1'])
            w, h = int(b['w']), int(b['h'])

            cut = im[y:y+h, x:x+w]
            print(f'x,y = ({x}, {y}), w,h = ({w}, {h}), im = {im.shape}, cut = {cut.shape}, path = {ipath}')
            opath = get_output_filename(a, opt.cut_folder, 'jpg', i)
            cv2.imwrite(opath, cut)

    print(f'saved cut images to "{opt.cut_folder}" directory')


if __name__ == "__main__":
    opt = parse_args(sys.argv[1:])

    paths, predictions = do_predictions(opt)
    annotations = convert_predictions(paths, predictions, opt)

    save_annotations(annotations, opt)
    save_images(annotations, opt)
    save_cuts(annotations, opt)

