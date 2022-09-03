#!/bin/sh

cd /survmanage
python3 manage.py runserver 0.0.0.0:${SURVMANAGE_PORT:-6789}

