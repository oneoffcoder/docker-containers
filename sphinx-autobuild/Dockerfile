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

ENV CONDA_HOME=/usr/local/conda
ENV PATH=${CONDA_HOME}/bin:${PATH}
ENV DEBIAN_FRONTEND=noninteractive
ENV AUTOBUILD_PORT=8000
ENV AUTOBUILD_HOST=0.0.0.0

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get -y install wget supervisor nano build-essential

# setup conda
RUN wget -q https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh -O /tmp/anaconda.sh \
    && /bin/bash /tmp/anaconda.sh -b -p $CONDA_HOME \
    && $CONDA_HOME/bin/conda update -n root conda -y \
    && pip install \
        sphinx \
        sphinx_rtd_theme \
        sphinxcontrib-bibtex \
        sphinx-autobuild \
        sphinxcontrib-blockdiag \
        sphinx-sitemap \
        jupyter-sphinx \
        nbsphinx \
    && conda install -c conda-forge pandoc ipython

# setup volumes
RUN mkdir /sphinx
VOLUME [ "/sphinx" ]

# setup supervisor
ADD ubuntu/usr/local/sbin /usr/local/sbin/
ADD ubuntu/etc/supervisor/conf.d /etc/supervisor/conf.d/

# clean up
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && apt-get clean

# expose port
EXPOSE 8000

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]