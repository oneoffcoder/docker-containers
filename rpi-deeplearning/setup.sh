#!/bin/bash

echo "update environment"
/root/miniconda/bin/conda env update -f /tmp/environment.yml
/root/miniconda/envs/py36/bin/pip install --upgrade pip
/root/miniconda/envs/py36/bin/pip install -vvv /tmp/output-artifacts/tensorflow-1.14.1-cp36-none-linux_armv7l.whl