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
COPY setup.sh /tmp/setup.sh
RUN /tmp/setup.sh
RUN rm -f /tmp/setup.sh
COPY scripts /scripts
COPY faces-small /data
RUN mkdir /model
VOLUME [ "/data", "/model" ]
ENTRYPOINT [ "python", "/scripts/pt.py" ]
CMD [ "--help" ]