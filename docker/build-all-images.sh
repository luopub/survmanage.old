# build dockers，在survmanage上一层目录
# Usage:
#     ./build-all.sh -v <version> -r <repository>

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR
cd ../..
sudo docker build -t survmanage:latest -f survmanage/docker/Dockerfile-survmanage .
sudo docker build -t survmanagenginx:latest -f survmanage/docker/Dockerfile-nginx .
sudo docker build -t imageserver:latest -f survmanage/docker/Dockerfile-imageserver .

version=
repository=
while getopts "v:r:" arg #选项后面的冒号表示该选项需要参数
do
        case $arg in
             v)
                version=$OPTARG
                ;;
             r)
                repository=${OPTARG}/
                ;;
             ?)  #当有不认识的选项的时候arg为?
			    echo "unkonw argument"
                exit 1
        ;;
        esac
done

echo version $version #参数存在$OPTARG中
echo repository ${repository}

if [ x${repository} != x ]; then
  sudo docker tag survmanage:latest ${repository}survmanage:latest
  sudo docker tag survmanagenginx:latest ${repository}survmanagenginx:latest
  sudo docker tag imageserver:latest ${repository}imageserver:latest
fi

if [ x${version} != x ]; then
  sudo docker tag survmanage:latest ${repository}survmanage:${version}
  sudo docker tag survmanagenginx:latest ${repository}survmanagenginx:${version}
  sudo docker tag imageserver:latest ${repository}imageserver:${version}
fi
