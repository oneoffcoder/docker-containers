#!/bin/bash

REPOSITORY=rpi-darknet
TAG=local

docker build --no-cache -t $REPOSITORY:$TAG .