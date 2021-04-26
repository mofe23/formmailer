# syntax=docker/dockerfile:1.0
FROM python:3.8.6-slim-buster

MAINTAINER Moritz Federspiel <moritz.federspiel@steadysense.at>

# Configure environment
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV LANGUAGE=C.UTF-8

RUN adduser --system formmailer

RUN apt-get update && apt-get upgrade -y

RUN pip install --upgrade pip

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt -t /requ

# Copy Entrypoints
COPY --chmod 0755 ./compose/entrypoint /

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
