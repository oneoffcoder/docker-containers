FROM nvidia/cuda:10.0-cudnn7-devel
LABEL Thanos "vangjee@gmail.com"
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install wget supervisor -y
RUN wget -q https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh -O /tmp/conda.sh
RUN bash /tmp/conda.sh -b
RUN echo "export PATH=/root/anaconda3/bin:${PATH}" >> /root/.bashrc
COPY requirements.txt /tmp/requirements.txt
RUN /root/anaconda3/bin/pip install -r /tmp/requirements.txt
COPY supervisord.conf /etc/supervisor/supervisord.conf
RUN mkdir /ipynb
EXPOSE 8888
VOLUME ["/ipynb"]
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]