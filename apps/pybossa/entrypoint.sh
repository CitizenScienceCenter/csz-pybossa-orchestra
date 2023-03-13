#!/usr/bin/env bash
set -e

# set env vars in static config files
envsubst < /app/pybossa/alembic.ini.template > /app/pybossa/alembic.ini

# check whether postgres db is already populated with pybossa tables
DB_EXISTS=$(psql --tuples-only "${POSTGRES_URL}" <<-EOSQL
SELECT EXISTS(
    SELECT FROM 
        information_schema.tables
    WHERE 
        table_schema = 'public' AND 
        table_type = 'BASE TABLE'
    );
EOSQL
)

# populate postgres database with pybossa tables if not existent
if [ "${DB_INIT}" -a "${DB_EXISTS} == 'f'" ] ; then
    echo "Postgres database population needed!"
    python /app/pybossa/cli.py db_create
else
    echo "Postgres database already populated with pybossa tables!"
fi

# This will exec the CMD from Dockerfile
exec "$@"