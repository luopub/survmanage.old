#!/bin/bash

REPO_NAME=docker20190707
# Must start from /docker
working_dir=/docker
upgrade_flag_file=${working_dir}/upgrade_flag
reset_flag_file=${working_dir}/reset_flag_file
hard_reset_flag_file=${working_dir}/hard_reset_flag_file

function copy_docker_files() {
    cd "$working_dir"

    echo Stock container ...
    docker compose up -d

    echo Wait a while ...
    sleep 10

    echo Update compose.yaml ...
    docker container cp docker-survmanage-1:/survmanage/docker/compose.yaml ${working_dir}

    docker container cp docker-survmanage-1:/survmanage/docker/upgrade_check_daemon.sh ${working_dir}
    chmod +x ${working_dir}/upgrade_check_daemon.sh

    docker container cp docker-survmanage-1:/survmanage/docker/rc.local ${working_dir}
    chmod +x ${working_dir}/rc.local
}

function networks_upgrade() {
    echo Networks upgrade ...
    echo Start to pull dockers survmanage ...

    echo Remove old image tags ...
    docker image rm -f ${REPO_NAME}/survmanage:latest survmanage:latest
    docker image rm -f ${REPO_NAME}/imageserver:latest imageserver:latest
    docker image rm -f ${REPO_NAME}/survmanagenginx:latest survmanagenginx:latest

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

    echo Removing not used images ...
    docker image ls | grep "<none>" | awk '{print $3;}' | xargs docker image rm

    copy_docker_files

    echo Upgrade done. Retart system ...
    shutdown -r now
}

function reset_device () {
    echo Retart system ...
    shutdown -r now
}

function hard_reset_device () {
    echo Hard reset system ...

    cd "$working_dir"

    docker compose down
    docker compose rm -f

    sleep 5

    # run mysql alone
    nohup docker compose run mysqlsurv > /dev/null 2>&1 &

    sleep 10

    # Drop the database
    docker exec -it $(docker ps -a | grep mysql | grep 3306 | awk '{print $1}') mysql --password=12345678 -e "drop database if exists survmanage;"

    sleep 5

    # Create the empty database
    docker exec -it $(docker ps -a | grep mysql | grep 3306 | awk '{print $1}') mysql --password=12345678 -e "create database survmanage;"

    sleep 5

    # shutdown mysql and run all images
    docker container stop $(docker ps -a | grep mysql | grep 3306 | awk '{print $1}')

    sleep 5

    docker container prune --force

    # start docker, "python manage.py migrate" will run automatic
    nohup docker compose up > /dev/null 2>&1 &

    sleep 20

    # load default data
    docker exec -it $(docker ps -a | grep survmanage | grep 6789 | awk '{print $1}') /bin/bash -c "cd /survmanage && python manage.py loaddata initdata/benzhireporturl_default.json"
    docker exec -it $(docker ps -a | grep survmanage | grep 6789 | awk '{print $1}') /bin/bash -c "cd /survmanage && python manage.py loaddata initdata/imageicon_defaults.json"
    docker exec -it $(docker ps -a | grep survmanage | grep 6789 | awk '{print $1}') /bin/bash -c "cd /survmanage && python manage.py loaddata initdata/systeminfo_default.json"

    reset_device
}

function manual_upgrade () {
  echo manual upgrade from "$1"

  echo Copy upgrade from docker to local
  cd "$working_dir"
  docker compose cp "survmanage:$1" /tmp

  filename=$(basename "$1")
  directory=$(basename "$filename" .tar)

  upgrade_file_path="/tmp/$filename"
  upgrade_file_dir="/tmp/$directory"

  if [ "$directory" == "$filename" ]; then
    echo Package must be a tar ball file.
    exit 1
  fi

  rm -rf "$upgrade_file_dir"

  echo Extracting tarball ...
  tar xf "$upgrade_file_path" -C /tmp

  chmod -R +r "$upgrade_file_dir"

  echo Shutdown running containers ...
  # 先关闭原来的compose
  cd "$working_dir"
  docker compose down
  docker compose rm -f

  echo Removing old version...
  docker image rm -f survmanage:latest
  docker image rm -f imageserver:latest
  docker image rm -f survmanagenginx:latest

  echo Load new images from tarball ...
  cd "$upgrade_file_dir"
  docker load -i survmanage-latest.tar
  docker load -i imageserver-latest.tar
  docker load -i survmanagenginx-latest.tar

  echo Removing not used images ...
  docker image ls | grep "<none>" | awk '{print $3;}' | xargs docker image rm

  echo Remove the temp folder ...
  rm -rf "$upgrade_file_dir"

  copy_docker_files

  echo Upgrade done. Retart system ...
  shutdown -r now

}

while true; do
  if [ -f ${upgrade_flag_file} ]; then
    echo Found upgrade flag file ${upgrade_flag_file}
    upgrade_content=$(cat ${upgrade_flag_file})
    rm ${upgrade_flag_file}

    if [ "x$upgrade_content" == "xnetwork-upgrade" ]; then
      networks_upgrade
    else
      manual_upgrade "$upgrade_content"
    fi
  elif [ -f ${reset_flag_file} ]; then
    echo Found reset flag file ${reset_flag_file}
    rm ${reset_flag_file}

    reset_device
  elif [ -f ${hard_reset_flag_file} ]; then
    echo Found hard reset flag file ${hard_reset_flag_file}
    rm ${hard_reset_flag_file}

    hard_reset_device
  fi
  sleep 10
done
