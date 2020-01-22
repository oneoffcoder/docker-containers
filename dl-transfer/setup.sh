#!/bin/bash

updateAptPackages() {
    echo "installing packages via APT"
    apt-get update -y
    apt-get upgrade -y
    apt-get install wget -y
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
        -c pytorch pytorch torchvision cudatoolkit=10.0
}

downloadModels() {
    echo "downloading models"
    declare -a models=("vgg19")

    for model in ${models[@]}; do
        package="from torchvision import models; models.${model}(pretrained=True)"
        echo $package
        python -c "$package"
    done
}

updateAptPackages
installAnaconda
installPytorch
downloadModels