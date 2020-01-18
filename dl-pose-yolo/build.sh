#!/bin/bash

REPOSITORY=dl-pose-yolo
TAG=local

docker build --no-cache -t $REPOSITORY:$TAG .
