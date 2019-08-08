#!/bin/bash

REPOSITORY=dl-classifier
TAG=local

docker build --no-cache -t $REPOSITORY:$TAG .