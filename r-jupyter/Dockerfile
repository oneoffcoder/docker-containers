FROM ubuntu:latest
LABEL org="One-Off Coder"
LABEL author="Jee Vang, Ph.D."
LABEL email="info@oneoffcoder.com"
LABEL website="https://www.oneoffcoder.com"
LABEL facebook="https://www.facebook.com/oneoffcoder"
LABEL twitter="https://twitter.com/oneoffcoder"
LABEL instagram="https://www.instagram.com/oneoffcoder/"
LABEL youtube="https://www.youtube.com/channel/UCCCv8Glpb2dq2mhUj5mcHCQ"
LABEL linkedin="https://www.linkedin.com/company/one-off-coder"

ENV NODE_HOME=/usr/local/node-v14.15.1-linux-x64
ENV CONDA_HOME=/usr/local/conda
ENV PATH=${NODE_HOME}/bin:${CONDA_HOME}/bin:${PATH}
ENV DEBIAN_FRONTEND=noninteractive
ENV NOTEBOOK_PASSWORD=""

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install wget nano supervisor unzip gnupg2 software-properties-common dirmngr apt-transport-https ca-certificates build-essential

# setup r
# https://linuxize.com/post/how-to-install-r-on-ubuntu-20-04/
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9 \
    && add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/' \
    && apt-get update -y \
    && apt-get -y install r-base

# setup nodejs
RUN wget -q https://nodejs.org/dist/v14.15.1/node-v14.15.1-linux-x64.tar.xz -O /tmp/node.tar.xz \
    && tar xf /tmp/node.tar.xz -C /usr/local \
    && node --version \
    && npm --version

# setup conda
RUN wget -q https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh -O /tmp/anaconda.sh \
    && /bin/bash /tmp/anaconda.sh -b -p $CONDA_HOME \
    && conda update --all \
    && conda update -c conda-forge jupyterlab \
    && conda install -c conda-forge nodejs \
    && pip install jupyterlab-commenting-service \
    && jupyter labextension install @jupyter-widgets/jupyterlab-manager @jupyterlab/commenting-extension @jupyterlab/toc @krassowski/jupyterlab-lsp \
    && conda install -c conda-forge python-language-server r-languageserver
COPY ubuntu/root/.jupyter /root/.jupyter/

# install r kernel
RUN Rscript \
    -e "repos <- 'https://cloud.r-project.org/'" \
    -e "dependencies <- c('Depends', 'Imports', 'LinkingTo', 'Suggests', 'Enhances')" \
    -e "install.packages('IRkernel', repos=repos, Ncpus=10, dependencies=dependencies)" \
    -e "IRkernel::installspec()"

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