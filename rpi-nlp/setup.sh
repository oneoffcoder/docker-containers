#!/bin/bash

BASE_DIR=/root/miniconda/bin
CONDA=$BASE_DIR/conda
PYTHON=/root/miniconda/envs/py36/bin/python

echo "update environment"
$CONDA env update -f /tmp/environment.yml

echo "download nltk packages"
$PYTHON -m nltk.downloader all