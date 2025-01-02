#!/usr/bin/env bash
set -e

if [ "${DOCKER}" == "yes" ]; then
    COVERAGE_DIR="$(dirname "$0")"

    echo "Running tests with coverage..."
    coverage run "${COVERAGE_DIR}/manage.py" test --settings=config.settings.test "$@" \
    && coverage report -m \
    && coverage html -d "${COVERAGE_DIR}/htmlcov"
else
    cd "$(dirname "${BASH_SOURCE[0]}")"
    PROJECT_DIR=$(git rev-parse --show-toplevel)
    cd "${PROJECT_DIR}"
    docker compose run -w /app --rm django /bin/bash -c "./backend/coverage.sh $*"
    [ $? -eq 0 ] && echo "See htmlcov/index.html in your browser." || echo "Failed to run coverage - check that all tests have passed."
fi
