# Use as a command line

To detect with Yolo v3 tiny weights.

```bash
docker run -it \
    --runtime=nvidia \
    --shm-size=5g \
    -e NVIDIA_VISIBLE_DEVICES=0 \
    -v $HOME/git/docker-containers/dl-darknet/cfg:/darknet/cfg \
    -v $HOME/git/docker-containers/dl-darknet/data:/darknet/data \
    -v $HOME/git/docker-containers/dl-darknet/image:/darknet/image \
    -v $HOME/git/docker-containers/dl-darknet/video:/darknet/video \
    -v $HOME/git/docker-containers/dl-darknet/log:/darknet/log \
    dl-darknet:local \
    /bin/sh -c "cd /darknet; ./darknet detector test cfg/coco.data cfg/yolov3-tiny.cfg weight/yolov3-tiny.weights data/dog.jpg -dont_show > image/dog.log"

docker run -it \
    --runtime=nvidia \
    --shm-size=5g \
    -e NVIDIA_VISIBLE_DEVICES=0 \
    -v $HOME/git/docker-containers/dl-darknet/cfg:/darknet/cfg \
    -v $HOME/git/docker-containers/dl-darknet/data:/darknet/data \
    -v $HOME/git/docker-containers/dl-darknet/image:/darknet/image \
    -v $HOME/git/docker-containers/dl-darknet/video:/darknet/video \
    -v $HOME/git/docker-containers/dl-darknet/log:/darknet/log \
    dl-darknet:local \
    /bin/sh -c "cd /darknet; ./darknet detector test cfg/coco.data cfg/yolov3-tiny.cfg weight/yolov3-tiny.weights data/eagle.jpg -dont_show > image/eagle.log"
```

To detect with Yolo v3 normal weights.

```bash
docker run -it \
    --runtime=nvidia \
    --shm-size=5g \
    -e NVIDIA_VISIBLE_DEVICES=0 \
    -v $HOME/git/docker-containers/dl-darknet/cfg:/darknet/cfg \
    -v $HOME/git/docker-containers/dl-darknet/data:/darknet/data \
    -v $HOME/git/docker-containers/dl-darknet/image:/darknet/image \
    -v $HOME/git/docker-containers/dl-darknet/video:/darknet/video \
    -v $HOME/git/docker-containers/dl-darknet/log:/darknet/log \
    dl-darknet:local \
    /bin/sh -c 'cd /darknet; ./darknet detector test cfg/coco.data cfg/yolov3.cfg weight/yolov3.weights data/dog.jpg -dont_show'
```

To detect with Yolo v3 on MP4 file.

```bash
docker run -it \
    --runtime=nvidia \
    --shm-size=5g \
    -e NVIDIA_VISIBLE_DEVICES=0 \
    -v $HOME/git/docker-containers/dl-darknet/cfg:/darknet/cfg \
    -v $HOME/git/docker-containers/dl-darknet/data:/darknet/data \
    -v $HOME/git/docker-containers/dl-darknet/image:/darknet/image \
    -v $HOME/git/docker-containers/dl-darknet/video:/darknet/video \
    -v $HOME/git/docker-containers/dl-darknet/log:/darknet/log \
    dl-darknet:local \
    /bin/sh -c 'cd /darknet; ./darknet detector demo cfg/coco.data cfg/yolov3.cfg weight/yolov3.weights video/dummy.mp4 -out_filename video/dummy.avi -dont_show'
```

To detect with Yolo v3 on MP4 file and redirect output to JSON + MJPEG + AVI. After you run the command below, direct your browsers to the following URLs.

* http://localhost:8070 for the JSON data of the annotations
* http://localhost:8090 for the annotated video

```bash
docker run -it \
    --runtime=nvidia \
    --shm-size=5g \
    -e NVIDIA_VISIBLE_DEVICES=0 \
    -v $HOME/git/docker-containers/dl-darknet/cfg:/darknet/cfg \
    -v $HOME/git/docker-containers/dl-darknet/data:/darknet/data \
    -v $HOME/git/docker-containers/dl-darknet/image:/darknet/image \
    -v $HOME/git/docker-containers/dl-darknet/video:/darknet/video \
    -v $HOME/git/docker-containers/dl-darknet/log:/darknet/log \
    -p 8070:8070 \
    -p 8090:8090 \
    dl-darknet:local \
    /bin/sh -c 'cd /darknet; ./darknet detector demo cfg/coco.data cfg/yolov3.cfg weight/yolov3.weights video/dummy.mp4 -json_port 8070 -mjpeg_port 8090 -ext_output -dont_show -out_filename video/dummy.avi'
```



# Use in interactive terminal mode

To run local build with GPU support.

```bash
docker run -it \
    --runtime=nvidia \
    --shm-size=5g \
    -e NVIDIA_VISIBLE_DEVICES=0 \
    dl-darknet:local
```

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

# Links

* https://github.com/pjreddie/darknet
* https://github.com/AlexeyAB/darknet