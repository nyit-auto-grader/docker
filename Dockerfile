FROM python:3.6.4-slim

USER root
WORKDIR /root

RUN apt-get update
RUN apt-get install -y git-core

COPY requirements.txt .
COPY process process

RUN pip install -U pip setuptools
RUN pip install -r requirements.txt

CMD ["python", "process"]
