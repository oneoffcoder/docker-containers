#!/bin/bash

IMAGEID=$(docker images | awk '$1 ~ /conda-deeplearning/ { print $3}')
VERSION=0.0.2
docker tag $IMAGEID vangjee/conda-deeplearning:$VERSION
docker tag $IMAGEID vangjee/conda-deeplearning:latest

docker push vangjee/conda-deeplearning:$VERSION
docker push vangjee/conda-deeplearning:latest