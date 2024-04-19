# syntax=docker/dockerfile:experimental

# Copyright (C) Iktos - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential


FROM python:3.9.19-slim-bullseye as builder-step-1

WORKDIR /app

ENV PIPENV_VENV_IN_PROJECT 1
ENV TZ=UTC

ADD . .

RUN pip install --upgrade pip poetry==1.3.2

RUN apt-get update \
    && apt-get install -y build-essential dumb-init \
    && apt-get -qq -y autoremove \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /var/log/dpkg.log

RUN poetry config --local virtualenvs.in-project true \
     && poetry install --no-dev -vvv \
     && echo 'include-system-site-packages = true' >> .venv/pyvenv.cfg

CMD ["dumb-init", "poetry", "run", "task", "run"]