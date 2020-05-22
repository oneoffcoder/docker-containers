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
COPY setup.sh /tmp/setup.sh
RUN /tmp/setup.sh
RUN rm -f /tmp/setup.sh
EXPOSE 8888 8070 8090
VOLUME ["/darknet/cfg", "/darknet/data", "/darknet/weight", "/darknet/video", "/darknet/image", "/darknet/log", "/darknet/backup", "/root/scripts"]
WORKDIR /darknet
ENTRYPOINT [ "./darknet" ]
CMD [ "" ]