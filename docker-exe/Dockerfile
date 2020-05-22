FROM ubuntu:latest
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
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install software-properties-common -y \
    && add-apt-repository ppa:deadsnakes/ppa -y \
    && apt-get update -y \
    && apt-get install python3.7 -y \
    && ln -s /usr/bin/python3.7 /usr/bin/python
RUN mkdir /app
COPY main.py /app
ENTRYPOINT [ "python", "/app/main.py" ]
CMD [ "--version" ]