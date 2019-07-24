#!/bin/bash

REPOSITORY=rpi-deeplearning
TAG=local

docker build --no-cache -t $REPOSITORY:$TAG .