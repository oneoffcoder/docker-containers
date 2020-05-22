FROM nvidia/cuda:10.0-cudnn7-devel
LABEL org="One-Off Coder"
LABEL author="Jee Vang, Ph.D."
LABEL email="info@oneoffcoder.com"
LABEL website="https://www.oneoffcoder.com"
LABEL facebook="https://www.facebook.com/oneoffcoder"
LABEL twitter="https://twitter.com/oneoffcoder"
LABEL instagram="https://www.instagram.com/oneoffcoder/"
LABEL youtube="https://www.youtube.com/channel/UCCCv8Glpb2dq2mhUj5mcHCQ"
LABEL linkedin="https://www.linkedin.com/company/one-off-coder"

ENV CONDA_HOME=/root/anaconda3
ENV PATH=${CONDA_HOME}/bin:${PATH}
ENV NOTEBOOK_PASSWORD=""

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install wget supervisor -y \
    && apt-get clean

COPY requirements.txt /tmp/requirements.txt
RUN wget -q https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh -O /tmp/anaconda.sh \
    && /bin/bash /tmp/anaconda.sh -b -p $CONDA_HOME \
    && /root/anaconda3/bin/pip install -r /tmp/requirements.txt \
    && /root/anaconda3/bin/python -m spacy download en_core_web_lg

RUN mkdir /root/ipynb \
    && mkdir /root/tensorboard
VOLUME ["/root/ipynb", "/root/tensorboard"]

RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY supervisord.conf /etc/supervisor/supervisord.conf
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]