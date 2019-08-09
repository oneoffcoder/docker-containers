# Purpose 

This project is an executable container with [all of PyTorch's convolutional neural networks](https://pytorch.org/docs/stable/torchvision/models.html) (CNNs). You may use it with ease to train, test and validate against your own data. All the available pre-trained model weights are downloaded into the container already. The way this container works is with the helper Python program `pt.py` and the docker instructions `ENTRYPOINT` and `CMD`. The `ENTRYPOINT` instruction points to `pt.py` and the `CMD` instruction passes in the `--help` flag. At runtime, you override what `CMD` passes to `pt.py` by specifying appropriate flags.

# Source

[GitHub](https://github.com/oneoffcoder/docker-containers/tree/master/dl-classifier)

# Options

There are many options or flags that controls `pt.py`. Here is a copy and paste version of what `pt.py --help` shows as available options.

```
usage: PyTorch Classification Models [-h] -m MODEL_TYPE [-f] -d DATA_DIR
                                     [-b BATCH_SIZE] [-e EPOCHS] [-p]
                                     [--optimizer_params OPTIMIZER_PARAMS]
                                     [--scheduler_params SCHEDULER_PARAMS]
                                     [-w NUM_WORKERS] [-s SEED]
                                     [-o OUTPUT_DIR] [-l LOAD_MODEL]
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
  --version             show program's version number and exit
```

The most important options as follows.

* `-m` specifies the model type (e.g. inception_v3, alexnet, vgg19_bn, etc...).
* `-d` specifies the data directory containing your images; your data directory **MUST** follow the required PyTorch layout as we are using its `ImageFolder` to build the `DataLoader`. Take a look on the [official documentation](https://pytorch.org/docs/stable/torchvision/datasets.html#imagefolder) to get a better idea of the folder structure of the data directory. The help printout also does a decent job at explaining.
* `-o` specifies the output directory that you want to serialize the PyTorch model to.
* `-e` specifies the number of epochs to train.

As for the docker container, you have 2 mounts that you should use to load data and save the models.

* `/data` should be mounted from your local directory storing your images.
* `/model` should be mounted from a local directory where the model will be saved.

# Usage

The following command will run the container and do its default programmed behavior, which is printing the help screen.

```bash
docker run -it oneoffcoder/dl-classifier
```

The following command will start learning from dummy data stored in the `/data` directory. Note that the `/data` is already pre-loaded with this dummy data and no mount is set to that directory. Also, since we do not specify an output directory, the model will be saved on the container in the `/tmp` directory.

```bash
docker run -it \
    --runtime=nvidia \
    --shm-size=5g \
    -e NVIDIA_VISIBLE_DEVICES=0 \
    oneoffcoder/dl-classifier -m inception_v3 -d /data -e 50
```

The following command is the most realistic one as you are mounting your data and folder to save the model.

```bash
docker run -it \
    -v $HOME/git/docker-containers/dl-classifier/faces:/data \
    -v $HOME/git/docker-containers/dl-classifier/model:/model \
    --runtime=nvidia \
    --shm-size=5g \
    -e NVIDIA_VISIBLE_DEVICES=0 \
    oneoffcoder/dl-classifier -m inception_v3 -d /data -e 25 -o /model
```
