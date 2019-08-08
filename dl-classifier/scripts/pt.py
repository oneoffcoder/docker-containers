import argparse
import sys
import os
from os import path
import json
import random
import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import time
import copy
from collections import namedtuple
from sklearn.metrics import multilabel_confusion_matrix
from collections import namedtuple
from argparse import RawTextHelpFormatter

def get_device():
    """
    Gets the device.
    :return: cuda:0 or cpu.
    """
    return torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')


def get_input_size(model_type):
    """
    Gets the input size required by the model. All models
    require an input size of 256 except for Inception v3,
    which requires 299.
    :param model_type: Model type.
    :return: Input size to the model.
    """
    return 299 if 'inception_v3' == model_type else 256


def determine_inception(model_type):
    """
    Determines if the model type is Inception v3.
    :param model_type: Model type.
    :return: A boolean indicating if the model is Inception v3.
    """
    return True if model_type == 'inception_v3' else False


def create_model(model_type, num_classes, pretrained):
    """
    Creates a model.
    :param model_type: Model type.
    :param num_classes: Number of classes.
    :param pretrained: A boolean indicating if pretrained weights should be used.
    :return: Model.
    """
    device = get_device()
    if 'resnet18' == model_type:
        model = models.resnet18(pretrained=pretrained)
        model.fc = nn.Linear(model.fc.in_features, num_classes)
    elif 'resnet34' == model_type:
        model = models.resnet34(pretrained=pretrained)
        model.fc = nn.Linear(model.fc.in_features, num_classes)
    elif 'resnet50' == model_type:
        model = models.resnet50(pretrained=pretrained)
        model.fc = nn.Linear(model.fc.in_features, num_classes)
    elif 'resnet101' == model_type:
        model = models.resnet101(pretrained=pretrained)
        model.fc = nn.Linear(model.fc.in_features, num_classes)
    elif 'resnet152' == model_type:
        model = models.resnet152(pretrained=pretrained)
        model.fc = nn.Linear(model.fc.in_features, num_classes)
    elif 'alexnet' == model_type:
        model = models.alexnet(pretrained=pretrained)
        model.classifier[6] = nn.Linear(4096, num_classes)
    elif 'vgg11' == model_type:
        model = models.vgg11(pretrained=pretrained)
        model.classifier[6] = nn.Linear(model.classifier[6].in_features, num_classes)
    elif 'vgg11_bn' == model_type:
        model = models.vgg11_bn(pretrained=pretrained)
        model.classifier[6] = nn.Linear(model.classifier[6].in_features, num_classes)
    elif 'vgg13' == model_type:
        model = models.vgg13(pretrained=pretrained)
        model.classifier[6] = nn.Linear(model.classifier[6].in_features, num_classes)
    elif 'vgg13_bn' == model_type:
        model = models.vgg13_bn(pretrained=pretrained)
        model.classifier[6] = nn.Linear(model.classifier[6].in_features, num_classes)
    elif 'vgg16' == model_type:
        model = models.vgg16(pretrained=pretrained)
        model.classifier[6] = nn.Linear(model.classifier[6].in_features, num_classes)
    elif 'vgg16_bn' == model_type:
        model = models.vgg16_bn(pretrained=pretrained)
        model.classifier[6] = nn.Linear(model.classifier[6].in_features, num_classes)
    elif 'vgg19' == model_type:
        model = models.vgg19(pretrained=pretrained)
        model.classifier[6] = nn.Linear(model.classifier[6].in_features, num_classes)
    elif 'vgg19_bn' == model_type:
        model = models.vgg19_bn(pretrained=pretrained)
        model.classifier[6] = nn.Linear(model.classifier[6].in_features, num_classes)
    elif 'squeezenet1_0' == model_type:
        model = models.squeezenet1_0(pretrained=pretrained)
        model.classifier[1] = nn.Conv2d(512, num_classes, kernel_size=(1,1), stride=(1,1))
        model.num_classes = num_classes
    elif 'squeezenet1_1' == model_type:
        model = models.squeezenet1_1(pretrained=pretrained)
        model.classifier[1] = nn.Conv2d(512, num_classes, kernel_size=(1,1), stride=(1,1))
        model.num_classes = num_classes
    elif 'densenet121' == model_type:
        model = models.densenet121(pretrained=pretrained)
        model.classifier = nn.Linear(model.classifier.in_features, num_classes)
    elif 'densenet161' == model_type:
        model = models.densenet161(pretrained=pretrained)
        model.classifier = nn.Linear(model.classifier.in_features, num_classes)
    elif 'densenet169' == model_type:
        model = models.densenet169(pretrained=pretrained)
        model.classifier = nn.Linear(model.classifier.in_features, num_classes)
    elif 'densenet201' == model_type:
        model = models.densenet201(pretrained=pretrained)
        model.classifier = nn.Linear(model.classifier.in_features, num_classes)
    elif 'googlenet' == model_type:
        model = models.googlenet(pretrained=pretrained)
        model.fc = nn.Linear(model.fc.in_features, num_classes)
    elif 'shufflenet_v2_x0_5' == model_type:
        model = models.shufflenet_v2_x0_5(pretrained=pretrained)
        model.fc = nn.Linear(model.fc.in_features, num_classes)
    elif 'shufflenet_v2_x1_0' == model_type:
        model = models.shufflenet_v2_x1_0(pretrained=pretrained)
        model.fc = nn.Linear(model.fc.in_features, num_classes)
    elif 'shufflenet_v2_x1_5' == model_type:
        model = models.shufflenet_v2_x1_5(pretrained=pretrained)
        model.fc = nn.Linear(model.fc.in_features, num_classes)
    elif 'shufflenet_v2_x2_0' == model_type:
        model = models.shufflenet_v2_x2_0(pretrained=pretrained)
        model.fc = nn.Linear(model.fc.in_features, num_classes)
    elif 'mobilenet_v2' == model_type:
        model = models.mobilenet_v2(pretrained=pretrained)
        model.classifier[1] = nn.Linear(model.classifier[1].in_features, num_classes)
    elif 'resnext50_32x4d' == model_type:
        model = models.resnext50_32x4d(pretrained=pretrained)
        model.classifier[1] = nn.Linear(model.classifier[1].in_features, num_classes)
    elif 'resnext101_32x8d' == model_type:
        model = models.resnext101_32x8d(pretrained=pretrained)
        model.fc = nn.Linear(model.fc.in_features, num_classes)
    elif 'wide_resnet50_2' == model_type:
        model = models.wide_resnet50_2(pretrained=pretrained)
        model.fc = nn.Linear(model.fc.in_features, num_classes)
    elif 'wide_resnet101_2' == model_type:
        model = models.wide_resnet101_2(pretrained=pretrained)
        model.fc = nn.Linear(model.fc.in_features, num_classes)
    elif 'mnasnet0_5' == model_type:
        model = models.mnasnet0_5(pretrained=pretrained)
        model.classifier[1] = nn.Linear(model.classifier[1].in_features, num_classes)
    elif 'mnasnet0_75' == model_type:
        model = models.mnasnet0_75(pretrained=pretrained)
        model.classifier[1] = nn.Linear(model.classifier[1].in_features, num_classes)
    elif 'mnasnet1_0' == model_type:
        model = models.mnasnet1_0(pretrained=pretrained)
        model.classifier[1] = nn.Linear(model.classifier[1].in_features, num_classes)
    elif 'mnasnet1_3' == model_type:
        model = models.mnasnet1_3(pretrained=pretrained)
        model.classifier[1] = nn.Linear(model.classifier[1].in_features, num_classes)
    else:
        model = models.inception_v3(pretrained=pretrained)
        model.AuxLogits.fc = nn.Linear(model.AuxLogits.fc.in_features, num_classes)
        model.fc = nn.Linear(model.fc.in_features, num_classes)
    return model.to(device)


def get_criterion():
    """
    Gets the criterion for determining loss. Only cross-entropy is supported.
    :return: Loss criterion.
    """
    return nn.CrossEntropyLoss()


def get_optimizer(model, params):
    """
    Gets the optimizer. Only SGD is supported.
    :param model: Model.
    :param params: Parameters to the optimizer.
    :return: Optimizer.
    """
    return optim.SGD(model.parameters(), **params)


def get_scheduler(optimizer, params):
    """
    Gets the scheduler. Only StepLR is supported.
    :param optimizer: Optimizer.
    :param params: Parameters to the scheduler.
    :return: Scheduler.
    """
    return lr_scheduler.StepLR(optimizer, **params)


def get_dataloaders(data_dir, input_size, batch_size, num_workers):
    """
    Gets the data loaders.
    :param data_dir: Root path to data with images.
    :param input_size: The input size required by the model.
    :param batch_size: The batch size used during training.
    :param num_workers: The number of CPU workers for loading images.
    :return: A tuple: dataloaders, dataset_sizes, class_names, num_classes.
    """
    data_transforms = {
        'train': transforms.Compose([
            transforms.Resize(input_size),
            transforms.CenterCrop(input_size),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ]),
        'test': transforms.Compose([
            transforms.Resize(input_size),
            transforms.CenterCrop(input_size),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ]),
        'valid': transforms.Compose([
            transforms.Resize(input_size),
            transforms.CenterCrop(input_size),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
    }

    shuffles = {
        'train': True,
        'test': True,
        'valid': False
    }

    samples = ['train', 'test', 'valid']
    image_datasets = { x: datasets.ImageFolder(os.path.join(data_dir, x), transform=data_transforms[x]) for x in samples }
    dataloaders = { x: torch.utils.data.DataLoader(image_datasets[x], batch_size=batch_size, shuffle=shuffles[x], num_workers=num_workers) for x in samples }
    dataset_sizes = { x: len(image_datasets[x]) for x in samples }
    class_names = image_datasets['train'].classes
    
    return dataloaders, dataset_sizes, class_names, len(class_names)


def train_model(model, criterion, optimizer, scheduler, dataloaders, dataset_sizes, num_epochs, is_inception):
    """
    Starts the training.
    :param model: Model.
    :param criterion: Criterion.
    :param optimizer: Optimizer.
    :param scheduler: Scheduler.
    :param dataloaders: Data loaders.
    :param dataset_sizes: Dataset sizes.
    :param num_epochs: Number of epochs to train for.
    :param is_inception: A boolean indicating if the model is Inception v3.
    :return: Model.
    """
    device = get_device()
    Result = namedtuple('Result', 'phase loss acc')

    since = time.time()

    best_model_wts = copy.deepcopy(model.state_dict())
    best_acc = 0.0
    
    for epoch in range(num_epochs):
        results = []
        # Each epoch has a training and validation phase
        for phase in ['train', 'test']:
            if phase == 'train':
                model.train()  # Set model to training mode
            else:
                model.eval()   # Set model to evaluate mode

            running_loss = 0.0
            running_corrects = 0

            # Iterate over data.
            for inputs, labels in dataloaders[phase]:
                inputs = inputs.to(device)
                labels = labels.to(device)

                # zero the parameter gradients
                optimizer.zero_grad()

                # forward
                # track history if only in train
                with torch.set_grad_enabled(phase == 'train'):
                    if is_inception and phase == 'train':
                        outputs, aux_outputs = model(inputs)
                        loss1 = criterion(outputs, labels)
                        loss2 = criterion(aux_outputs, labels)
                        loss = loss1 + 0.4*loss2
                    else:
                        outputs = model(inputs)
                        loss = criterion(outputs, labels)
                        
                    _, preds = torch.max(outputs, 1)
                    
                    # backward + optimize only if in training phase
                    if phase == 'train':
                        loss.backward()
                        optimizer.step()
                        scheduler.step()

                # statistics
                running_loss += loss.item() * inputs.size(0)
                running_corrects += torch.sum(preds == labels.data)

            epoch_loss = running_loss / dataset_sizes[phase]
            epoch_acc = running_corrects.double() / dataset_sizes[phase]
            
            result = Result(phase, epoch_loss, float(str(epoch_acc.cpu().numpy())))
            results.append(result)

            # deep copy the model
            if phase == 'test' and epoch_acc > best_acc:
                best_acc = epoch_acc
                best_model_wts = copy.deepcopy(model.state_dict())
        
        results = ['{} loss: {:.4f} acc: {:.4f}'.format(r.phase, r.loss, r.acc) for r in results]
        results = ' | '.join(results)
        print('Epoch {}/{} | {}'.format(epoch, num_epochs - 1, results))

    time_elapsed = time.time() - since
    print('Training complete in {:.0f}m {:.0f}s'.format(time_elapsed // 60, time_elapsed % 60))
    print('Best val Acc: {:4f}'.format(best_acc))

    # load best model weights
    model.load_state_dict(best_model_wts)
    return model


def get_metrics(model, dataloaders, class_names):
    """
    Gets the classification performance metrics for each class.
    :param model: Model.
    :param dataloaders: Data loaders.
    :param class_names: Class names.
    :return: A named tuple: clazz, tn, fp, fn, tp, sen, spe, acc, f1, mcc
    """
    device = get_device()
    Metric = namedtuple('Metric', 'clazz tn fp fn tp sen spe acc f1 mcc')

    y_true = []
    y_pred = []
    was_training = model.training
    model.eval()

    with torch.no_grad():
        for i, (inputs, labels) in enumerate(dataloaders['valid']):
            inputs = inputs.to(device)
            labels = labels.to(device)
            cpu_labels = labels.cpu().numpy()

            outputs = model(inputs)
            _, preds = torch.max(outputs, 1)

            for j in range(inputs.size()[0]):
                cpu_label = f'{cpu_labels[j]:02}'
                clazz_name = class_names[preds[j]]
                
                y_true.append(cpu_label)
                y_pred.append(clazz_name)
                
        model.train(mode=was_training)
    
    cmatrices = multilabel_confusion_matrix(y_true, y_pred, labels=class_names)
    metrics = []
    for clazz in range(len(cmatrices)):
        cmatrix = cmatrices[clazz]
        tn, fp, fn, tp = cmatrix[0][0], cmatrix[0][1], cmatrix[1][0], cmatrix[1][1]
        sen = tp / (tp + fn)
        spe = tn / (tn + fp)
        acc = (tp + tn) / (tp + fp + fn + tn)
        f1 = (2.0 * tp) / (2 * tp + fp + fn)
        mcc_denom = np.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
        mcc = (tp * tn - fp * fn) / mcc_denom if mcc_denom > 0 else 0
        metric = Metric(clazz, tn, fp, fn, tp, sen, spe, acc, f1, mcc)
        metrics.append(metric)
    
    return metrics


def print_metrics(metrics):
    """
    Prints the metrics for each class.
    :param metrics: List of metrics.
    :return: None.
    """
    for m in metrics:
        print('{}: sen = {:.5f}, spe = {:.5f}, acc = {:.5f}, f1 = {:.5f}, mcc = {:.5f}'
              .format(m.clazz, m.sen, m.spe, m.acc, m.f1, m.mcc))


def get_ms_past_epoch():
    """
    Gets the number of milliseconds past epoch.
    :return: ms past epoch.
    """
    return int(round(time.time() * 1000))


def save_model(model_type, model, output_dir):
    """
    Saves the model.
    :param model_type: Model type.
    :param model: Model.
    :output_dir: Output directory.
    :return: None.
    """
    o_dir = '/tmp' if output_dir is None or len(output_dir.strip()) == 0 else output_dir.strip()
    millis = get_ms_past_epoch()
    output_file = '{}-{}.t'.format(model_type, millis)
    output_path = '{}/{}'.format(o_dir, output_file)
    torch.save(model.state_dict(), output_path)
    print('saved model to {}'.format(output_path))


def load_model(model_type, num_classes, model_path):
    """
    Loads a model.
    :param model_type: Model type.
    :param num_classes: Number of classes.
    :param model_path: Model path.
    :return: Model.
    """
    model = create_model(model_type, num_classes, False)
    model.load_state_dict(torch.load(model_path))
    return model


def get_model(model_type, num_classes, pretrained, model_path):
    """
    Gets a model. If the model_path is not null and has length greater
    than zero, then an attempt will be made to load such existing
    model. In the event of failure, a new model of model_type will
    be created.
    :param model_type: Model type.
    :param num_classes: Number of classes.
    :param pretrained: A boolean indicating if pretrained weights should be used.
    :param model_path: Path to an existing model.
    :return: Model.
    """
    if model_path is None or len(model_path.strip()) == 0:
        print('creating new model {}, pretrained = {}'.format(model_type, pretrained))
        return create_model(model_type, num_classes, pretrained)
    else:
        try:
            print('loading model {} from {}'.format(model_type, model_path))
            return load_model(model_type, num_classes, model_path)
        except:
            print('could not load model {} from {}, will create a new one'.format(model_type, model_path))
            return create_model(model_type, num_classes, pretrained)


def parse_args(args):
    """
    Parses arguments.
    :return: Arguments.
    """
    parser = argparse.ArgumentParser('PyTorch classification models', formatter_class=RawTextHelpFormatter)
    
    parser.add_argument('-m', '--model_type', help="""model type
    For example:
        - inception_v3
        - alexnet 
        - vgg19_bn 
    For the full list, go to https://pytorch.org/docs/stable/torchvision/models.html.
    """.strip(), required=True)
    
    parser.add_argument('-d', '--data_dir', help="""data directory
    e.g. /path/to/images
    Note that there should be 3 sub-directories under /path/to/images:
        - /path/to/images/train     # for training
        - /path/to/images/test      # for testing during training
        - /path/to/images/valid     # for validation after training
    Inside each of these sub-directories should be additional sub-directories 
    that correspond to your class labels. Assuming you have only two classes,
    such as 0 and 1, then you should have the following directories:
        - /path/to/images/train/0   # for training 0-th class
        - /path/to/images/train/1   # for training 1-st class
        - /path/to/images/test/0    # for testing 0-th class during training
        - /path/to/images/test/1    # for testing 1-st class during training
        - /path/to/images/valid/0   # for validating 0-th class after training
        - /path/to/images/valid/1   # for validating 1-st class after training
    """.strip(), required=True)
    
    parser.add_argument('-b', '--batch_size', help='batch size (default: 4)', required=False, default=4, type=int)
    
    parser.add_argument('-e', '--epochs', help='number of epochs (default: 25)', required=False, default=25, type=int)
    
    parser.add_argument('--pretrained', help='use transfer learning by loading pretrained weights (default: true)', required=False, default=True, type=bool)
    
    parser.add_argument('--optimizer_params', help="""optimizer parameters (default: {"lr": 0.001, "momentum": 0.9})
    torch.optim.SGD is the only optimizer supported.
    The string you pass in must be parseable by json.loads().
    Example of a JSON string is as follows.
    {"lr": 0.001, "momentum": 0.9}
    """.strip(), required=False, default='{"lr": 0.001, "momentum": 0.9}', type=json.loads)
    
    parser.add_argument('--scheduler_params', help="""scheduler parameters (default: {"step_size": 7, "gamma": 0.1})
    torch.optim.lr_scheduler.StepLR is the only scheduler supported.
    The string you pass in must be parseable by json.loads().
    Example of a JSON string is as follows.
    {"step_size": 7, "gamma": 0.1}
    """.strip(), required=False, default='{"step_size": 7, "gamma": 0.1}', type=json.loads)
    
    parser.add_argument('-w', '--num_workers', help='number of workers (default: 4)', required=False, default=4, type=int)
    
    parser.add_argument('-s', '--seed', help="""seed used for random number generators (default: 1299827)
    Use a negative number (e.g. -1) to seed with the current time
    represented as milliseconds past epoch.
    """.strip(), required=False, default=1299827, type=int)
    
    parser.add_argument('-o', '--output_dir', help="""output dir (default: /tmp)
    e.g. /tmp/inception_v3-1565298691256.t
    Note that the file path is: [model_type]-[milliseconds_past_epoch].t
    You may only control the output directory, not the file name.
    """.strip(), required=False, default='/tmp')
    
    parser.add_argument('-l', '--load_model', help="""path of model to load
    e.g. /path/to/model.t
    If such a path does NOT exists, then a new model (of the model_type) will 
    be created. If such a path does exists, then that model will be used
    as a starting point for training.
    """.strip(), required=False, default=None)

    return parser.parse_args(args)


def do_it(args):
    """
    Do it.
    :param args: Arguments.
    :return: None.
    """
    data_dir = args.data_dir
    model_type = args.model_type
    input_size = get_input_size(model_type)
    batch_size = args.batch_size
    num_workers = args.num_workers

    print('creating data loaders')
    dataloaders, dataset_sizes, class_names, num_classes = get_dataloaders(data_dir, input_size, batch_size, num_workers)
    
    model_path = args.load_model
    pretrained = args.pretrained
    optimizer_params = args.optimizer_params
    scheduler_params = args.scheduler_params

    print('constructing training components')
    model = get_model(model_type, num_classes, pretrained, model_path)
    criterion = get_criterion()
    optimizer = get_optimizer(model, optimizer_params)
    scheduler = get_scheduler(optimizer, scheduler_params)

    num_epochs = args.epochs
    is_inception = determine_inception(model_type)

    print('training initiated')
    model = train_model(model, criterion, optimizer, scheduler, dataloaders, dataset_sizes, num_epochs=num_epochs, is_inception=is_inception)

    print_metrics(get_metrics(model, dataloaders, class_names))

    output_dir = args.output_dir
    save_model(model_type, model, output_dir)

    print('done')


if __name__ == "__main__":
    # python scripts/pt.py -m inception_v3 -d faces-small -e 1
    # python scripts/pt.py -m inception_v3 -d faces-small -l /tmp/inception_v3-1565300203817.t -e 1
    args = parse_args(sys.argv[1:])

    seed = args.seed if args.seed > 0 else get_ms_past_epoch()
    print('seed: {}'.format(seed))
    random.seed(seed)
    torch.manual_seed(seed)

    do_it(args)