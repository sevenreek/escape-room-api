FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-alpine3.14
ENV DOCKER_VERNEMQ_ALLOW_ANONYMOUS=on
ENV DOCKER_VERNEMQ_ACCEPT_EULA=yes
RUN apk add --no-cache py3-pip
RUN python3 -m pip install aioredis paho-mqtt
EXPOSE 80
COPY . .
WORKDIR /app
CMD uvicorn app.mainapi:app --host 0.0.0.0 --port 80