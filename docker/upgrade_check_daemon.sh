#!/bin/bash

REPO_NAME=docker20190707
flag_file=upgrade_flag

while true; do
	if [ -f ${flag_file} ]; then
		echo Found upgrade flag file ${flag_file}
		rm ${flag_file}

		echo Start to pull dockers survmanage ...
		docker pull ${REPO_NAME}/survmanage:latest

		echo Start to pull dockers imageserver ...
		docker pull ${REPO_NAME}/imageserver:latest

		echo Start to pull dockers survmanagenginx ...
		docker pull ${REPO_NAME}/survmanagenginx:latest

		echo Shutdown running dockers
		docker compose down

		echo Remove old dockers ...
		docker image rm survmanage imageserver survmanagenginx

		echo Tag new dockers ...
		docker tag ${REPO_NAME}/survmanage:latest survmanage:latest
		docker tag ${REPO_NAME}/imageserver:latest imageserver:latest
		docker tag ${REPO_NAME}/survmanagenginx:latest survmanagenginx:latest

		echo Stock container ...
		docker compose up -d

		echo Wait a while ...
		sleep 10

		echo Update compose.yaml ...
		docker container cp docker-survmanage-1:/survmanage/docker/compose.yaml .

		echo Upgrade done. Retart system ...
		shutdown -r now
	else
		echo No upgrade, sleep some seconds
	fi
	sleep 10
done
