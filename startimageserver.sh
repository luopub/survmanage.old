#!/bin/sh

cd /survmanage
python3 manage.py cameradaemon --max-camera=${MAX_CAMERA:-8}

