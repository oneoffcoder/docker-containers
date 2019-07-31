import argparse
import sys
import os
from os import path
import json
from PIL import Image, ImageFont, ImageDraw, ImageEnhance

def parse_args(args):
    """
    Parses arguments.
    :return: Arguments.
    """
    parser = argparse.ArgumentParser('Makes bounding boxes on images')
    parser.add_argument('-j', '--json', help='JSON file results from darknet', required=True)
    parser.add_argument('-d', '--dir', help='output directory for images with bounding box', required=True)
    return parser.parse_args(args)


def annotate(item, o_dir):
    i_path = item['filename']
    o_path = os.path.join(o_dir, os.path.basename(i_path)).replace('.jpg', '.png')
    print('{} to {}'.format(i_path, o_path))

    i_img = Image.open(i_path).convert('RGBA')
    o_img = Image.new('RGBA', i_img.size)

    o_img.paste(i_img, (0, 0))

    draw = ImageDraw.Draw(o_img, 'RGBA')

    font = ImageFont.load_default()

    for obj in item['objects']:
        name = obj['name']
        x = obj['relative_coordinates']['center_x'] * i_img.size[0]
        y = obj['relative_coordinates']['center_y'] * i_img.size[1]
        w = (obj['relative_coordinates']['width'] * i_img.size[0]) / 2.0
        h = (obj['relative_coordinates']['height'] * i_img.size[1]) / 2.0

        x0 = x - w
        y0 = y - h
        x1 = x + w
        y1 = y + h

        points = [(x0, y0), (x1, y1)]

        draw.rectangle(points, fill=None)
        draw.text((x0, y0 - font.getsize(name)[1]), name, font=font)

    o_img.save(o_path, 'PNG')


def do_it(args):
    json_path = args.json
    dir_path = args.dir
    print('attempting to create bounding box from {} to {}'.format(json_path, dir_path))

    if path.exists(json_path) is False:
        print('{} file does not exists!'.format(json_path))
        return -1
    
    if path.exists(dir_path) is False:
        print('{} directory does not exists, creating'.format(dir_path))
        os.makedirs(dir_path)

    with open(json_path, 'r') as json_file:
        data = json.load(json_file)
        for item in data:
            annotate(item, dir_path)
            break
        
    

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    do_it(args)