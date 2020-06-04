#!/bin/bash

ORGANIZATION=oneoffcoder
REPOSITORY=spark-jupyter
VERSION=0.0.8
IMAGEID=spark-jupyter:local

echo ${IMAGEID}

docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:latest
