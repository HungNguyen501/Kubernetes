FROM python:3.12-slim

COPY requirements.txt /
RUN  apt-get update \
    && apt-get install gcc -y \
    && apt-get clean \
    && pip install -r /requirements.txt \
    && rm -rf /root/.cache/pip

    
COPY app/ /app/
WORKDIR /app
