#!/bin/bash

updateAptPackages() {
    echo "installing packages via APT"
    apt-get update -y
    apt-get upgrade -y
    apt-get install git libopencv-dev wget -y
}

installAnaconda() {
    echo "installing anaconda"
    CONDA_HOME=/opt/anaconda
    CONDA=$CONDA_HOME/bin/conda
    
    wget -q https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh -O /tmp/anaconda.sh
    /bin/bash /tmp/anaconda.sh -b -p $CONDA_HOME
    $CONDA install -c menpo opencv -y
    echo "CONDA_HOME=${CONDA_HOME}" >> /root/.bashrc
    echo "export PATH=\${CONDA_HOME}/bin:\${PATH}" >> /root/.bashrc
    rm -fr /tmp/anaconda.sh
} 

installDarknet() {
    echo "installing darknet"
    DARKNET_HOME=/darknet
    # git clone https://github.com/pjreddie/darknet.git $DARKNET_HOME
    git clone https://github.com/AlexeyAB/darknet.git $DARKNET_HOME
    sed -i 's/GPU=0/GPU=1/g' $DARKNET_HOME/Makefile
    sed -i 's/OPENCV=0/OPENCV=1/g' $DARKNET_HOME/Makefile
    sed -i 's/CUDNN=0/CUDNN=1/g' $DARKNET_HOME/Makefile
    cd $DARKNET_HOME
    make -j 4
    mkdir $DARKNET_HOME/weight
    mkdir $DARKNET_HOME/video
    mkdir $DARKNET_HOME/image
    mkdir $DARKNET_HOME/log
    mkdir $DARKNET_HOME/backup
    wget -q https://pjreddie.com/media/files/yolov3-tiny.weights -O $DARKNET_HOME/weight/yolov3-tiny.weights
    wget -q https://pjreddie.com/media/files/yolov3.weights -O $DARKNET_HOME/weight/yolov3.weights
    echo "DARKNET_HOME=${DARKNET_HOME}" >> /root/.bashrc
    echo "export PATH=\${DARKNET_HOME}:\${PATH}" >> /root/.bashrc
}

updateAptPackages
installAnaconda
installDarknet
