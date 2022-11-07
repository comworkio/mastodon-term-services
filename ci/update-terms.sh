#!/usr/bin/env bash

source ./ci/compute-env.sh
./ci/env-file.sh

cp config.yaml ./admin/

docker-compose -f ./admin/docker-compose.yml up ${DOCKER_BUILD_OPT} --force-recreate update-terms
