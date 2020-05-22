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