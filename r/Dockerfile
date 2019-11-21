FROM ubuntu:disco
LABEL One-Off Coder "info@oneoffcoder.com"

ENV CONDA_HOME=/usr/local/conda
ENV PATH=${CONDA_HOME}/bin:${PATH}
ENV DEBIAN_FRONTEND=noninteractive

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get -y install wget nano supervisor unzip gnupg2 software-properties-common

# setup r
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9 \
    && add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu disco-cran35/' \
    && apt-get update -y \
    && apt-get -y install r-base

# setup conda
RUN wget -q https://repo.anaconda.com/archive/Anaconda3-2019.07-Linux-x86_64.sh -O /tmp/Anaconda3-2019.07-Linux-x86_64.sh \
    && /bin/bash /tmp/Anaconda3-2019.07-Linux-x86_64.sh -b -p $CONDA_HOME \
    && $CONDA_HOME/bin/conda update -n root conda -y

# install r kernel
RUN Rscript -e "install.packages('IRkernel', repos='https://mirrors.nics.utk.edu/cran/')" \
       -e "IRkernel::installspec(name = 'ir36', displayname = 'R 3.6')"

# setup volumes
RUN mkdir /root/ipynb \
    && mkdir /root/libs
VOLUME [ "/root/ipynb" ]
VOLUME [ "/root/libs" ]

# clean up
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && apt-get clean
