#!/bin/bash

BASE_DIR=/root/miniconda/bin
CONDA=$BASE_DIR/conda

echo "update environment"
$CONDA env update -f /tmp/environment.yml
