import argparse
import sys

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from PIL import Image
import matplotlib.pyplot as plt

import torchvision.transforms as transforms
import torchvision.models as models

import copy

import warnings
from collections import namedtuple

def get_device():
    return torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def get_image_size():
    imsize = 512 if torch.cuda.is_available() else 128
    return imsize

def get_loader():
    image_size = get_image_size()
    loader = transforms.Compose([
        transforms.Resize((image_size, image_size)),
        transforms.ToTensor()])
    return loader

def get_unloader():
    unloader = transforms.ToPILImage()
    return unloader

def image_loader(image_name):
    device = get_device()
    image = Image.open(image_name)
    # fake batch dimension required to fit network's input dimensions
    loader = get_loader()
    image = loader(image).unsqueeze(0)
    return image.to(device, torch.float)

def to_pil_image(tensor, title=None):
    image = tensor.cpu().clone()  # we clone the tensor to not do changes on it
    image = image.squeeze(0)      # remove the fake batch dimension
    unloader = get_unloader()
    image = unloader(image)
    return image

class ContentLoss(nn.Module):

    def __init__(self, target,):
        super(ContentLoss, self).__init__()
        # we 'detach' the target content from the tree used
        # to dynamically compute the gradient: this is a stated value,
        # not a variable. Otherwise the forward method of the criterion
        # will throw an error.
        self.target = target.detach()

    def forward(self, input):
        self.loss = F.mse_loss(input, self.target)
        return input

def gram_matrix(input):
    a, b, c, d = input.size()  # a=batch size(=1)
    # b=number of feature maps
    # (c,d)=dimensions of a f. map (N=c*d)

    features = input.view(a * b, c * d)  # resise F_XL into \hat F_XL

    G = torch.mm(features, features.t())  # compute the gram product

    # we 'normalize' the values of the gram matrix
    # by dividing by the number of element in each feature maps.
    return G.div(a * b * c * d)

class StyleLoss(nn.Module):

    def __init__(self, target_feature):
        super(StyleLoss, self).__init__()
        self.target = gram_matrix(target_feature).detach()

    def forward(self, input):
        G = gram_matrix(input)
        self.loss = F.mse_loss(G, self.target)
        return input

class Normalization(nn.Module):
    def __init__(self, mean, std):
        super(Normalization, self).__init__()
        # .view the mean and std to make them [C x 1 x 1] so that they can
        # directly work with image Tensor of shape [B x C x H x W].
        # B is batch size. C is number of channels. H is height and W is width.
        self.mean = torch.tensor(mean).view(-1, 1, 1)
        self.std = torch.tensor(std).view(-1, 1, 1)

    def forward(self, img):
        # normalize img
        return (img - self.mean) / self.std

def get_style_model_and_losses(cnn, normalization_mean, normalization_std,
                               style_img, content_img,
                               content_layers=['conv_4'],
                               style_layers=['conv_1', 'conv_2', 'conv_3', 'conv_4', 'conv_5']):
    cnn = copy.deepcopy(cnn)

    # normalization module
    normalization = Normalization(normalization_mean, normalization_std).to(device)

    # just in order to have an iterable access to or list of content/syle
    # losses
    content_losses = []
    style_losses = []

    # assuming that cnn is a nn.Sequential, so we make a new nn.Sequential
    # to put in modules that are supposed to be activated sequentially
    model = nn.Sequential(normalization)

    i = 0  # increment every time we see a conv
    for layer in cnn.children():
        if isinstance(layer, nn.Conv2d):
            i += 1
            name = 'conv_{}'.format(i)
        elif isinstance(layer, nn.ReLU):
            name = 'relu_{}'.format(i)
            # The in-place version doesn't play very nicely with the ContentLoss
            # and StyleLoss we insert below. So we replace with out-of-place
            # ones here.
            layer = nn.ReLU(inplace=False)
        elif isinstance(layer, nn.MaxPool2d):
            name = 'pool_{}'.format(i)
        elif isinstance(layer, nn.BatchNorm2d):
            name = 'bn_{}'.format(i)
        else:
            raise RuntimeError('Unrecognized layer: {}'.format(layer.__class__.__name__))

        model.add_module(name, layer)

        if name in content_layers:
            # add content loss:
            target = model(content_img).detach()
            content_loss = ContentLoss(target)
            model.add_module("content_loss_{}".format(i), content_loss)
            content_losses.append(content_loss)

        if name in style_layers:
            # add style loss:
            target_feature = model(style_img).detach()
            style_loss = StyleLoss(target_feature)
            model.add_module("style_loss_{}".format(i), style_loss)
            style_losses.append(style_loss)

    # now we trim off the layers after the last content and style losses
    for i in range(len(model) - 1, -1, -1):
        if isinstance(model[i], ContentLoss) or isinstance(model[i], StyleLoss):
            break

    model = model[:(i + 1)]

    return model, style_losses, content_losses

def get_input_optimizer(input_img):
    # this line to show that input is a parameter that requires a gradient
    optimizer = optim.LBFGS([input_img.requires_grad_()])
    return optimizer

def run_style_transfer(cnn, normalization_mean, normalization_std,
                       content_img, style_img, input_img, num_steps=600,
                       style_weight=1000000, content_weight=1):
    model, style_losses, content_losses = get_style_model_and_losses(cnn,
        normalization_mean, normalization_std, style_img, content_img)
    optimizer = get_input_optimizer(input_img)

    run = [0]
    while run[0] <= num_steps:

        def closure():
            # correct the values of updated input image
            input_img.data.clamp_(0, 1)

            optimizer.zero_grad()
            model(input_img)
            style_score = 0
            content_score = 0

            for sl in style_losses:
                style_score += sl.loss
            for cl in content_losses:
                content_score += cl.loss

            style_score *= style_weight
            content_score *= content_weight

            loss = style_score + content_score
            loss.backward()

            run[0] += 1
            
            if run[0] % 10 == 0:
                s_score = style_score.item()
                c_score = content_score.item()

                print(f'[{run[0]}/{num_steps}] Style Loss {s_score:.4f}, Content Loss {c_score}')
            return style_score + content_score

        optimizer.step(closure)

    # a last correction...
    input_img.data.clamp_(0, 1)

    return input_img

def parse_args(args):
    parser = argparse.ArgumentParser('Neural Style Transfer',
        epilog='One-Off Coder http://www.oneoffcoder.com')
    
    parser.add_argument('--seed', help='Seed', default=37, required=False)
    parser.add_argument('--steps', help='Number of steps', default=600, required=False)
    parser.add_argument('--sweight', help='Style weight', default=1000000, required=False)
    parser.add_argument('--cweight', help='Content weight', default=1, required=False)

    parser.add_argument('-s', '--style', help='Style image path', required=True)
    parser.add_argument('-c', '--content', help='Content image path', required=True)
    parser.add_argument('-o', '--output', help='Output image path', default='./image/output.jpg', required=False)

    return parser.parse_args(args)

if __name__ == '__main__':
    args = parse_args(sys.argv[1:])

    seed = args.seed

    num_steps = args.steps
    style_weight = args.sweight
    content_weight = args.cweight

    style_path = args.style
    content_path = args.content
    output_path = args.output

    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

    style_img = image_loader(style_path)
    content_img = image_loader(content_path)
    input_img = content_img.clone()

    assert style_img.size() == content_img.size(), \
        f'size mismatch, style {style_img.size()}, content {content_img.size()}'

    device = get_device()

    cnn = models.vgg19(pretrained=True).features.to(device).eval()
    cnn_normalization_mean = torch.tensor([0.485, 0.456, 0.406]).to(device)
    cnn_normalization_std = torch.tensor([0.229, 0.224, 0.225]).to(device)

    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        output = run_style_transfer(cnn, cnn_normalization_mean,        
                    cnn_normalization_std,content_img, style_img, input_img,
                    num_steps=num_steps, style_weight=style_weight, 
                    content_weight=content_weight)
        output_img = to_pil_image(output)
        output_img.save(output_path)