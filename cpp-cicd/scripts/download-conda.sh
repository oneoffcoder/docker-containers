#!/bin/bash
if [ $TARGETPLATFORM == "linux/arm64" ]
then
    echo "downloading anaconda for linux/arm64"
    wget -q https://repo.anaconda.com/archive/Anaconda3-2023.03-1-Linux-aarch64.sh -O /tmp/anaconda.sh
else
    echo "downloading anaconda for linux/amd64"
    wget -q https://repo.anaconda.com/archive/Anaconda3-2023.03-1-Linux-x86_64.sh -O /tmp/anaconda.sh
fi