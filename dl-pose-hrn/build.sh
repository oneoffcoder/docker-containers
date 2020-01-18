#!/bin/bash

REPOSITORY=dl-pose-hrn
TAG=local

docker build --no-cache -t $REPOSITORY:$TAG .
