FROM ubuntu:disco
LABEL One-Off Coder "info@oneoffcoder.com"

ENV CONDA_HOME=/usr/local/conda
ENV PATH=${CONDA_HOME}/bin:${PATH}

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get -y install openjdk-12-jdk wget nano supervisor \
    && apt-get clean

# setup conda
RUN wget -q https://repo.anaconda.com/archive/Anaconda3-2019.07-Linux-x86_64.sh -O /tmp/Anaconda3-2019.07-Linux-x86_64.sh \
    && /bin/bash /tmp/Anaconda3-2019.07-Linux-x86_64.sh -b -p $CONDA_HOME \
    && $CONDA_HOME/bin/conda update -n root conda -y \
    && wget -q https://github.com/SpencerPark/IJava/releases/download/v1.3.0/ijava-1.3.0.zip -O /tmp/ijava-1.3.0.zip

# setup volumes
RUN mkdir /root/ipynb
VOLUME [ "/root/ipynb" ]

# clean up
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*