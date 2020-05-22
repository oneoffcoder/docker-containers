FROM oneoffcoder/rpi-nlp
LABEL org="One-Off Coder"
LABEL author="Jee Vang, Ph.D."
LABEL email="info@oneoffcoder.com"
LABEL website="https://www.oneoffcoder.com"
LABEL facebook="https://www.facebook.com/oneoffcoder"
LABEL twitter="https://twitter.com/oneoffcoder"
LABEL instagram="https://www.instagram.com/oneoffcoder/"
LABEL youtube="https://www.youtube.com/channel/UCCCv8Glpb2dq2mhUj5mcHCQ"
LABEL linkedin="https://www.linkedin.com/company/one-off-coder"

COPY environment.yml /tmp/environment.yml
COPY setup.sh /tmp/setup.sh
COPY output-artifacts/ /tmp/output-artifacts
RUN /tmp/setup.sh
RUN rm -f /tmp/setup.sh
RUN rm -f /tmp/environment.yml
RUN rm -fr /tmp/output-artifacts