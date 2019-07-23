#!/bin/bash

BASE_DIR=/usr/local/miniconda/bin
CONDA=$BASE_DIR/conda
PIP=$BASE_DIR/pip
JUPYTER=$BASE_DIR/jupyter
PYTHON=$BASE_DIR/python

$CONDA update -n root conda -y
$CONDA update --all -y
$PIP install --upgrade pip
$CONDA env create -f /tmp/environment.yml --quiet
$PYTHON -m ipykernel install --name sklearn --display-name "sklearn"