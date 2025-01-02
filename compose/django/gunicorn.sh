#!/bin/sh

set -e

backend/run.sh wait_for_db
backend/run.sh migrate

gunicorn --workers=3 --threads=6 --worker-class=gthread --worker-tmp-dir /dev/shm config.wsgi