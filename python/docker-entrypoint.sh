#!/usr/bin/env ash

set -x

migrate() {
    PGPASSWORD=$dbpass createdb -h $dbhost -U $dbhost $dbname
    PGPASSWORD=$dbpass psql -U $dbhost -d $dbname -h $dbhost -a -f titanic.sql
}

sleep 10

[ $MIGRATE == "TRUE" ] && migrate || echo "Skipping Migration"

exec $@