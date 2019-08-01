import argparse
import sys
import os
from os import path
import json
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import seaborn as sns
import multiprocessing
from joblib import Parallel, delayed


def parse_args(args):
    """
    Parses arguments.
    :return: Arguments.
    """
    parser = argparse.ArgumentParser('Makes bounding boxes on images')
    parser.add_argument('-j', '--json', help='JSON file results from darknet', required=True)
    parser.add_argument('-d', '--dir', help='output directory for images with bounding box', required=True)
    parser.add_argument('-c', '--colors', help='number of colors', type=int, default=10, required=False)
    parser.add_argument('--ttf', help='true type font path', default='/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf', required=False)
    parser.add_argument('--ttfsize', help='true type font size', default=12, type=int, required=False)
    return parser.parse_args(args)


def get_colors(n_colors):
    """
    Gets a vector colors. Each color is defined by a triplet (R, G, B) where R, G and B are a value in [0, 255].
    :param n_colors: Number of colors.
    :return: Array of colors.
    """
    def normalize(v):
        return int(v * 255)

    return [(normalize(t[0]), normalize(t[1]), normalize(t[2])) for t in sns.color_palette('hls', n_colors)]


def get_font(args):
    """
    Gets a font.
    :param args: Arguments (ttf and ttfsize).
    :return: Font.
    """
    try:
        return ImageFont.truetype(args.ttf, args.ttfsize)
    except:
        return ImageFont.load_default()


def annotate(item, o_dir, args):
    """
    Annotates an item.
    :param item: Item where object has been detected (as generated from darknet).
    :param o_dir: Output directory.
    :param args: Arguments.
    :return: 1 if successful; otherwise 0.
    """
    try:
        i_path = item['filename']
        o_path = os.path.join(o_dir, os.path.basename(i_path)).replace('.jpg', '.png')
        print('{} to {}'.format(i_path, o_path))

        i_img = Image.open(i_path).convert('RGBA')
        o_img = Image.new('RGBA', i_img.size)

        o_img.paste(i_img, (0, 0))

        draw = ImageDraw.Draw(o_img, 'RGBA')

        font = get_font(args)
        colors = get_colors(args.colors)
        n_colors = len(colors)

        for obj in item['objects']:
            name = obj['name']
            clazz = obj['class_id']
            x = obj['relative_coordinates']['center_x'] * i_img.size[0]
            y = obj['relative_coordinates']['center_y'] * i_img.size[1]
            w = (obj['relative_coordinates']['width'] * i_img.size[0]) / 2.0
            h = (obj['relative_coordinates']['height'] * i_img.size[1]) / 2.0

            x0 = x - w
            y0 = y - h
            x1 = x + w
            y1 = y + h

            points = [(x0, y0), (x1, y1)]
            color = colors[clazz % n_colors]
            draw.rectangle(points, fill=None, outline=color)

            t_x, t_y = font.getsize(name)
            label_points = [(x0, y0 - t_y), (x0 + t_x, y0)]
            draw.rectangle(label_points, fill=color)
            draw.text((x0, y0 - t_y), name, font=font, fill=None)

        o_img.save(o_path, 'PNG')
        return 1
    except:
        return 0


def get_json(json_path):
    """
    Gets the JSON data.
    :param json_path: Path to JSON file.
    :return: JSON.
    """
    with open(json_path, 'r') as json_file:
        data = json.load(json_file)
        return data


def do_it(args):
    """
    Start the annotation process.
    :param args: Arguments.
    :return: None.
    """
    json_path = args.json
    dir_path = args.dir
    print('attempting to create bounding box from {} to {}'.format(json_path, dir_path))

    if path.exists(json_path) is False:
        print('{} file does not exists!'.format(json_path))
        return -1
    
    if path.exists(dir_path) is False:
        print('{} directory does not exists, creating'.format(dir_path))
        os.makedirs(dir_path)

    n_jobs = multiprocessing.cpu_count()
    data = get_json(json_path)
    results = Parallel(n_jobs=n_jobs, verbose=50)(delayed(annotate)(item, dir_path, args) for item in data)
    print('done {} of {}'.format(sum(results), len(data)))

    
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    do_it(args)