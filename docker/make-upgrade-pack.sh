# build dockers，在survmanage上一层目录
# Usage:
#     ./build-all.sh -v <version> -r <repository>


usage () {
  echo "usage: $1 -v <version>"
}

version=
while getopts "v:h" arg #选项后面的冒号表示该选项需要参数
do
        case $arg in
             v)
                version=$OPTARG
                ;;
             h)
                usage "$0"
                exit 0
                ;;
             ?)  #当有不认识的选项的时候arg为?
			    echo "unkonw argument"
                exit 1
        ;;
        esac
done

if [ "x$version" == x ]; then
  echo version is required.
  usage "$0"
  exit 1
fi

tmp_root=/tmp
working_name="upgrade-${version}"
working_dir="${tmp_root}/${working_name}"
sudo rm -rf "${working_dir}"
sudo mkdir -p "${working_dir}"
cd "${working_dir}"

# prepare files
sudo docker save survmanage:latest -o survmanage-latest.tar && sudo chmod +r survmanage-latest.tar
sudo docker save survmanagenginx:latest -o survmanagenginx-latest.tar && sudo chmod +r survmanagenginx-latest.tar
sudo docker save imageserver:latest -o imageserver-latest.tar && sudo chmod +r imageserver-latest.tar
#sudo cp -R /docker .
#sudo cp /etc/rc.local .

# Then pack the directory
cd ..
sudo rm -f ${working_name}.tar
sudo tar czf ${working_name}.tar ${working_name}
sudo chmod +r ${working_name}.tar

echo Copy to upload directory ...
cd /docker
sudo docker compose cp "${tmp_root}/${working_name}.tar" survmanage:/dynamic_data/upload