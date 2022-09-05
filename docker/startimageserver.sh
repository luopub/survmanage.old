#!/bin/sh

# wait mysql to be ready
while true; do if [ -z `python3 /survmanage/docker/check_mysql_ready.py` ]; then echo mysql not ready.; sleep 5; else echo mysql ready.; break; fi; done

cd /survmanage
python3 manage.py cameradaemon --max-camera=${MAX_CAMERA:-8}

