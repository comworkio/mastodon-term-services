#!/usr/bin/env bash

source ./ci/compute-env.sh
./ci/env-file.sh

rm -rf ./admin/config.yaml
cp config.yaml ./admin/

docker-compose -f ./admin/docker-compose.yml up ${DOCKER_BUILD_OPT} --force-recreate update-ban
