FROM ubuntu:19.10

LABEL org="One-Off Coder"
LABEL email="info@oneoffcoder.com"

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get -y install build-essential cmake libboost-all-dev

RUN mkdir /project
WORKDIR /project
VOLUME [ "/project" ]

COPY scripts/build-project.sh /build/build-project.sh
RUN chmod +x /build/build-project.sh

RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD [ "/build/build-project.sh" ]