#!/bin/bash

mysqlcheck() {
  # Wait for MySQL to be available...
  COUNTER=20
  until mysql -h mysql -u $MYSQL_ENV_MYSQL_USER -p$MYSQL_ENV_MYSQL_PASSWORD -e "show databases" 2>/dev/null; do
    echo "WARNING: MySQL still not up. Trying again..."
    sleep 10
    let COUNTER-=1
    if [ $COUNTER -lt 1 ]; then
      echo "ERROR: MySQL connection timed out. Aborting."
      exit 1
    fi
  done

  count=`mysql -h mysql -u $MYSQL_ENV_MYSQL_USER -p$MYSQL_ENV_MYSQL_PASSWORD -e "select count(*) from information_schema.tables where table_type='BASE TABLE' and table_schema='$MYSQL_ENV_MYSQL_DATABASE';" | tail -1`
  if [ "$count" == "0" ]; then
    echo "Database is empty. Creating database..."
    cd /opt/pdnsadmin
    source ./flask/bin/activate
    ./create_db.py
  fi
}

sed -i "s,%PDNS_STATS_URL%,${PDNS_STATS_URL}," /opt/pdnsadmin/config.py
mysqlcheck
 
# Start PowerDNS Admin
echo "Starting PowerDNS Admin..."

cd /opt/pdnsadmin
source ./flask/bin/activate
gunicorn --workers=4 -b $BIND_ADDRESS:$BIND_PORT run:app
