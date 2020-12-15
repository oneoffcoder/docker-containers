#!/bin/bash

ORGANIZATION=oneoffcoder
REPOSITORY=sphinx-autobuild
VERSION=0.0.2
IMAGEID=$REPOSITORY:local

echo ${IMAGEID}

docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:latest

docker push ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker push ${ORGANIZATION}/${REPOSITORY}:latest