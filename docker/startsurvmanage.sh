#!/bin/sh

# wait mysql to be ready
while true; do if [ -z `python3 /survmanage/docker/check_mysql_ready.py` ]; then echo mysql not ready.; sleep 5; else echo mysql ready.; break; fi; done

cd /survmanage
python manage.py migrate
python3 manage.py runserver 0.0.0.0:${SURVMANAGE_PORT:-6789}

