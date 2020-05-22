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

# update ubuntu
RUN apt-get update \
    && apt-get install -y \
        build-essential \
        python3-dev \
    && apt-get clean

# update conda
RUN /databricks/conda/bin/conda update -n base -c defaults conda
COPY environment.yml /tmp/environment.yml
RUN /databricks/conda/bin/conda env update --file /tmp/environment.yml

# install maven
RUN wget -q http://mirror.metrocast.net/apache/maven/maven-3/3.6.1/binaries/apache-maven-3.6.1-bin.tar.gz -O /tmp/maven.tar.gz \
    && tar xvfz /tmp/maven.tar.gz -C /opt \
    && ln -s /opt/apache-maven-3.6.1 /opt/maven

# install jars
COPY pom.xml /tmp/pom.xml
RUN cd /tmp \
    && /opt/maven/bin/mvn dependency:copy-dependencies -DoutputDirectory=/databricks/jars

# clean up
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*