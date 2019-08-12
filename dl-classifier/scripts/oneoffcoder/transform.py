from torchvision.transforms import *
from collections import namedtuple
import json

TRANSFORM_CONFIG = namedtuple('TRANSFORM_CONFIG', 'phase clazz name order params')

COMPOSABLE_TRANSFORMS = ['RandomApply', 'RandomChoice', 'RandomOrder', 'Compose']

TRANSFORMS = [
    'Resize', 'CenterCrop', 'ColorJitter', 'FiveCrop', 'Grayscale',
    'Pad', 'RandomAffine', 'RandomCrop',
    'RandomGrayScale', 'RandomHorizontalFlip', 'RandomPerspective', 'RandomResizedCrop', 'RandomRotation',
    'RandomVerticalFlip', 'TenCrop', 'Normalize', 'RandomErasing', 'ToTensor'
]

PARAMS = [
    #
    {"size": 224}, {"size": 224}, 
    {"brightness": 0, "contrast": 0, "saturation": 0, "hue": 0}, 
    {"size": 0}, {"num_output_channels": 3},
    #
    {"padding": 10, "fill": 0, "padding_mode": "constant"},
    {"degrees": [-10,10], "translate": [0.5, 0.5], "scale": [1.0, 1.5], "shear": 5, "resample": False, "fillcolor": 0},
    {"size": [224, 224], "padding": None, "pad_if_needed": False, "fill": 0, "padding_mode": "constant"},
    #
    {"p": 0.1}, {"p": 0.5},
    {"distortion_scale": 0.5, "p": 0.5, "interpolation": 3},
    {"size": 224, "scale": [0.08, 1.0], "ratio": [0.75, 1.33], "interpolation": 2},
    {"degrees": 10, "resample": False, "expand": False, "center": None},
    #
    {"p": 0.5}, {"size": 224, "vertical_flip": False},
    {"mean": [0.485, 0.456, 0.406], "std": [0.229, 0.224, 0.225]},
    {"p": 0.5, "scale": [0.02, 0.33], "ratio": [0.3, 3.3], "value": 0, "inplace": False},
    {}
]

def __get_transform__(clazz, params):
    if 'Resize' == clazz:
        return Resize(**params)
    elif 'CenterCrop' == clazz:
        return CenterCrop(**params)
    elif 'ColorJitter' == clazz:
        return ColorJitter(**params)
    elif 'FiveCrop' == clazz:
        return FiveCrop(**params)
    elif 'Grayscale' == clazz:
        return Grayscale(**params)
    elif 'Pad' == clazz:
        return Pad(**params)
    elif 'RandomAffine' == clazz:
        return RandomAffine(**params)
    elif 'RandomCrop' == clazz:
        return RandomCrop(**params)
    elif 'RandomGrayscale' == clazz:
        return RandomGrayscale(**params)
    elif 'RandomHorizontalFlip' == clazz:
        return RandomHorizontalFlip(**params)
    elif 'RandomPerspective' == clazz:
        return RandomPerspective(**params)
    elif 'RandomResizedCrop' == clazz:
        return RandomResizedCrop(**params)
    elif 'RandomRotation' == clazz:
        return RandomRotation(**params)
    elif 'RandomVerticalFlip' == clazz:
        return RandomVerticalFlip(**params)
    elif 'TenCrop' == clazz:
        return TenCrop(**params)
    elif 'Normalize' == clazz:
        return Normalize(**params)
    elif 'RandomErasing' == clazz:
        return RandomErasing(**params)
    elif 'ToTensor' == clazz:
        return ToTensor()
    else:
        return None

def get_default_transforms(input_size=299):
    return {
        'train': Compose([
            Resize(input_size),
            CenterCrop(input_size),
            ToTensor(),
            Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ]),
        'test': Compose([
            Resize(input_size),
            CenterCrop(input_size),
            ToTensor(),
            Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ]),
        'valid': Compose([
            Resize(input_size),
            CenterCrop(input_size),
            ToTensor(),
            Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
    }

def __convert_options__(options):
    convert = lambda o: TRANSFORM_CONFIG(o[0], o[1], o[2], int(o[3]), json.loads(o[4]))
    only_com = lambda o: True if o.clazz in COMPOSABLE_TRANSFORMS else False
    only_sin = lambda o: False if o.clazz in COMPOSABLE_TRANSFORMS else True

    com_options = filter(only_com, map(convert, options))
    sin_options = filter(only_sin, map(convert, options))

    return com_options, sin_options

def __convert_single_transforms__(confs, transforms={}):
    for conf in confs:
        if conf.phase not in transforms:
            transforms[conf.phase] = {}
            
        t = __get_transform__(conf.clazz, conf.params)
        
        transforms[conf.phase][conf.name] = {
            'order': conf.order,
            'transform': t
        }
    return transforms

def __convert_composable_transforms__(confs, transforms):
    for conf in confs:
        t_inputs = [transforms[conf.phase][name]['transform'] for name in conf.params['transforms']]
        t = None

        if 'RandomApply' == conf.clazz:
            p = conf.params['p'] if 'p' in conf.params else 0.5
            t = RandomApply(t_inputs, p=p)
        elif 'RandomChoice' == conf.clazz:
            t = RandomChoice(t_inputs)
        elif 'RandomOrder' == conf.clazz:
            t = RandomOrder(t_inputs)
        elif 'Compose' == conf.clazz:
            t = Compose(t_inputs)
        
        if t is not None:
            transforms[conf.phase][conf.name] = {
                'order': conf.order,
                'transform': t
            }

def __clean_transient_transforms__(transforms):
    for _, v in transforms.items():
        # delete transient transforms
        delete_names = [name for name, t in v.items() if t['order'] < 0]
        for name in delete_names:
            del v[name]

def __get_final_transforms__(transforms):
    d = {}
    for k, v in transforms.items():
        tups = sorted([(t['order'], t['transform']) for _, t in v.items()], key=lambda tup: tup[0])
        items = map(lambda item: item[1], tups)
        d[k] = items
    return d

def get_transforms(transform_options):
    com_options, sin_options = __convert_options__(transform_options)

    transforms = {}
    __convert_single_transforms__(sin_options, transforms)
    __convert_composable_transforms__(com_options, transforms)
    __clean_transient_transforms__(transforms)

    transforms = __get_final_transforms__(transforms)
    return transforms