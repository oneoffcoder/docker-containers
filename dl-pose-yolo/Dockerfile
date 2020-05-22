FROM nvidia/cuda:10.1-cudnn7-devel
LABEL org="One-Off Coder"
LABEL author="Jee Vang, Ph.D."
LABEL email="info@oneoffcoder.com"
LABEL website="https://www.oneoffcoder.com"
LABEL facebook="https://www.facebook.com/oneoffcoder"
LABEL twitter="https://twitter.com/oneoffcoder"
LABEL instagram="https://www.instagram.com/oneoffcoder/"
LABEL youtube="https://www.youtube.com/channel/UCCCv8Glpb2dq2mhUj5mcHCQ"
LABEL linkedin="https://www.linkedin.com/company/one-off-coder"

ENV DEBIAN_FRONTEND=noninteractive
ENV CONDA_HOME="/opt/anaconda"
ENV PATH="${CONDA_HOME}/bin:${PATH}"

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get -y install wget libgeos-dev libsm6 libxext6 libxrender-dev \
    && apt-get clean

# setup conda
RUN wget -q https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh -O /tmp/anaconda.sh \
    && /bin/bash /tmp/anaconda.sh -b -p $CONDA_HOME \
    && conda update -n root conda -y \
    && conda install pytorch torchvision cudatoolkit=10.1 -c pytorch -y \
    && conda install cython -c anaconda -y \
    && pip install \
        EasyDict==1.7 \
        opencv-python \
        shapely==1.6.4 \
        Cython \
        scipy \
        pandas \
        pyyaml \
        json_tricks \
        scikit-image \
        yacs==0.1.6 \
        tensorboardX==1.6 \
        pycocotools \
        tqdm \
        joblib

# setup yolo
RUN mkdir /yolo \
    && mkdir /yolo/custom
COPY . /yolo

# setup input/output data volume
VOLUME [ "/yolo/custom" ]

# clean up
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# entry point
WORKDIR /yolo
ENTRYPOINT [ "python", "detect-person.py" ]
CMD [ "--help" ]
