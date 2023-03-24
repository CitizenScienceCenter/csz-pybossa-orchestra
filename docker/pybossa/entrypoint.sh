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
    if [ "${DB_INIT}" = true ] ; then
        echo "Initialization of postgres database..."
        python /app/pybossa/cli.py db_create
        echo "Initialization completed"
    else
        echo "Postgres database not set to be populated with pybossa tables by this container!"
        echo "-> Set env var DB_INIT=true for this container to trigger population of postgres database"
    fi
else 
    echo "Postgres database already populated with pybossa tables!"
    echo "-> no database initalization needed."
fi

# This will exec the CMD from Dockerfile
exec "$@"