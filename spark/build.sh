#!/bin/bash

docker build --no-cache -t spark0:local -f Dockerfile.stage0 .
docker build --no-cache -t spark:local -f Dockerfile.stage1 .
