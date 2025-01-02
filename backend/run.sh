#!/usr/bin/env bash

if [ "${DOCKER}" == "yes" ]; then
    python $(dirname "$0")/manage.py "$@"
else
    cd $(dirname "${BASH_SOURCE[0]}")
    PROJECT_DIR=$(git rev-parse --show-toplevel)
    cd $PROJECT_DIR

    docker compose run -w /app --rm django python backend/manage.py "$@"

fi
