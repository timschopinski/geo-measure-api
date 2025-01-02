#!/usr/bin/env bash

docker compose run -w /app --rm django python backend/manage.py shell_plus
