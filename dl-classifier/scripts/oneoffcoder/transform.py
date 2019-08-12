from torchvision.transforms import *
from collections import namedtuple

TRANSFORM = namedtuple('TRANSFORM', 'transform order')

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

def get_transform(clazz, params):
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

def test_transforms():
    for t, p in zip(TRANSFORMS, PARAMS):
        print(get_transform(t, p))