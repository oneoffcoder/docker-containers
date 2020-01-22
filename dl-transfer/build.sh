#!/bin/bash

REPOSITORY=dl-transfer
TAG=local

docker build --no-cache -t $REPOSITORY:$TAG .