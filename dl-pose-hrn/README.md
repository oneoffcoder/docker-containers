# Deep High-Resolution Network

This container is used to [estimate pose](https://github.com/leoxiaobin/deep-high-resolution-net.pytorch). Pose estimation using this container is a two step process.

1. Use [Yolo](https://hub.docker.com/repository/docker/oneoffcoder/dl-pose-yolo) to detect the humans in an image.
2. Use this container to estimate the pose of each human in an image.

To build the container, you will need to download the models first; see [Deep High-Resolution Network](https://github.com/leoxiaobin/deep-high-resolution-net.pytorch) instructions. After you download the models, you should place the models in a directory called `models` with the following structure.

```
models/
└── pytorch
    ├── imagenet
    ├── pose_coco
    └── pose_mpii
```

Then use the build script.

```bash
./build.sh
```

You need to set up your input directories in a certain way. Look [here](https://hub.docker.com/repository/docker/oneoffcoder/dl-pose-yolo) for more information on the meaning of this directory layout.

```
custom/
├── annots
├── cuts
├── images
└── inspect
```

Run the [Yolo container](https://hub.docker.com/repository/docker/oneoffcoder/dl-pose-yolo) to detect where the humans are located in your images.

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

Now, run this container to estimate the human poses.

```bash
docker run -it \
    -v `pwd`/custom:/hrn/custom \
    --gpus=all \
    --shm-size=5g \
    oneoffcoder/dl-pose-hrn \
      --circle 0 \
      --label 0 \
      --line 1 \
      --line_thickness 2 \
      --cfg custom/w32_256x256_adam_lr1e-3.yaml
```

The key is in the configuration file, specified by the `--cfg` flag, `custom/w32_256x256_adam_lr1e-3.yaml`. Note that this file should be placed at the root (under `custom`). Pay attention to the `ANNOTS`, `IMAGES`, `CUTS` and `FINAL` parameters for `DATASET`. Here's the example.

```yaml
AUTO_RESUME: true
CUDNN:
  BENCHMARK: true
  DETERMINISTIC: false
  ENABLED: true
DATA_DIR: ''
GPUS: (0,)
OUTPUT_DIR: 'custom/output'
LOG_DIR: 'log'
WORKERS: 24
PRINT_FREQ: 100

DATASET:
  COLOR_RGB: true
  DATASET: custom
  DATA_FORMAT: jpg
  FLIP: true
  NUM_JOINTS_HALF_BODY: 8
  PROB_HALF_BODY: -1.0
  ROOT: 'data/example/'
  ROT_FACTOR: 30
  SCALE_FACTOR: 0.25
  TEST_SET: valid
  TRAIN_SET: train
  ANNOTS: 'custom/annots'
  IMAGES: 'custom/images'
  CUTS: 'custom/cuts'
  FINAL: 'custom/final'
MODEL:
  INIT_WEIGHTS: true
  NAME: pose_hrnet
  NUM_JOINTS: 16
  PRETRAINED: 'models/pytorch/pose_mpii/pose_hrnet_w32_256x256.pth'
  TARGET_TYPE: gaussian
  IMAGE_SIZE:
  - 256
  - 256
  HEATMAP_SIZE:
  - 64
  - 64
  SIGMA: 2
  EXTRA:
    PRETRAINED_LAYERS:
    - 'conv1'
    - 'bn1'
    - 'conv2'
    - 'bn2'
    - 'layer1'
    - 'transition1'
    - 'stage2'
    - 'transition2'
    - 'stage3'
    - 'transition3'
    - 'stage4'
    FINAL_CONV_KERNEL: 1
    STAGE2:
      NUM_MODULES: 1
      NUM_BRANCHES: 2
      BLOCK: BASIC
      NUM_BLOCKS:
      - 4
      - 4
      NUM_CHANNELS:
      - 32
      - 64
      FUSE_METHOD: SUM
    STAGE3:
      NUM_MODULES: 4
      NUM_BRANCHES: 3
      BLOCK: BASIC
      NUM_BLOCKS:
      - 4
      - 4
      - 4
      NUM_CHANNELS:
      - 32
      - 64
      - 128
      FUSE_METHOD: SUM
    STAGE4:
      NUM_MODULES: 3
      NUM_BRANCHES: 4
      BLOCK: BASIC
      NUM_BLOCKS:
      - 4
      - 4
      - 4
      - 4
      NUM_CHANNELS:
      - 32
      - 64
      - 128
      - 256
      FUSE_METHOD: SUM
LOSS:
  USE_TARGET_WEIGHT: true
TRAIN:
  BATCH_SIZE_PER_GPU: 32
  SHUFFLE: true
  BEGIN_EPOCH: 0
  END_EPOCH: 210
  OPTIMIZER: adam
  LR: 0.001
  LR_FACTOR: 0.1
  LR_STEP:
  - 170
  - 200
  WD: 0.0001
  GAMMA1: 0.99
  GAMMA2: 0.0
  MOMENTUM: 0.9
  NESTEROV: false
TEST:
  BATCH_SIZE_PER_GPU: 1
  MODEL_FILE: ''
  FLIP_TEST: true
  POST_PROCESS: true
  SHIFT_HEATMAP: true
DEBUG:
  DEBUG: true
  SAVE_BATCH_IMAGES_GT: true
  SAVE_BATCH_IMAGES_PRED: true
  SAVE_HEATMAPS_GT: true
  SAVE_HEATMAPS_PRED: true
```

The `circle`, `label` and `line` flags indicate if you want the final annotated (output) pictures to have circles, labels or lines. After you run the container against your input data, you should have a `custom/final` folder with your input images annotated with the pose estimations. There will also be a `custom/output` folder for debugging purposes.