from json_tricks import dump, dumps, load, loads, strip_comments
from PIL import Image
import cv2
import numpy as np
import pathlib


def format_joint_key(k):
    return int(k.replace('joint_', ''))

def get_opath(image_path, odir):
    tokens = image_path.split('/')
    fname = tokens[2]
    opath = f'{odir}/{fname}'
    return opath

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

def get_predictions(ipath):
    with open(ipath, 'r') as f:
        preds = load(f)
    return preds

def annotate(ipath, odir='./annot'):
    preds = get_predictions(ipath)

    for batch, d in preds.items():
        coords = get_coords(d)

        image_path = d['input']['path']
        image = get_image(image_path)

        annotate_circles(image, coords)
        annotate_labels(image, coords)
        annotate_lines(image, coords)

        opath = get_opath(image_path, odir)
        cv2.imwrite(opath, image)

        print(f'{opath}')

def get_preds(dpath):
    files = pathlib.Path(dpath).glob('**/*.json')
    return [str(f) for f in files]

files = get_preds('./custom/output/custom/pose_hrnet/w32_256x256_adam_lr1e-3/annots')

for ipath in files:
    annotate(ipath)

