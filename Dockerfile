FROM python:3.12.1-alpine3.18
LABEL maintainer="Koalixious"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /temp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    adduser \
    --disabled-password \
    --no-create-home \
    django-user

ENV PATH="/venv/bin:$PATH"

USER django-user