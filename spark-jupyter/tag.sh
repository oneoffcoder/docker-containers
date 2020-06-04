#!/bin/bash

ORGANIZATION=oneoffcoder
REPOSITORY=spark-jupyter
IMAGEID=spark-jupyter:local

docker tag ${IMAGEID} ${ORGANIZATION}/${REPOSITORY}:latest
