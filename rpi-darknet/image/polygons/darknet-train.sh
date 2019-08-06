#!/bin/bash

./darknet detector train \
  /darknet/image/polygons/iaia-polygons.data \
  /darknet/image/polygons/yolo-iaia-polygons.cfg \
  -dont_show

./darknet detector train \
  /darknet/image/polygons/iaia-polygons.data \
  /darknet/image/polygons/tiny-yolo-iaia-polygons.cfg \
  -dont_show