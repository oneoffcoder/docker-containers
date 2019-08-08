#!/bin/bash

updateAptPackages() {
    echo "installing packages via APT"
    apt-get update -y
    apt-get upgrade -y
    apt-get install git libopencv-dev wget -y
}

installAnaconda() {
    echo "installing anaconda"
    wget -q https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh -O /tmp/anaconda.sh
    /bin/bash /tmp/anaconda.sh -b -p $CONDA_HOME
    rm -fr /tmp/anaconda.sh
} 

installPytorch() {
    echo "installing pytorch"
    conda install --yes \
        -c menpo \
        -c pytorch \
        opencv \
        pytorch torchvision cudatoolkit=10.0
}

updateAptPackages
installAnaconda
installPytorch