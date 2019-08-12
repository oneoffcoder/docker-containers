# Purpose 

This project is an executable container with [all of PyTorch's convolutional neural networks](https://pytorch.org/docs/stable/torchvision/models.html) (CNNs). You may use it with ease to train, test and validate against your own data. All the available pre-trained model weights are downloaded into the container already. The way this container works is with the helper Python program `pt.py` and the docker instructions `ENTRYPOINT` and `CMD`. The `ENTRYPOINT` instruction points to `pt.py` and the `CMD` instruction passes in the `--help` flag. At runtime, you override what `CMD` passes to `pt.py` by specifying appropriate flags.

# Docker Hub

[Image](https://hub.docker.com/r/oneoffcoder/dl-classifier)

# Options

There are many options or flags that controls `pt.py`. Here is a copy and paste version of what `pt.py --help` shows as available options.

```
usage: PyTorch Classification Models [-h] -m MODEL_TYPE [-f] -d DATA_DIR
                                     [-t phase type name order params]
                                     [-b BATCH_SIZE] [-e EPOCHS] [-p]
                                     [--optimizer_params OPTIMIZER_PARAMS]
                                     [--scheduler_params SCHEDULER_PARAMS]
                                     [-w NUM_WORKERS] [-s SEED]
                                     [-o OUTPUT_DIR] [-l LOAD_MODEL]
                                     [--figure_width FIGURE_WIDTH]
                                     [--figure_height FIGURE_HEIGHT]
                                     [--version]

optional arguments:
  -h, --help            show this help message and exit
  -m MODEL_TYPE, --model_type MODEL_TYPE
                        model type
                            For example:
                                - inception_v3
                                - alexnet 
                                - vgg19_bn 
                            For the full list, go to https://pytorch.org/docs/stable/torchvision/models.html.
  -f                    indicates if we are feature extracting (default: False)
                            This option is a flag. If used, then feature extracting will be true, else,
                            feature extracting will be false
                            
  -d DATA_DIR, --data_dir DATA_DIR
                        data directory
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
  -t phase type name order params, --transform phase type name order params
                        transform
                            For example (https://pytorch.org/docs/stable/torchvision/transforms.html)
                                # PIL tranforms
                                train Resize r 0 '{"size": 224}'
                                train CenterCrop cc 1 '{"size": 224}'
                                train ColorJitter cj 2 '{"brightness": 0, "contrast": 0, "saturation": 0, "hue": 0}'
                                train FiveCrop fc 3 '{"size": 0}'
                                train Grayscale gs 4 '{"num_output_channels": 3}'
                                train Pad p 5 '{"padding": 10, "fill": 0, "padding_mode": "constant"}'
                                train RandomAffine ra 6 '{"degrees": [-10,10], "translate": [0.5, 0.5], "scale": [1.0, 1.5], "shear": 5, "resample": false, "fillcolor": 0}'
                                train RandomApply rap 7 '{"transforms": ["r", "cc", "fc"], "p": 0.5}'
                                train RandomChoice rc 8 '{"transforms": ["r", "cc", "fc"]}'
                                train RandomCrop rcr 9 '{"size": [224, 224], "padding": null, "pad_if_needed": false, "fill": 0, "padding_mode": "constant"}'
                                train RandomGrayscale rgs 10 '{"p": 0.1}'
                                train RandomHorizontalFlip rhp 11 '{"p": 0.5}'
                                train RandomOrder ro 12 '{"transforms": ["r", "cc", "fc"]}'
                                train RandomPerspective rp 13 '{"distortion_scale": 0.5, "p": 0.5, "interpolation": 3}'
                                train RandomResizedCrop rrc 14 '{"size": 224, "scale": [0.08, 1.0], "ratio": [0.75, 1.33], "interpolation": 2}'
                                train RandomRotation rrot 15 '{"degrees": 10, "resample": false, "expand": false, "center": null}'
                                train RandomVerticalFlip rvf 16 '{"p": 0.5}'
                                train TenCrop tc 19 '{"size": 224, "vertical_flip": false}'
                                train Compose compose 20 '{"transforms": ["r", "cc", "fc"]}'
                                # tensor transforms
                                train Normalize norm 21 '{"mean": [0.485, 0.456, 0.406], "std": [0.229, 0.224, 0.225]}'
                                train RandomErasing rer 22 '{"p": 0.5, "scale": [0.02, 0.33], "ratio": [0.3, 3.3], "value": 0, "inplace": false}'
                                # conversion transforms
                                train ToTensor tt 23 '{}'
                            Note the pattern: [phase] [official name] [custom name] [order] [parameters]
                                - [phase] specifies the training, testing or validation phases; must be train, test or valid
                                - [official name] the official API name
                                - [custom name] the variable name that will be used to store the instantiation of the transform
                                - [order] the order in which the transform will be placed; use -1 to exclude a transform
                                - [parameters] a JSON parseable string literal serving as parameters to the transform
                            Defining custom transforms will override the default. Use at your own risk!
                            
  -b BATCH_SIZE, --batch_size BATCH_SIZE
                        batch size (default: 4)
  -e EPOCHS, --epochs EPOCHS
                        number of epochs (default: 25)
  -p                    use transfer learning by loading pretrained weights (default: True)
                            To turn off using pretrained weights, pass in -p.
                            By default, without -p, pretrained weights are used.
                            
  --optimizer_params OPTIMIZER_PARAMS
                        optimizer parameters (default: {"lr": 0.001, "momentum": 0.9})
                            torch.optim.SGD is the only optimizer supported.
                            The string you pass in must be parseable by json.loads().
                            Example of a JSON string is as follows.
                            {"lr": 0.001, "momentum": 0.9}
  --scheduler_params SCHEDULER_PARAMS
                        scheduler parameters (default: {"step_size": 7, "gamma": 0.1})
                            torch.optim.lr_scheduler.StepLR is the only scheduler supported.
                            The string you pass in must be parseable by json.loads().
                            Example of a JSON string is as follows.
                            {"step_size": 7, "gamma": 0.1}
  -w NUM_WORKERS, --num_workers NUM_WORKERS
                        number of workers (default: 4)
  -s SEED, --seed SEED  seed used for random number generators (default: 1299827)
                            Use a negative number (e.g. -1) to seed with the current time
                            represented as milliseconds past epoch.
  -o OUTPUT_DIR, --output_dir OUTPUT_DIR
                        output dir (default: /tmp)
                            e.g. /tmp/inception_v3-1565298691256.t
                            Note that the file path is: [model_type]-[milliseconds_past_epoch].t
                            You may only control the output directory, not the file name.
  -l LOAD_MODEL, --load_model LOAD_MODEL
                        path of model to load
                            e.g. /path/to/model.pth
                            If such a path does NOT exists, then a new model (of the model_type) will 
                            be created. If such a path does exists, then that model will be used
                            as a starting point for training.
  --figure_width FIGURE_WIDTH
                        figure width (default: 20)
  --figure_height FIGURE_HEIGHT
                        figure height (default: 8)
  --version             show program's version number and exit

One-Off Coder http://www.oneoffcoder.com
```

The most important options as follows.

* `-m` specifies the model type: `resnet18` `resnet34` `resnet50` `resnet101` `resnet152` `alexnet` `vgg11` `vgg11_bn` `vgg13` `vgg13_bn` `vgg16` `vgg16_bn` `vgg19` `vgg19_bn` `squeezenet1_0` `squeezenet1_1` `densenet121` `densenet161` `densenet169` `densenet201` `googlenet` `shufflenet_v2_x0_5` `shufflenet_v2_x1_0` `mobilenet_v2` `resnext50_32x4d` `resnext101_32x8d` `wide_resnet50_2` `wide_resnet101_2` `mnasnet0_5` `mnasnet1_0` `inception_v3`
* `-d` specifies the data directory containing your images; your data directory **MUST** follow the required PyTorch layout as we are using its `ImageFolder` to build the `DataLoader`. Take a look on the [official documentation](https://pytorch.org/docs/stable/torchvision/datasets.html#imagefolder) to get a better idea of the folder structure of the data directory. The help printout also does a decent job at explaining.
* `-o` specifies the output directory that you want to serialize the PyTorch model to.
* `-e` specifies the number of epochs to train.
* `-t` specifies the transforms: `Resize`, `CenterCrop`, `ColorJitter`, `FiveCrop`, `Grayscale`, `Pad`, `RandomAffine`, `RandomCrop`, `RandomGrayscale`, `RandomHorizontalFlip`, `RandomPerspective`, `RandomResizedCrop`, `RandomRotation`, `RandomVerticalFlip`, `TenCrop`, `Normalize`, `RandomErasing`, `ToTensor`, `RandomChoice`, `RandomOrder`, `RandomApply`, `Compose`. Nearly all transforms (PIL, Tensor, Conversion) are supported. If you define a transform that is incompatible, obviously, the whole process might break. For example, the Inception v3 model requires an image size of 299 while all other models require 224. You may choose to override the `train`, `test` or `valid` transform phases individually or all together.

As for the docker container, you have 2 mounts that you should use to load data and save the models.

* `/data` should be mounted from your local directory storing your images.
* `/model` should be mounted from a local directory where the model will be saved.

# Usage

The following command will run the container and do its default programmed behavior, which is printing the help screen.

```bash
docker run -it dl-classifier:local
```

The following command will start learning from dummy data stored in the `/data` directory. Note that the `/data` is already pre-loaded with this dummy data and no mount is set to that directory. Also, since we do not specify an output directory, the model will be saved on the container in the `/tmp` directory.

```bash
docker run -it \
    --runtime=nvidia \
    --shm-size=5g \
    -e NVIDIA_VISIBLE_DEVICES=0 \
    dl-classifier:local -m inception_v3 -d /data -e 50
```

The following command is the most realistic one as you are mounting your data and folder to save the model.

```bash
docker run -it \
    -v $HOME/git/docker-containers/dl-classifier/faces:/data \
    -v $HOME/git/docker-containers/dl-classifier/model:/model \
    --runtime=nvidia \
    --shm-size=5g \
    -e NVIDIA_VISIBLE_DEVICES=0 \
    dl-classifier:local -m inception_v3 -d /data -e 25 -o /model
```

## Local usage

If you have set up your local (non-Docker) environment and want to try out the code locally.

```bash
# simple testing
python scripts/pt.py \
    -m inception_v3 \
    -d faces-small \
    -e 1 \
    -t train Resize r1 0 '{"size": 299}' \
    -t train CenterCrop c1 1 '{"size": 299}' \
    -t train ToTensor t1 2 '{}' \
    -t train Normalize n1 3 '{"mean": [0.485, 0.456, 0.406], "std": [0.229, 0.224, 0.225]}' \
    -t test Resize r2 0 '{"size": 299}' \
    -t test CenterCrop c2 1 '{"size": 299}' \
    -t test ToTensor t2 2 '{}' \
    -t test Normalize n2 3 '{"mean": [0.485, 0.456, 0.406], "std": [0.229, 0.224, 0.225]}' \
    -t valid Resize r3 0 '{"size": 299}' \
    -t valid CenterCrop c3 1 '{"size": 299}' \
    -t valid ToTensor t3 2 '{}' \
    -t valid Normalize n3 3 '{"mean": [0.485, 0.456, 0.406], "std": [0.229, 0.224, 0.225]}'

# more difficult example
python scripts/pt.py \
    -m inception_v3 \
    -d faces \
    -e 25 \
    -t train Resize r1 0 '{"size": 299}' \
    -t train CenterCrop c1 1 '{"size": 299}' \
    -t train ToTensor t1 2 '{}' \
    -t train Normalize n1 3 '{"mean": [0.485, 0.456, 0.406], "std": [0.229, 0.224, 0.225]}' \
    -t test Resize r2 0 '{"size": 299}' \
    -t test CenterCrop c2 1 '{"size": 299}' \
    -t test ToTensor t2 2 '{}' \
    -t test Normalize n2 3 '{"mean": [0.485, 0.456, 0.406], "std": [0.229, 0.224, 0.225]}' \
    -t valid Resize r3 0 '{"size": 299}' \
    -t valid CenterCrop c3 1 '{"size": 299}' \
    -t valid ToTensor t3 2 '{}' \
    -t valid Normalize n3 3 '{"mean": [0.485, 0.456, 0.406], "std": [0.229, 0.224, 0.225]}'
```

# Take a Look!

Check out [Niklaus Wirth](https://en.wikipedia.org/wiki/Niklaus_Wirth).

# Citation

```
@misc{oneoffcoder_dl_classifier_2019, 
title={An executable docker container with all of PyTorch classification models}, 
url={https://github.com/oneoffcoder/docker-containers/tree/master/dl-classifier}, 
journal={GitHub},
author={One-Off Coder}, 
year={2019}, 
month={Aug}}
```
