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
    -v $HOME/git/docker-containers/dl-darknet/cfg:/darknet/cfg \
    -v $HOME/git/docker-containers/dl-darknet/data:/darknet/data \
    -v $HOME/git/docker-containers/dl-darknet/image:/darknet/image \
    -v $HOME/git/docker-containers/dl-darknet/video:/darknet/video \
    dl-darknet:local \
    /bin/sh -c 'cd /darknet; ./darknet detector test cfg/coco.data cfg/yolov3-tiny.cfg weight/yolov3-tiny.weights data/dog.jpg -dont_show'

docker run -it \
    --runtime=nvidia \
    --shm-size=5g \
    -e NVIDIA_VISIBLE_DEVICES=0 \
    -v $HOME/git/docker-containers/dl-darknet/cfg:/darknet/cfg \
    -v $HOME/git/docker-containers/dl-darknet/data:/darknet/data \
    -v $HOME/git/docker-containers/dl-darknet/image:/darknet/image \
    -v $HOME/git/docker-containers/dl-darknet/video:/darknet/video \
    dl-darknet:local \
    /bin/sh -c 'cd /darknet; ./darknet detector test cfg/coco.data cfg/yolov3.cfg weight/yolov3.weights data/dog.jpg -dont_show'

docker run -it \
    --runtime=nvidia \
    --shm-size=5g \
    -e NVIDIA_VISIBLE_DEVICES=0 \
    -v $HOME/git/docker-containers/dl-darknet/cfg:/darknet/cfg \
    -v $HOME/git/docker-containers/dl-darknet/data:/darknet/data \
    -v $HOME/git/docker-containers/dl-darknet/image:/darknet/image \
    -v $HOME/git/docker-containers/dl-darknet/video:/darknet/video \
    dl-darknet:local \
    /bin/sh -c 'cd /darknet; ./darknet detector demo cfg/coco.data cfg/yolov3.cfg weight/yolov3.weights video/dummy.mp4 -out_filename video/dummy.avi -dont_show'
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