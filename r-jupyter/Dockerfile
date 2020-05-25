FROM ubuntu:eoan
LABEL org="One-Off Coder"
LABEL author="Jee Vang, Ph.D."
LABEL email="info@oneoffcoder.com"
LABEL website="https://www.oneoffcoder.com"
LABEL facebook="https://www.facebook.com/oneoffcoder"
LABEL twitter="https://twitter.com/oneoffcoder"
LABEL instagram="https://www.instagram.com/oneoffcoder/"
LABEL youtube="https://www.youtube.com/channel/UCCCv8Glpb2dq2mhUj5mcHCQ"
LABEL linkedin="https://www.linkedin.com/company/one-off-coder"

ENV CONDA_HOME=/usr/local/conda
ENV PATH=${CONDA_HOME}/bin:${PATH}
ENV DEBIAN_FRONTEND=noninteractive
ENV NOTEBOOK_PASSWORD=""

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get -y install wget nano supervisor unzip gnupg2 software-properties-common

# setup r
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9 \
    && add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu eoan-cran35/' \
    && apt-get update -y \
    && apt-get -y install r-base

# setup conda
RUN wget -q https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh -O /tmp/anaconda.sh \
    && /bin/bash /tmp/anaconda.sh -b -p $CONDA_HOME \
    && $CONDA_HOME/bin/conda update -n root conda -y
COPY ubuntu/root/.jupyter /root/.jupyter/

# install r kernel
RUN Rscript -e "install.packages('IRkernel', repos='https://mirrors.nics.utk.edu/cran/')" \
       -e "IRkernel::installspec(name = 'ir36', displayname = 'R 3.6')"

# setup volumes
RUN mkdir /root/ipynb \
    && mkdir /root/libs
VOLUME [ "/root/ipynb" ]
VOLUME [ "/root/libs" ]

# setup supervisor
COPY ubuntu/etc/supervisor/supervisor.conf /etc/supervisor/supervisor.conf
COPY ubuntu/etc/supervisor/conf.d/all.conf /etc/supervisor/conf.d/all.conf

# clean up
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && apt-get clean

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]