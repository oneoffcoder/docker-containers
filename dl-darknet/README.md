![One-Off Coder Logo](../logo.png "One-Off Coder")

# Purpose

The purpose of this docker image is to dockerize [darknet](https://pjreddie.com/darknet/) so that you may easily use it and also in a portable manner.

# Docker Hub

[Image](https://hub.docker.com/r/oneoffcoder/dl-darknet)

# Use as a command line

Detection with tiny weights.

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
    -v $HOME/git/docker-containers/dl-darknet/backup:/darknet/backup \
    -v $HOME/git/docker-containers/dl-darknet/scripts:/root/scripts \
    dl-darknet:local \
    detector test cfg/coco.data cfg/yolov3-tiny.cfg weight/yolov3-tiny.weights data/dog.jpg -dont_show > image/dog.log
```

Detection with normal weights.

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
    -v $HOME/git/docker-containers/dl-darknet/backup:/darknet/backup \
    -v $HOME/git/docker-containers/dl-darknet/scripts:/root/scripts \
    dl-darknet:local \
    detector test cfg/coco.data cfg/yolov3.cfg weight/yolov3.weights data/dog.jpg -dont_show > image/dog2.log
```

Detection on a MP4 file.

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
    -v $HOME/git/docker-containers/dl-darknet/backup:/darknet/backup \
    -v $HOME/git/docker-containers/dl-darknet/scripts:/root/scripts \
    dl-darknet:local \
    detector demo cfg/coco.data cfg/yolov3.cfg weight/yolov3.weights video/dummy.mp4 -out_filename video/dummy.avi -dont_show
```

Detection on a MP4 file and output to JSON + MJPEG + AVI. After you run the command below, direct your browsers to the following URLs.

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
    -v $HOME/git/docker-containers/dl-darknet/backup:/darknet/backup \
    -v $HOME/git/docker-containers/dl-darknet/scripts:/root/scripts \
    -p 8070:8070 \
    -p 8090:8090 \
    dl-darknet:local \
    detector demo cfg/coco.data cfg/yolov3.cfg weight/yolov3.weights video/dummy.mp4 -json_port 8070 -mjpeg_port 8090 -ext_output -dont_show -out_filename video/dummy.avi
```

Detection on a real-time video stream and redirect output to JSON + MJPEG + AVIG. Note that you can test the below by downloading and installing [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam) on your phone; replace the IP below with the one on your phone (the software on the phone will show you what the phone's IP is).

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
    -v $HOME/git/docker-containers/dl-darknet/backup:/darknet/backup \
    -v $HOME/git/docker-containers/dl-darknet/scripts:/root/scripts \
    -p 8070:8070 \
    -p 8090:8090 \
    dl-darknet:local \
    detector demo cfg/coco.data cfg/yolov3.cfg weight/yolov3.weights http://192.168.0.210:8080/video?dummy=param.mjpg -json_port 8070 -mjpeg_port 8090 -ext_output -dont_show -out_filename video/dummy.avi
```

Training your own object detector.

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
    -v $HOME/git/docker-containers/dl-darknet/backup:/darknet/backup \
    -v $HOME/git/docker-containers/dl-darknet/scripts:/root/scripts \
    dl-darknet:local \
    detector train /darknet/image/polygons/iaia-polygons.data /darknet/image/polygons/tiny-yolo-iaia-polygons.cfg -dont_show
```

Testing your own object detector.

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
    -v $HOME/git/docker-containers/dl-darknet/backup:/darknet/backup \
    -v $HOME/git/docker-containers/dl-darknet/scripts:/root/scripts \
    dl-darknet:local \
    detector test /darknet/image/polygons/iaia-polygons.data /darknet/image/polygons/tiny-yolo-iaia-polygons.cfg /darknet/backup/tiny-yolo-iaia-polygons_last.weights -ext_output -dont_show -out /darknet/log/result.json < /darknet/image/polygons/iaia-polygons_valid.txt
```

Annotating the images with the results.

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
    -v $HOME/git/docker-containers/dl-darknet/backup:/darknet/backup \
    -v $HOME/git/docker-containers/dl-darknet/scripts:/root/scripts \
    --entrypoint /opt/anaconda/bin/python \
    dl-darknet:local \
    /root/scripts/annotate.py -j /darknet/log/result.json  -d /darknet/image/polygons/annotations
```

# Use in interactive terminal mode

To run local build with GPU support.

```bash
docker run -it \
    --runtime=nvidia \
    --shm-size=5g \
    -e NVIDIA_VISIBLE_DEVICES=0 \
    --entrypoint /bin/bash \
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

# Take a Look!

Check out [Grace Hopper](https://en.wikipedia.org/wiki/Grace_Hopper).

# Citation

```
@misc{oneoffcoder_dl_darknet_2019, 
title={Docker container with darknet}, 
url={https://github.com/oneoffcoder/docker-containers/tree/master/dl-darknet}, 
journal={GitHub},
author={One-Off Coder}, 
year={2019}, 
month={Jul}}
```