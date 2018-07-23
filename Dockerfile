FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y python
RUN apt-get install -y python-pip
RUN apt-get install -y python-dev
RUN apt-get clean all

COPY requirements.txt /tmp/requirements.txt
COPY src /app
COPY run.sh /app/run.sh
WORKDIR /app

RUN pip install -r /tmp/requirements.txt
RUN rm /tmp/requirements.txt

EXPOSE 1337
ENTRYPOINT ["./run.sh"]
