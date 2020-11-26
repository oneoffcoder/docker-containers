#!/bin/bash

ORGANIZATION=oneoffcoder
REPOSITORY=python-java
VERSION=0.0.1
IMAGEID=python-java:local

echo ${IMAGEID}

docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:latest

docker push ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker push ${ORGANIZATION}/${REPOSITORY}:latest