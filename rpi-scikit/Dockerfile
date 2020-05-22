FROM oneoffcoder/rpi-jupyterlab
LABEL org="One-Off Coder"
LABEL author="Jee Vang, Ph.D."
LABEL email="info@oneoffcoder.com"
LABEL website="https://www.oneoffcoder.com"
LABEL facebook="https://www.facebook.com/oneoffcoder"
LABEL twitter="https://twitter.com/oneoffcoder"
LABEL instagram="https://www.instagram.com/oneoffcoder/"
LABEL youtube="https://www.youtube.com/channel/UCCCv8Glpb2dq2mhUj5mcHCQ"
LABEL linkedin="https://www.linkedin.com/company/one-off-coder"

RUN apt-get update -y 
RUN apt-get upgrade -y
COPY environment.yml /tmp/environment.yml
COPY setup.sh /tmp/setup.sh
RUN /tmp/setup.sh
RUN rm -f /tmp/setup.sh
RUN rm -f /tmp/environment.yml
