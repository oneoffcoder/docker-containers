#!/bin/bash

updateAptPackages() {
    echo "installing packages via APT"
    apt-get install git libopencv-dev python3-opencv -y
}

installMiniconda() {
    echo "installing miniconda"
    CONDA_HOME=/root/miniconda
    CONDA=$CONDA_HOME/bin/conda
    PIP=/root/miniconda/bin/pip

    wget -q http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh -O /tmp/miniconda.sh
    /bin/bash /tmp/miniconda.sh -b -p $CONDA_HOME
    $CONDA update -n root conda -y
    $CONDA update --all -y
    $CONDA config --add channels rpi
    $CONDA install python=3.6 -y
    $PIP install --upgrade pip
    $CONDA install opencv joblib -y
    echo "CONDA_HOME=${CONDA_HOME}" >> /root/.bashrc
    echo "export PATH=\${CONDA_HOME}/bin:\${PATH}" >> /root/.bashrc
    rm -fr /tmp/miniconda.sh
} 

installDarknet() {
    DARKNET_HOME=/darknet
    echo "installing darknet"
    git clone https://github.com/AlexeyAB/darknet.git $DARKNET_HOME
    sed -i 's/OPENCV=0/OPENCV=1/g' $DARKNET_HOME/Makefile
    cd $DARKNET_HOME
    make -j 4
    mkdir $DARKNET_HOME/weight
    mkdir $DARKNET_HOME/video
    mkdir $DARKNET_HOME/image
    mkdir $DARKNET_HOME/log
    wget -q https://pjreddie.com/media/files/yolov3-tiny.weights -O $DARKNET_HOME/weight/yolov3-tiny.weights
    wget -q https://pjreddie.com/media/files/yolov3.weights -O $DARKNET_HOME/weight/yolov3.weights
    echo "DARKNET_HOME=${DARKNET_HOME}" >> /root/.bashrc
    echo "export PATH=\${DARKNET_HOME}:\${PATH}" >> /root/.bashrc
}

setupScripts() {
    mkdir /root/scripts
}

updateAptPackages
installMiniconda
installDarknet
setupScripts