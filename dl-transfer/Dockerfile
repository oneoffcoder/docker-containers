FROM nvidia/cuda:10.0-cudnn7-devel

LABEL organization="One-Off Coder"
LABEL email="info@oneoffcoder.com"

ENV DEBIAN_FRONTEND=noninteractive
ENV CONDA_HOME="/opt/anaconda"
ENV PATH="${CONDA_HOME}/bin:${PATH}"

# setup environment
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install wget -y

# setup conda
RUN wget -q https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh -O /tmp/anaconda.sh \
    && /bin/bash /tmp/anaconda.sh -b -p $CONDA_HOME \
    && conda install --yes -c pytorch pytorch torchvision cudatoolkit=10.0 \
    && python -c "from torchvision import models; models.vgg19(pretrained=True)"

# setup app
COPY . /app
VOLUME [ "/app/images" ]
WORKDIR /app
ENTRYPOINT [ "python", "app.py" ]
CMD [ "--help" ]

# clean up
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*