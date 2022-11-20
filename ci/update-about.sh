#!/usr/bin/env bash

source ./ci/compute-env.sh
./ci/env-file.sh

rm -rf ./admin/about.md
cp about.md ./admin/

docker-compose -f ./admin/docker-compose.yml up ${DOCKER_BUILD_OPT} --force-recreate update-about
