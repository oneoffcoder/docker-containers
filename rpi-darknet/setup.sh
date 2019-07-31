#!/bin/bash

updateAptPackages() {
    echo "installing packages via APT"
    apt-get install git libopencv-dev python3-opencv -y
}

installMiniconda() {
    echo "installing miniconda"
    CONDA=/root/miniconda/bin/conda
    PIP=/root/miniconda/bin/pip

    wget -q http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh -O /tmp/miniconda.sh
    /bin/bash /tmp/miniconda.sh -b -p /root/miniconda
    $CONDA update -n root conda -y
    $CONDA update --all -y
    $CONDA config --add channels rpi
    $CONDA install python=3.6 -y
    $PIP install --upgrade pip
    echo "PATH=/root/miniconda/bin:${PATH}" >> /root/.bashrc
    rm -fr /tmp/miniconda.sh
} 

installDarknet() {
    DARKNET_HOME=/usr/local/darknet
    echo "installing darknet"
    git clone https://github.com/pjreddie/darknet.git $DARKNET_HOME
    sed -i 's/OPENCV=0/OPENCV=1/g' $DARKNET_HOME/Makefile
    cd $DARKNET_HOME
    make -j 4
    echo "PATH=${DARKNET_HOME}:${PATH}" >> /root/.bashrc
}

updateAptPackages
installMiniconda
installDarknet
