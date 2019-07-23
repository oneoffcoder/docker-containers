FROM vangjee/rpi-base
LABEL Thanos "vangjee@gmail.com"
RUN apt-get update -y 
RUN apt-get upgrade -y
RUN wget -q http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh -O /tmp/miniconda.sh
RUN /bin/bash /tmp/miniconda.sh -b -p /usr/local/miniconda
RUN echo "PATH=/usr/local/miniconda/bin:$PATH" >> /root/.bashrc
RUN /usr/local/miniconda/bin/conda config --add channels rpi
RUN /usr/local/miniconda/bin/conda install python=3.5 -y
RUN /usr/local/miniconda/bin/conda install python=3.6 -y