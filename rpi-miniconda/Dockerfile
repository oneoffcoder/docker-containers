FROM oneoffcoder/rpi-base
LABEL org="One-Off Coder"
LABEL author="Jee Vang, Ph.D."
LABEL email="info@oneoffcoder.com"
LABEL website="https://www.oneoffcoder.com"
LABEL facebook="https://www.facebook.com/oneoffcoder"
LABEL twitter="https://twitter.com/oneoffcoder"
LABEL instagram="https://www.instagram.com/oneoffcoder/"
LABEL youtube="https://www.youtube.com/channel/UCCCv8Glpb2dq2mhUj5mcHCQ"
LABEL linkedin="https://www.linkedin.com/company/one-off-coder"

RUN apt-get update -y 
RUN apt-get upgrade -y
RUN wget -q http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh -O /tmp/miniconda.sh
RUN /bin/bash /tmp/miniconda.sh -b -p /root/miniconda
# RUN echo "PATH=/root/miniconda/bin:${PATH}" >> /root/.bashrc
RUN /root/miniconda/bin/conda update -n root conda -y
RUN /root/miniconda/bin/conda update --all -y
RUN /root/miniconda/bin/pip install --upgrade pip
RUN /root/miniconda/bin/conda config --add channels rpi
RUN /root/miniconda/bin/conda install python=3.6 -y