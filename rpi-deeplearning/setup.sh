#!/bin/bash

BASE_DIR=/root/miniconda/bin
CONDA=$BASE_DIR/conda
PYTHON=$BASE_DIR/python

echo "update environment"
$CONDA env update -f /tmp/environment.yml

$CONDA create -n p34 python=3.4 -y
$CONDA create -n p35 python=3.5 -y

$PYTHON -m ipykernel install --user --name py34 --display-name "py34"
$PYTHON -m ipykernel install --user --name py35 --display-name "py35"