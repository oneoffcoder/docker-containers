FROM ubuntu:latest
LABEL One-Off Coder "info@oneoffcoder.com"
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
CMD [ "--version" ]]