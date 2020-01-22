# Yolo v3 using PyTorch

Towards the purpose of pose estimation, this container is used for detecting humans in images using [Yolo v3 with a PyTorch implementation](https://github.com/eriklindernoren/PyTorch-YOLOv3). You will need to use this container to first detect humans in images, then another container to estimate the poses of the humans in each picture.

To build the container, you need to download the weights.

```bash
cd weights
bash download_weights.sh
```

Then use the build script.

```bash
./build.sh
```

In order to use the Docker image, you need to set up your input directories in a certain way. 

```
custom/
├── annots
├── cuts
├── images
└── inspect
```

Here, we have a root folder called `custom`. 

* All your input images should be placed in `custom/images`, and all sub-directories should be empty. 
* The `custom/annots` will store the annotations (bounding-boxes) of where humans are detected. These are just a bunch of JSON files (output).
* The `custom/cuts` folder will store the cut images; one input image may generate multiple cuts if there are more than one human detected. These are just a bunch of JPG files (output).
* The `custom/inspect` will store the images with the bounding boxes of where humans were detected for visual inspection. These are just a bunch of JPG files (output).

To use the Docker image, then issue a command like the following. Note that you must have CUDA and cuDNN installed. Take note of the mount which mounts your `custom` directory to the container `/yolo/custom` directory.

```bash
docker run -it \
    -v `pwd`/custom:/yolo/custom \
    --gpus=all \
    --shm-size=5g \
    oneoffcoder/dl-pose-yolo \
      --image_folder custom/images \
      --annot_folder custom/annots \
      --inspect_folder custom/inspect \
      --cut_folder custom/cuts \
      --batch_size 8 \
      --n_cpu 8
```

# Citation

```
@misc{oneoffcoder_dl_pose_yolo_2019, 
title={An executable docker container with YOLO V3 for pose estimation}, 
url={https://github.com/oneoffcoder/docker-containers/tree/master/dl-pose-yolo}, 
journal={GitHub},
author={One-Off Coder}, 
year={2020}, 
month={Jan}}
```