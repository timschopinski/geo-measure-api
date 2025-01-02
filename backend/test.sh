#!/usr/bin/env bash

if [ "${DOCKER}" == "yes" ]; then
    PYTHONDONTWRITEBYTECODE=1 python $(dirname "$0")/manage.py test --settings=config.settings.test $*
else
    cd $(dirname "${BASH_SOURCE[0]}")
    PROJECT_DIR=$(git rev-parse --show-toplevel)
    cd $PROJECT_DIR

    docker compose run -w /app --rm django /bin/bash -c "./backend/test.sh $*"

fi
