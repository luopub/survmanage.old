# build dockers，在survmanage上一层目录
# Usage:
#     ./push-all.sh -v <version> -r <repository>

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR
cd ../..

version=
repository=
latest=
while getopts "v:r:hl" arg #选项后面的冒号表示该选项需要参数
do
        case $arg in
             v)
                version=$OPTARG
                ;;
             r)
                repository=${OPTARG}/
                ;;
             l)
                latest=1
                ;;
             h)
                echo "usage: ./push-all.sh -v <version> -r <repository>"
                exit 0
                ;;
             ?)  #当有不认识的选项的时候arg为?
			    echo "unkonw argument"
                exit 1
        ;;
        esac
done

echo version "$version" #参数存在$OPTARG中
echo repository "${repository}"

if [ "x${repository}" == x ]; then
  echo repository must not be empty
  exit 1
fi

if [ "x${latest}" != x ]; then
  sudo docker push "${repository}survmanage:latest"
  sudo docker push "${repository}survmanagenginx:latest"
  sudo docker push "${repository}imageserver:latest"
fi

if [ "x${version}" != x ]; then
  sudo docker push "${repository}survmanage:${version}"
  sudo docker push "${repository}survmanagenginx:${version}"
  sudo docker push "${repository}imageserver:${version}"
fi
