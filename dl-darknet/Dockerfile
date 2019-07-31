FROM nvidia/cuda:10.0-cudnn7-devel
LABEL One-Off Coder "info@oneoffcoder.com"
ENV DEBIAN_FRONTEND=noninteractive
COPY setup.sh /tmp/setup.sh
RUN /tmp/setup.sh
RUN rm -f /tmp/setup.sh
VOLUME ["/darknet/cfg", "/darknet/weight", "/darknet/video", "/darknet/image"]