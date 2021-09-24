FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-alpine3.14
ENV DOCKER_VERNEMQ_ALLOW_ANONYMOUS=on
ENV DOCKER_VERNEMQ_ACCEPT_EULA=yes
RUN apk add --no-cache py3-pip
RUN python3 -m pip install aioredis paho-mqtt fastapi-mqtt
EXPOSE 80
COPY . ./api
WORKDIR /api
CMD uvicorn mainapi:app --host 0.0.0.0 --port 80