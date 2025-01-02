#!/bin/bash
set -e


PROJECT_DIR=$(git rev-parse --show-toplevel)
ROOT=$(basename "${PROJECT_DIR}")
ROOT=$(echo "$ROOT" | tr '[:upper:]' '[:lower:]')

running_containers=$(docker ps -f name=${ROOT}_* -aq)
if [[ $running_containers ]]; then
    echo "Stopping running containers..."
    docker stop $running_containers
fi


while [[ $# -gt 0 ]]
do
    key="$1"
    case $key in
        -r|--remove_db_volume)
        remove_db_volume=true
        shift
        ;;
        -f|--force)
        force=true
        shift
        ;;
        -n|--no-fixtures)
        no_fixtures=true
        shift
        ;;
        *)
        shift
        ;;
    esac
done

echo "This will delete your current database (your entire data) and create new one using fixtures."

if [ "${force}" != "true" ]; then
    read -r -p "Are you sure? [y/N] " response

    if ! [[ "$response" =~ ^([yY][eE][sS]|[yY])+$ ]]
    then
        exit 1
    fi
fi

echo "Removing unused containers (this may take a while)..."
docker container prune --force

echo "Removing docker volumes..."
volumes="${ROOT}_postgres_data ${ROOT}_media"

docker volume rm -f ${volumes}

sleep 5

if [ "${no_fixtures}" = true ]; then
    echo "Done recreating db with no fixtures"
    exit
fi

echo "Executing migrations..."

backend/run.sh makemigrations
backend/run.sh migrate

echo "Loading fixtures..."

./backend/run.sh load_fixtures

echo "Reset script completed successfully."
