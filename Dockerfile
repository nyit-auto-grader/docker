FROM python:3.6.4-slim

USER root
WORKDIR /root

COPY requirements.txt .
COPY process process

RUN pip install -r requirements.txt

CMD ["python", "process"]

