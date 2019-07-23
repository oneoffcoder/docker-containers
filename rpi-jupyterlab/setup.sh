#!/bin/bash

BASE_DIR=/root/miniconda/bin
CONDA=$BASE_DIR/conda
PIP=$BASE_DIR/pip
JUPYTER=$BASE_DIR/jupyter
PYTHON=$BASE_DIR/python

$CONDA update -n root conda -y
$CONDA update --all -y
$PIP install --upgrade pip
$CONDA install --file /tmp/requirements.txt -y
$CONDA env create -f /tmp/environment.yml --quiet
$PYTHON -m ipykernel install --user --name py36 --display-name "py36"