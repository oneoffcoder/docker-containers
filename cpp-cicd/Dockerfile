FROM ubuntu:latest

ENV NJOBS=8
ENV CONDA_HOME=/root/anaconda3
ENV PATH=${CONDA_HOME}/bin:${PATH}

ARG TARGETPLATFORM
ARG BUILDPLATFORM

# ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get -y install \
        build-essential \
        cmake \
        libboost-all-dev \
        gcc \
        clang \
        gdb \
        libblkid-dev \
        e2fslibs-dev \
        libaudit-dev \
        valgrind \
        ninja-build \
        doxygen \
        graphviz \
        mscgen \
        dia \
        lcov \
        wget

# anaconda
COPY scripts/download-conda.sh /tmp/download-conda.sh
RUN chmod +x /tmp/download-conda.sh \
    && /bin/bash /tmp/download-conda.sh \
    && /bin/bash /tmp/anaconda.sh -b -p $CONDA_HOME \
    && conda update conda -y \
    && conda update --all -y \
    && conda install -y sphinx sphinx_rtd_theme breathe -c conda-forge \
    && pip install sphinx-sitemap

RUN mkdir /project
WORKDIR /project
VOLUME [ "/project" ]

COPY scripts/build-project.sh /build/build-project.sh
RUN chmod +x /build/build-project.sh

RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD [ "/build/build-project.sh" ]