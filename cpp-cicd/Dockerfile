FROM ubuntu:19.10
LABEL org="One-Off Coder"
LABEL author="Jee Vang, Ph.D."
LABEL email="info@oneoffcoder.com"
LABEL website="https://www.oneoffcoder.com"
LABEL facebook="https://www.facebook.com/oneoffcoder"
LABEL twitter="https://twitter.com/oneoffcoder"
LABEL instagram="https://www.instagram.com/oneoffcoder/"
LABEL youtube="https://www.youtube.com/channel/UCCCv8Glpb2dq2mhUj5mcHCQ"
LABEL linkedin="https://www.linkedin.com/company/one-off-coder"

ENV NJOBS=8
ENV CONDA_HOME=/root/anaconda3
ENV PATH=${CONDA_HOME}/bin:${PATH}

# ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get -y install build-essential cmake libboost-all-dev gcc clang gdb libblkid-dev e2fslibs-dev libaudit-dev valgrind ninja-build doxygen graphviz mscgen dia lcov wget

# anaconda
RUN wget -q https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh -O /tmp/anaconda.sh \
    && /bin/bash /tmp/anaconda.sh -b -p $CONDA_HOME \
    && conda update --all \
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