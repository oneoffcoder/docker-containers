#!/bin/bash

BASE_DIR=/root/miniconda/bin
CONDA=$BASE_DIR/conda
PIP=$BASE_DIR/pip
JUPYTER=$BASE_DIR/jupyter
PYTHON=$BASE_DIR/python

echo "update conda"
$CONDA update -n root conda -y

echo "update all for conda"
$CONDA update --all -y

echo "update pip"
$PIP install --upgrade pip

echo "install requirements.txt"
$CONDA install --file /tmp/requirements.txt -y

echo "create new environment"
$CONDA env create -f /tmp/environment.yml --quiet

echo "install kernel for new environment"
$PYTHON -m ipykernel install --user --name py36 --display-name "py36"