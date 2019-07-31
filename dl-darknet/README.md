# Interactive terminal mode

To run local build with GPU support.

```bash
docker run -it \
    --runtime=nvidia \
    --shm-size=5g \
    -e NVIDIA_VISIBLE_DEVICES=0 \
    dl-darknet:local

docker run -it \
    --runtime=nvidia \
    --shm-size=5g \
    -e NVIDIA_VISIBLE_DEVICES=0 \
    dl-darknet:local \
    darknet detect \
    cfg/yolov3-tiny.cfg \
    weight/yolov3-tiny.weights \
    data/dog.jpg
```

## Useful commands

To test if OpenCV was installed correctly.

```bash
python -c "import cv2; print(cv2.__version__)"
```

To run Yolo v3 with tiny weights.

```bash
time ./darknet detect \
    cfg/yolov3-tiny.cfg \
    weight/yolov3-tiny.weights \
    data/dog.jpg
```

To run Yolo v3 with normal weights.

```bash
time ./darknet detect \
    cfg/yolov3.cfg \
    weight/yolov3.weights \
    data/dog.jpg
```

To run Yolo v3 full command.

```bash
time ./darknet detector \
    test cfg/coco.data \
    cfg/yolov3.cfg \
    weight/yolov3.weights \
    data/dog.jpg
```