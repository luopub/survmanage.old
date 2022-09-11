#!/bin/bash

REPO_NAME=docker20190707
# Must start from /docker
working_dir=/docker
upgrade_flag_file=${working_dir}/upgrade_flag
reset_flag_file=${working_dir}/reset_flag

function networks_upgrade() {
		echo Start to pull dockers survmanage ...
		docker pull ${REPO_NAME}/survmanage:latest
		if [ x$? != x0 ]; then
		    exit $?
		fi

		echo Start to pull dockers imageserver ...
		docker pull ${REPO_NAME}/imageserver:latest
		if [ x$? != x0 ]; then
		    exit $?
		fi

		echo Start to pull dockers survmanagenginx ...
		docker pull ${REPO_NAME}/survmanagenginx:latest
		if [ x$? != x0 ]; then
		    exit $?
		fi

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
		docker container cp docker-survmanage-1:/survmanage/docker/compose.yaml ${working_dir}
		docker container cp docker-survmanage-1:/survmanage/docker/upgrade_check_daemon.sh ${working_dir}
		chmod +x ${working_dir}/upgrade_check_daemon.sh

		echo Upgrade done. Retart system ...
		shutdown -r now
}

function reset_device () {
		echo Retart system ...
		shutdown -r now
}

while true; do
	if [ -f ${upgrade_flag_file} ]; then
		echo Found upgrade flag file ${upgrade_flag_file}
		rm ${upgrade_flag_file}

		networks_upgrade
	elif [ -f ${reset_flag_file} ]; then
		echo Found reset flag file ${reset_flag_file}
		rm ${reset_flag_file}

		reset_device
	fi
	sleep 10
done
