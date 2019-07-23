#!/bin/bash

BASE_DIR=/root/miniconda/bin
CONDA=$BASE_DIR/conda
PIP=$BASE_DIR/pip
JUPYTER=$BASE_DIR/jupyter
PYTHON=$BASE_DIR/python

echo "update conda"
$CONDA update -n root conda -y

echo "update conda all"
$CONDA update --all -y

echo "update pip"
$PIP install --upgrade pip

echo "update environment"
$CONDA env update -f /tmp/environment.yml --prune