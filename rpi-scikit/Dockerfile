FROM vangjee/rpi-jupyterlab
LABEL Thanos "vangjee@gmail.com"
RUN apt-get update -y 
RUN apt-get upgrade -y
RUN apt-get install build-essential gfortran libopenblas-dev liblapack-dev python-dev default-libmysqlclient-dev libfreetype6-dev libxml2-dev libxslt1-dev -y
COPY requirements.txt /tmp/requirements.txt
RUN pip3.7 install -r /tmp/requirements.txt
RUN rm -f /tmp/requirements.txt
