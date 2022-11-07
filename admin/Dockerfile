FROM python:3-alpine

ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    LOG_LEVEL=INFO \
    TERMS_FILE_PATH=/app/terms.html

COPY . /app/

WORKDIR /app

RUN apk add --no-cache libpq-dev && \
    pip3 install --upgrade pip && \
    pip3 install -r requirements.txt
