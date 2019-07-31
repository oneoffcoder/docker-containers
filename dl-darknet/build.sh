#!/bin/bash

REPOSITORY=dl-darknet
TAG=local

docker build --no-cache -t $REPOSITORY:$TAG .