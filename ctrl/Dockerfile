FROM python:3.9-alpine3.14
RUN apk add --no-cache py3-pip
RUN python3 -m pip install aioredis paho-mqtt
COPY . /ctrl
WORKDIR /ctrl
CMD python3 main.py