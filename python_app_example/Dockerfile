FROM python:3.12-slim

WORKDIR /app

COPY api/ /app/

RUN  apt-get update \
    && apt-get install gcc -y \
    && apt-get clean \
    && pip install -r /app/requirements.txt \
    && rm -rf /root/.cache/pip

CMD [ "uvicorn", "application:app", "--host", "0.0.0.0", "--port", "8123", "--workers", "1" ]
