#!/bin/bash

BASE_DIR=/root/miniconda/bin
CONDA=$BASE_DIR/conda
PIP=$BASE_DIR/pip
JUPYTER=$BASE_DIR/jupyter
PYTHON=$BASE_DIR/python

echo "update conda"
$CONDA update -n root conda -y

echo "create new environment"
$CONDA env create -f /tmp/environment.yml --quiet

echo "setting up ~/.bashrc"
echo "source /root/miniconda/bin/activate py36" >> ~/.bashrc
echo "PATH=/root/miniconda/envs/py36/bin:$PATH" >> ~/.bashrc