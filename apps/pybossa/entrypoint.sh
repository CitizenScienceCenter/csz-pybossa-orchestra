#!/usr/bin/env bash
set -e

# set env vars in static config files
envsubst < /app/pybossa/alembic.ini.template > /app/pybossa/alembic.ini

# This will exec the CMD from Dockerfile
exec "$@"