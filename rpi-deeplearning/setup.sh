#!/bin/bash

BASE_DIR=/root/miniconda/bin
CONDA=$BASE_DIR/conda
PYTHON=$BASE_DIR/python

echo "update environment"
$CONDA env update -f /tmp/environment.yml
