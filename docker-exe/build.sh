#!/bin/bash

REPOSITORY=docker-exe
TAG=local

docker build --no-cache -t $REPOSITORY:$TAG .