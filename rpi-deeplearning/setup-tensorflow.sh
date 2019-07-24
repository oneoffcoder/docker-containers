#!/bin/bash

wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh -O /tmp/miniconda.sh

/bin/bash /tmp/miniconda.sh -b -p /home/pi/miniconda

echo "PATH=/home/pi/miniconda/bin:${PATH}" >> /home/pi/.bashrc

conda update -n root conda -y
conda update --all -y
pip install --upgrade pip
conda config --add channels rpi
conda install python=3.6 -y

git clone https://github.com/tensorflow/tensorflow.git /home/pi/git/tensorflow

cd /home/pi/git/tensorflow

git checkout r1.14

CI_DOCKER_EXTRA_PARAMS="-e CI_BUILD_PYTHON=python3 -e CROSSTOOL_PYTHON_INCLUDE_PATH=/home/pi/miniconda/include/python3.6m/" \
    tensorflow/tools/ci_build/ci_build.sh PI-PYTHON3 \
    tensorflow/tools/ci_build/pi/build_raspberry_pi.sh