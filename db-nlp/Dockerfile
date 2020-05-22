FROM databricksruntime/standard:latest
LABEL org="One-Off Coder"
LABEL author="Jee Vang, Ph.D."
LABEL email="info@oneoffcoder.com"
LABEL website="https://www.oneoffcoder.com"
LABEL facebook="https://www.facebook.com/oneoffcoder"
LABEL twitter="https://twitter.com/oneoffcoder"
LABEL instagram="https://www.instagram.com/oneoffcoder/"
LABEL youtube="https://www.youtube.com/channel/UCCCv8Glpb2dq2mhUj5mcHCQ"
LABEL linkedin="https://www.linkedin.com/company/one-off-coder"

RUN apt-get update \
    && apt-get install -y \
        build-essential \
        python3-dev \
    && apt-get clean

RUN /databricks/conda/bin/conda update -n base -c defaults conda
COPY environment.yml /tmp/environment.yml
RUN /databricks/conda/bin/conda env update --file /tmp/environment.yml
RUN /databricks/conda/envs/dcs-minimal/bin/python -m spacy download en_core_web_lg \
    && /databricks/conda/envs/dcs-minimal/bin/python -m nltk.downloader all

RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*