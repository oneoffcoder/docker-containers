FROM ubuntu:disco
LABEL org="One-Off Coder"
LABEL author="Jee Vang, Ph.D."
LABEL email="info@oneoffcoder.com"
LABEL website="https://www.oneoffcoder.com"
LABEL facebook="https://www.facebook.com/oneoffcoder"
LABEL twitter="https://twitter.com/oneoffcoder"
LABEL instagram="https://www.instagram.com/oneoffcoder/"
LABEL youtube="https://www.youtube.com/channel/UCCCv8Glpb2dq2mhUj5mcHCQ"
LABEL linkedin="https://www.linkedin.com/company/one-off-coder"

ENV IJAVA_COMPILER_OPTS="--source 12 --enable-preview"
ENV IJAVA_CLASSPATH="/root/libs/"
ENV CONDA_HOME=/usr/local/conda
ENV PATH=${CONDA_HOME}/bin:${PATH}

# setup ubuntu
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get -y install openjdk-12-jdk wget nano supervisor unzip \
    && apt-get clean

# setup conda
RUN wget -q https://repo.anaconda.com/archive/Anaconda3-2019.07-Linux-x86_64.sh -O /tmp/Anaconda3-2019.07-Linux-x86_64.sh \
    && /bin/bash /tmp/Anaconda3-2019.07-Linux-x86_64.sh -b -p $CONDA_HOME \
    && $CONDA_HOME/bin/conda update -n root conda -y \
    && wget -q https://github.com/SpencerPark/IJava/releases/download/v1.3.0/ijava-1.3.0.zip -O /tmp/ijava-1.3.0.zip \
    && unzip /tmp/ijava-1.3.0.zip -d /tmp/ijava \
    && python /tmp/ijava/install.py --sys-prefix
COPY ubuntu/root/.jupyter /root/
COPY ubuntu/usr/local/conda/share/jupyter/kernels/java/kernel.json /usr/local/conda/share/jupyter/kernels/java/kernel.json

# setup volumes
RUN mkdir /root/ipynb \
    && mkdir /root/libs
VOLUME [ "/root/ipynb" ]
VOLUME [ "/root/libs" ]

# setup supervisor
COPY ubuntu/etc/supervisor/supervisor.conf /etc/supervisor/supervisor.conf
COPY ubuntu/etc/supervisor/conf.d/all.conf /etc/supervisor/conf.d/all.conf

# clean up
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]