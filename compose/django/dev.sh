#!/bin/bash
set -e

backend/run.sh wait_for_db

exec "$@"
