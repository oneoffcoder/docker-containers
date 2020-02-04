#!/bin/bash

ORGANIZATION=oneoffcoder
REPOSITORY=cpp-cicd
VERSION=0.0.1
IMAGEID=cpp-cicd:local

docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:latest

docker push ${ORGANIZATION}/${REPOSITORY}:${VERSION}
docker push ${ORGANIZATION}/${REPOSITORY}:latest