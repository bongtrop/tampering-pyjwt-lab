FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y python
RUN apt-get install -y python-pip
RUN apt-get install -y python-dev
RUN apt-get install -y python-gmpy2
RUN apt-get clean all

COPY requirements.txt /tmp/requirements.txt
COPY src /app
WORKDIR /app

RUN pip install -r /tmp/requirements.txt

EXPOSE 1337
ENTRYPOINT ["python"]
CMD ["app.py"]
