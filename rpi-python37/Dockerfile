FROM arm32v7/ubuntu
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
RUN apt-get update -y 
RUN apt-get upgrade -y
RUN apt-get install wget build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev -y
RUN wget -q https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tar.xz -O /tmp/Python-3.7.4.tar.xz
RUN tar xf /tmp/Python-3.7.4.tar.xz -C /tmp
WORKDIR /tmp/Python-3.7.4
RUN ./configure
RUN make -j 4
RUN make altinstall
WORKDIR /
RUN rm -fr /tmp/Python-3.7.4
RUN rm -f /tmp/Python-3.7.4.tar.xz
RUN apt-get --purge remove wget build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev -y
RUN apt-get autoremove -y
RUN apt-get clean