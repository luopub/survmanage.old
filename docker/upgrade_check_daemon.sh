#!/bin/bash

REPO_NAME=docker20190707
# Must start from /docker
working_dir=/docker
upgrade_flag_file=${working_dir}/upgrade_flag
reset_flag_file=${working_dir}/reset_flag

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

    copy_docker_files

    echo Upgrade done. Retart system ...
    shutdown -r now
}

function reset_device () {
    echo Retart system ...
    shutdown -r now
}

function manual_upgrade () {
  echo manual upgrade from "$1"

  echo Copy upgrade from docker to local
  cd "$working_dir"
  sudo docker compose cp "survmanage:$1" .

  filename=$(basename "$1")
  directory=$(basename "$filename" .tar)

  upgrade_file_path="/tmp/$filename"

  if [ "$directory" == "$filename" ]; then
    echo Package must be a tar ball file.
    exit 1
  fi

  sudo rm -rf "$directory"

  echo Extracting tarball ...
  tar xf "$upgrade_file_path" -C /tmp

  sudo chmod -R +r "$directory"

  echo Shutdown running containers ...
  # 先关闭原来的compose
  cd "$working_dir"
  sudo docker compose down
  sudo docker compose rm -f
  sudo docker image rm -f survmanage:latest
  sudo docker image rm -f imageserver:latest
  sudo docker image rm -f survmanagenginx:latest

  echo Load new images from tarball ...
  cd "/tmp/$directory"
  sudo docker load -i survmanage-latest.tar
  sudo docker load -i imageserver-latest.tar
  sudo docker load -i survmanagenginx-latest.tar

  echo Remove the temp folder ...
  cd ..
  sudo rm -rf "$directory"

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
  fi
  sleep 10
done
