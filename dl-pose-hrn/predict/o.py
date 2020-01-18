from json_tricks import dump, dumps, load, loads, strip_comments
from PIL import Image
import cv2
import numpy as np
import pathlib
import os
from joblib import Parallel, delayed
import argparse
import sys
from collections import ChainMap

class Overlay(object):

    def __init__(self, params={}):
        d = {
            'circle': True,
            'circle_radius': 20,
            'circle_color': [0, 0, 255],
            'cirlce_thickness': 10,
            'label': True,
            'label_font_scale': 3,
            'label_colors': [[0, 0, 255], [0, 255, 0], [255, 0, 0]],
            'label_thickness': 10,
            'line': True,
            'line_color': [0, 0, 255],
            'line_thickness': 8
        }
        self.params = ChainMap(params, d)

    def get_annot_id(self, fpath):
        base = os.path.basename(fpath)
        stem, _= os.path.splitext(base)
        return stem

    def get_pose_id(self, fpath):
        base = os.path.basename(fpath)
        stem, _ = os.path.splitext(base)
        dash_index = stem.rfind('-')
        stem = stem[:dash_index]
        return stem

    def get_pose_order(self, fpath):
        base = os.path.basename(fpath)
        stem, _ = os.path.splitext(base)
        dash_index = stem.rfind('-')
        if -1 == dash_index:
            return 0
        order = int(stem[dash_index+1:])
        return order

    def get_image(self, image_path):
        image = Image.open(image_path).convert('RGB')
        image = np.array(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        return image

    def get_file_paths(self, dpath, ext):
        return [str(p) for p in pathlib.Path(dpath).glob(f'**/*.{ext}')]

    def get_json_content(self, ipath):
        with open(ipath, 'r') as f:
            content = load(f)
        return content

    def get_annot(self, ipath):
        d = self.get_json_content(ipath)
        d['id'] = self.get_annot_id(d['path'])

        return d

    def get_pose(self, ipath):
        d = self.get_json_content(ipath)
        d = d['batch_0']
        d['id'] = self.get_pose_id(d['input']['path'])
        d['order'] = self.get_pose_order(d['input']['path'])

        return d

    def transform_poses(self, annot):
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

        for box in annot['boxes']:
            if 'pose' in box:
                x, y = int(box['x1']), int(box['y1'])

                coords = get_coords(box['pose'])
                coords = [(x + dx, y + dy) for dx, dy in coords]

                box['joints'] = coords

                del box['pose']

    def annotate_image(self, annot, params):
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

        image_path = annot['path']
        image = self.get_image(image_path)
        for box in annot['boxes']:
            if 'joints' not in box:
                continue

            if params['circle']:
                radius = params['circle_radius']
                color = params['circle_color']
                thickness = params['circle_thickness']

                annotate_circles(image, box['joints'], radius=radius, color=color, thickness=thickness)

            if params['label']:
                font_scale = params['label_font_scale']
                thickness = params['label_thickness']

                annotate_labels(image, box['joints'], font_scale=font_scale, thickness=thickness)

            if params['line']:
                thickness = params['line_thickness']

                annotate_lines(image, box['joints'], thickness=thickness)

        return image

    def do_overlay(self, annot, output_dir, params):
        k = annot['id']
        print(f'processing {k}')
        self.transform_poses(annot)
        image = self.annotate_image(annot, params)

        opath = f'{output_dir}/{k}.jpg'
        cv2.imwrite(opath, image)

    def do_overlays(self, annots_dir, poses_dir, output_dir):
        annot_files = self.get_file_paths(annots_dir, 'json')
        poses_files = self.get_file_paths(poses_dir, 'json')

        annots = {a['id']: a for a in [self.get_annot(f) for f in annot_files]}
        poses = [self.get_pose(f) for f in poses_files]

        for pose in poses:
            k = pose['id']
            o = pose['order']
            if k in annots:
                annots[k]['boxes'][o]['pose'] = pose

        os.makedirs(output_dir, exist_ok=True)
        params = self.params

        Parallel(n_jobs=-1)(delayed(self.do_overlay)(annot, output_dir, params) for _, annot in annots.items())

def parse_args(args):
    parser = argparse.ArgumentParser(description='Annotates joints')

    parser.add_argument('-a', '--annots_dir', help='annotation directory', type=str, required=True)
    parser.add_argument('-p', '--poses_dir', help='poses directory', type=str, required=True)
    parser.add_argument('-o', '--output_dir', help='output directory', type=str, required=True)
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

def args2params(args):
    params = {
        'circle': True if args.circle == 1 else False,
        'label': True if args.label == 1 else False,
        'line': True if args.line == 1 else False,
        'circle_radius': args.circle_radius,
        'circle_thickness': args.circle_thickness,
        'label_font_scale': args.label_font_scale,
        'label_thickness': args.label_thickness,
        'line_thickness': args.line_thickness
    }
    return params

if __name__ == '__main__':
    args = parse_args(sys.argv[1:])

    annots_dir = args.annots_dir
    poses_dir = args.poses_dir
    output_dir = args.output_dir

    params = args2params(args)
    overlay = Overlay(params)
    overlay.do_overlays(annots_dir, poses_dir, output_dir)
