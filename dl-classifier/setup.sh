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
        -c pytorch \
        scikit-learn=0.21.1 pytorch torchvision cudatoolkit=10.0
}

downloadModels() {
    echo "downloading models"
    declare -a models=("resnet18" "resnet34" "resnet50" "resnet101" "resnet152" "alexnet" "vgg11" "vgg11_bn" "vgg13" "vgg13_bn" "vgg16" "vgg16_bn" "vgg19" "vgg19_bn" "squeezenet1_0" "squeezenet1_1" "densenet121" "densenet161" "densenet169" "densenet201" "googlenet" "shufflenet_v2_x0_5" "shufflenet_v2_x1_0" "mobilenet_v2" "resnext50_32x4d" "resnext101_32x8d" "wide_resnet50_2" "wide_resnet101_2" "mnasnet0_5" "mnasnet1_0" "inception_v3")

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