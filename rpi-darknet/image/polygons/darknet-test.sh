#!/bin/bash

./darknet detector \
  test \
  /darknet/image/polygons/iaia-polygons.data \
  /darknet/image/polygons/yolo-iaia-polygons.cfg \
  /darknet/backup/yolo-iaia-polygons_last.weights \
  -ext_output \
  -dont_show \
  -out /darknet/log/result.json < /darknet/image/polygons/iaia-polygons_valid.txt

./darknet detector \
  test \
  /darknet/image/polygons/iaia-polygons.data \
  /darknet/image/polygons/tiny-yolo-iaia-polygons.cfg \
  /darknet/backup/tiny-yolo-iaia-polygons_last.weights \
  -ext_output \
  -dont_show \
  -out /darknet/log/result.json < /darknet/image/polygons/iaia-polygons_valid.txt