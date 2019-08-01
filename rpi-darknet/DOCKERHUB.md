# Purpose

The purpose of this docker image is to dockerize [darknet](https://pjreddie.com/darknet/) so that you may easily use it in a portable manner on your Raspbery Pi.

# Source

[GitHub](https://github.com/oneoffcoder/docker-containers/tree/master/rpi-darknet)

# Detection

Detection with tiny weights.

```bash
docker run -it \
    -v $HOME/git/docker-containers/rpi-darknet/cfg:/darknet/cfg \
    -v $HOME/git/docker-containers/rpi-darknet/data:/darknet/data \
    -v $HOME/git/docker-containers/rpi-darknet/image:/darknet/image \
    -v $HOME/git/docker-containers/rpi-darknet/video:/darknet/video \
    -v $HOME/git/docker-containers/rpi-darknet/log:/darknet/log \
    -v $HOME/git/docker-containers/rpi-darknet/backup:/darknet/backup \
    -v $HOME/git/docker-containers/rpi-darknet/scripts:/root/scripts \
    rpi-darknet:local \
    /bin/sh -c "cd /darknet; ./darknet detector test cfg/coco.data cfg/yolov3-tiny.cfg weight/yolov3-tiny.weights data/dog.jpg -dont_show > image/dog.log"
```

Detection on a real-time video stream and redirect output to JSON + MJPEG + AVIG. Note that you can test the below by downloading and installing [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam) on your phone; replace the IP below with the one on your phone (the software on the phone will show you what the phone's IP is).

```bash
docker run -it \
    -v $HOME/git/docker-containers/rpi-darknet/cfg:/darknet/cfg \
    -v $HOME/git/docker-containers/rpi-darknet/data:/darknet/data \
    -v $HOME/git/docker-containers/rpi-darknet/image:/darknet/image \
    -v $HOME/git/docker-containers/rpi-darknet/video:/darknet/video \
    -v $HOME/git/docker-containers/rpi-darknet/log:/darknet/log \
    -v $HOME/git/docker-containers/rpi-darknet/backup:/darknet/backup \
    -v $HOME/git/docker-containers/rpi-darknet/scripts:/root/scripts \
    rpi-darknet:local \
    /bin/sh -c 'cd /darknet; ./darknet detector demo cfg/coco.data cfg/yolov3.cfg weight/yolov3.weights http://192.168.0.210:8080/video?dummy=param.mjpg -json_port 8070 -mjpeg_port 8090 -ext_output -dont_show -out_filename video/dummy.avi'
```

# Training
Training your own object detector.

```bash
docker run -it \
    -v $HOME/git/docker-containers/rpi-darknet/cfg:/darknet/cfg \
    -v $HOME/git/docker-containers/rpi-darknet/data:/darknet/data \
    -v $HOME/git/docker-containers/rpi-darknet/image:/darknet/image \
    -v $HOME/git/docker-containers/rpi-darknet/video:/darknet/video \
    -v $HOME/git/docker-containers/rpi-darknet/log:/darknet/log \
    -v $HOME/git/docker-containers/rpi-darknet/backup:/darknet/backup \
    -v $HOME/git/docker-containers/rpi-darknet/scripts:/root/scripts \
    rpi-darknet:local \
    /bin/sh -c 'cd /darknet; ./darknet detector train /darknet/image/polygons/iaia-polygons.data /darknet/image/polygons/tiny-yolo-iaia-polygons.cfg -dont_show'
```

Testing your own object detector.

```bash
docker run -it \
    -v $HOME/git/docker-containers/rpi-darknet/cfg:/darknet/cfg \
    -v $HOME/git/docker-containers/rpi-darknet/data:/darknet/data \
    -v $HOME/git/docker-containers/rpi-darknet/image:/darknet/image \
    -v $HOME/git/docker-containers/rpi-darknet/video:/darknet/video \
    -v $HOME/git/docker-containers/rpi-darknet/log:/darknet/log \
    -v $HOME/git/docker-containers/rpi-darknet/backup:/darknet/backup \
    -v $HOME/git/docker-containers/rpi-darknet/scripts:/root/scripts \
    rpi-darknet:local \
    /bin/sh -c 'cd /darknet; ./darknet detector test /darknet/image/polygons/iaia-polygons.data /darknet/image/polygons/tiny-yolo-iaia-polygons.cfg /darknet/backup/tiny-yolo-iaia-polygons_last.weights -ext_output -dont_show -out /darknet/log/result.json < /darknet/image/polygons/iaia-polygons_valid.txt'
```

Annotating the images with the results.

```bash
docker run -it \
    -v $HOME/git/docker-containers/rpi-darknet/cfg:/darknet/cfg \
    -v $HOME/git/docker-containers/rpi-darknet/data:/darknet/data \
    -v $HOME/git/docker-containers/rpi-darknet/image:/darknet/image \
    -v $HOME/git/docker-containers/rpi-darknet/video:/darknet/video \
    -v $HOME/git/docker-containers/rpi-darknet/log:/darknet/log \
    -v $HOME/git/docker-containers/rpi-darknet/backup:/darknet/backup \
    -v $HOME/git/docker-containers/rpi-darknet/scripts:/root/scripts \
    rpi-darknet:local \
    /bin/sh -c '/opt/anaconda/bin/python /root/scripts/annotate.py -j /darknet/log/result.json  -d /darknet/image/polygons/annotations'
```