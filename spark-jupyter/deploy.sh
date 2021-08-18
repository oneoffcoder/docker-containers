#!/bin/bash

ORGANIZATION=oneoffcoder
REPOSITORY=spark-jupyter
VERSION=0.1.0
IMAGEID=spark-jupyter:local

echo ${IMAGEID}

docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:latest

docker push ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker push ${ORGANIZATION}/${REPOSITORY}:latest