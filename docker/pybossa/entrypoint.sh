#!/usr/bin/env bash
set -e

# set env vars in static config files
envsubst < /app/pybossa/alembic.ini.template > /app/pybossa/alembic.ini

# check whether postgres db is already populated with pybossa tables and set corresponding env var
if [ $(psql --tuples-only "${POSTGRES_URL}" <<-EOSQL
    SELECT EXISTS(
    SELECT FROM 
        information_schema.tables
    WHERE 
        table_schema = 'public' AND 
        table_type = 'BASE TABLE');
EOSQL
) = "f" ] ; then
    DB_EXISTS=false
fi

# populate postgres database with pybossa tables if not existent
if [ "${DB_EXISTS}" = false ] ; then
    echo "Postgres database population needed!"
    echo "Initialization of postgres database..."
    python /app/pybossa/cli.py db_create
    echo "...done"
else 
    echo "Postgres database already populated with pybossa tables!"
    echo "-> no database initalization needed."
fi

# migrate to new database layout (if applicable)
alembic upgrade head

# This will exec the CMD from Dockerfile
exec "$@"