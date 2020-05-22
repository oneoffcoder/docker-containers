FROM ubuntu:19.10
LABEL org="One-Off Coder"
LABEL author="Jee Vang, Ph.D."
LABEL website="https://www.oneoffcoder.com"
LABEL email="info@oneoffcoder.com"
LABEL facebook="https://www.facebook.com/oneoffcoder"
LABEL twitter="https://twitter.com/oneoffcoder"
LABEL instagram="https://www.instagram.com/oneoffcoder/"
LABEL youtube="https://www.youtube.com/channel/UCCCv8Glpb2dq2mhUj5mcHCQ"
LABEL linkedin="https://www.linkedin.com/company/one-off-code"

ENV NJOBS=8

RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get -y install build-essential cmake libboost-all-dev gcc clang gdb libblkid-dev e2fslibs-dev libaudit-dev valgrind ninja-build doxygen graphviz mscgen dia lcov

RUN mkdir /project
WORKDIR /project
VOLUME [ "/project" ]

COPY scripts/build-project.sh /build/build-project.sh
RUN chmod +x /build/build-project.sh

RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD [ "/build/build-project.sh" ]