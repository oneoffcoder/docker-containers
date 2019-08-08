FROM nvidia/cuda:10.0-cudnn7-devel
LABEL One-Off Coder "info@oneoffcoder.com"
ENV DEBIAN_FRONTEND=noninteractive
ENV CONDA_HOME="/opt/anaconda"
ENV PATH="${CONDA_HOME}/bin:${PATH}"
COPY setup.sh /tmp/setup.sh
RUN /tmp/setup.sh
RUN rm -f /tmp/setup.sh
RUN COPY scripts /scripts
RUN mkdir /data
RUN mkdir /model
VOLUME ["/data", "/model"]