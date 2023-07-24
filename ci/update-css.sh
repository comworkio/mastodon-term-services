#!/usr/bin/env bash

source ./ci/compute-env.sh
./ci/env-file.sh

rm -rf ./admin/custom.css
cp custom.css ./admin/

docker-compose -f ./admin/docker-compose.yml up ${DOCKER_BUILD_OPT} --force-recreate update-css
