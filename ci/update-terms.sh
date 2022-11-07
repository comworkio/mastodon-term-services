#!/usr/bin/env bash

source ./ci/compute-env.sh

ENV_FILE="mastodon-terms.env"

echo "${LOG_LEVEL}" > "${ENV_FILE}"
echo "${DB_HOST}" >> "${ENV_FILE}"
echo "${DB_PORT}" >> "${ENV_FILE}"
echo "${DB_NAME}" >> "${ENV_FILE}"
echo "${DB_USER}" >> "${ENV_FILE}"
echo "${DB_PASSWORD}" >> "${ENV_FILE}"

docker-compose up update-tems -d --build --force-recreate