import platform
import os
import pathlib
from ruamel.yaml import YAML
from django.contrib.auth.models import User
from rest_framework import routers
from rest_framework.decorators import action
from rest_framework.response import Response
from django.conf import settings
from rest_framework.authtoken.models import Token

from utils.rest_mixins import GroupbyMixin
from utils.rest_utils import MyModelViewSet, SimpleViewSetBase
from utils.error_code import ErrorCode
from utils.code_message_exception import CodeMsgException

from channel.models import Channel, ChannelAlgorithm
from algorithm.models import Algorithm, AlgorithmDefaultParameters
from alert.models import Alert

from .models import ProjectInfo, ImageIcon, SystemInfo

from . import deviceinfo


class NetworkSetting:
    @classmethod
    def set_static_network_values(cls, data, value):
        data['addresses'] = [value['ip']+'/'+str(cls.mask_to_mask_bits(value['mask']))]
        data['gateway4'] = value['gateway']
        data['nameservers'] = {'addresses': [value['dns1'], value['dns2']]}

    @classmethod
    def set_network_settings_eth0(cls, eth0):
        """
            network:
               version: 2
               renderer: networkd
               ethernets:
                  eth0:
                     dhcp4: no
                     addresses: [192.168.0.166/24]
                     gateway4: 192.168.0.1 #这里注释掉，不然连接不上外网，有线的优先级发生冲突
                     nameservers: #也注释掉，用不到
                         addresses: [114.114.114.114,8.8.8.8]
        """
        data = {
            'network': {
                'version': 2,
                'renderer': 'networkd',
                'ethernets': {
                    'eth0': {
                    }
                }
            }
        }

        data_eth0 = data['network']['ethernets']['eth0']
        use_dhcp = ('useDhcp' not in eth0) or eth0.get('useDhcp')
        data_eth0['dhcp4'] = 'yes' if use_dhcp else 'no'

        if not use_dhcp:
            cls.set_static_network_values(data_eth0, eth0)

        yaml = YAML()
        yaml.dump(data, settings.NETWORK_CONFIG_ETH0)

    @classmethod
    def set_network_settings_wlan0(cls, wlan0):
        """
            network:
                version: 2
                renderer: networkd
                #ethernets:
                wifis:
                    wlan0:
                        dhcp4: no
                        access-points:
                            "TP-LINK-DY":
                                 password: "dianying123"
                        addresses: [192.168.0.222/24]
                        gateway4: 192.168.0.1
                        nameservers:
                            addresses: [114.114.114.114,8.8.8.8]
        """
        if wlan0.get('enableWlan'):
            data = {
                'network': {
                    'version': 2,
                    'renderer': 'networkd',
                    'wifis': {
                        'wlan0': {
                        }
                    }
                }
            }
            data_wlan0 = data['network']['wifis']['wlan0']
            use_dhcp = ('useDhcp' not in wlan0) or wlan0.get('useDhcp')
            data_wlan0['dhcp4'] = 'yes' if use_dhcp else 'no'
            if wlan0.get('ssidName'):
                data_wlan0['access-points'] = {
                    wlan0.get('ssidName'): {
                        'password': wlan0.get('ssidPassword')
                    }
                }
            if not use_dhcp:
                cls.set_static_network_values(data_wlan0, wlan0)
        else:
            data = {
                'network': {
                    'version': 2,
                    'renderer': 'networkd'
                }
            }

        yaml = YAML()
        yaml.dump(data, settings.NETWORK_CONFIG_WLAN0)

    @classmethod
    def set_network_settings(cls, data):
        eth0 = data.get('eth0')
        cls.set_network_settings_eth0(eth0)
        wlan0 = data.get('wlan0')
        cls.set_network_settings_wlan0(wlan0)

    @staticmethod
    def get_static_network_values(data):
        address = data['addresses'][0]
        mask_bits = ('/' in address and int(address.split('/')[1])) or 0
        ip = ('/' in address and address.split('/')[0]) or address
        gateway = data['gateway4']
        dns = data['nameservers']['addresses']
        dns1 = len(dns) > 0 and dns[0] or None
        dns2 = len(dns) > 1 and dns[1] or None

        return ip, mask_bits, gateway, dns1, dns2

    @staticmethod
    def mask_bits_to_mask(mask_bits):
        mask = [(256 - (1 << (8 - min(8, max(0, mask_bits - i * 8))))) for i in range(4)]

        return '.'.join([str(m) for m in mask])

    @staticmethod
    def mask_to_mask_bits(mask):
        mask = mask.split('.')
        mask = [int(m) << (8*(3-i)) for i, m in enumerate(mask)]
        mask_value = sum(mask)
        for i in range(32):
            if (mask_value & (1 << i)) != 0:
                return 32 - i
        return 0

    @classmethod
    def get_network_settings_from_yaml(cls):
        result = {}
        if settings.NETWORK_CONFIG_ETH0.exists():
            with open(settings.NETWORK_CONFIG_ETH0, encoding='utf-8') as f:
                yaml = YAML(typ='safe')  # default, if not specfied, is 'rt' (round-trip)
                data = yaml.load(f)
                try:
                    eth0 = data['network']['ethernets']['eth0']
                    use_dhcp = eth0['dhcp4'] == 'yes'
                    data_eth0 = {
                        'useDhcp': use_dhcp
                    }
                    if not use_dhcp:
                        ip, mask_bits, gateway, dns1, dns2 = cls.get_static_network_values(eth0)
                        data_eth0.update({
                            'ip': ip,
                            'mask': cls.mask_bits_to_mask(mask_bits),
                            'gateway': gateway,
                            'dns1': dns1,
                            'dns2': dns2
                        })
                    result['eth0'] = data_eth0
                except Exception as e:
                    pass

        if settings.NETWORK_CONFIG_WLAN0.exists():
            with open(settings.NETWORK_CONFIG_WLAN0, encoding='utf-8') as f:
                yaml = YAML(typ='safe')  # default, if not specfied, is 'rt' (round-trip)
                data = yaml.load(f)
                try:
                    wlan0 = data['network']['wifis']['wlan0']
                    use_dhcp = wlan0['dhcp4'] == 'yes'
                    data_wlan0 = {
                        'useDhcp': use_dhcp
                    }
                    ssid_name = list(wlan0['access-points'].keys())[0]
                    ssid_password = list(wlan0['access-points'].values())[0]['password']
                    data_wlan0.update({
                        'ssidName': ssid_name,
                        'ssidPassword': ssid_password,
                        'enableWlan': not not (ssid_name and ssid_password)
                    })
                    if not use_dhcp:
                        ip, mask_bits, gateway, dns1, dns2 = cls.get_static_network_values(wlan0)
                        data_wlan0.update({
                            'ip': ip,
                            'mask': cls.mask_bits_to_mask(mask_bits),
                            'gateway': gateway,
                            'dns1': dns1,
                            'dns2': dns2
                        })
                    result['wlan0'] = data_wlan0
                except Exception as e:
                    pass
        return result


class ProjectInfoViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = ProjectInfo

    authentication_classes = []
    permission_classes = []

    @action(detail=False, methods=['get'])
    def auth_info(self, request):
        if settings.AUTH_CHECK_ONLINE:
            code, message = self.model.re_activate()
            if code != 0:
                raise CodeMsgException(code, message)
        else:
            if self.model.objects.count() == 0:
                raise CodeMsgException(ErrorCode.NOT_ACTIVATED, '系统尚未激活')

        return Response({'project_name': self.model.objects.first().project_name})

    @action(detail=False, methods=['post'])
    def activate(self, request):
        # if self.model.activated():
        #     raise CodeMsgException(ErrorCode.ALREADY_ACTIVED, '项目不能重复激活')

        # 检查项目名称
        data = request.data
        project_name = data.get('project_name')
        if not project_name:
            raise CodeMsgException(ErrorCode.INVALID_PROJECT_NAME, '项目名称无效')

        # auth_code = data.get('auth_code')
        # if not self.model.check_auth_code(auth_code):
        #     raise CodeMsgException(ErrorCode.INVALID_AUTH_CODE, '授权码无效或已使用')

        username = data.get('username')
        password = data.get('password')
        if not username:
            raise CodeMsgException(ErrorCode.INVALID_USERNAME, '用户名不能为空')
        if not password:
            raise CodeMsgException(ErrorCode.INVALID_PASSWORD, '密码不能为空')

        # 先新建用户
        try:
            # 如果用户名已经存在，删除后重新创建
            user = User.objects.get(username=username)
            Token.objects.filter(user=user).delete()
            user.delete()
        except Exception as e:
            pass
        try:
            user = User.objects.create_user(username=username, password=password)
        except Exception as e:
            raise CodeMsgException(ErrorCode.INVALID_USERNAME_OR_PASSWORD, '用户名或密码不合格')

        # Save after all check finished
        auth_code = data.get('auth_code')
        code, message = self.model.activate(project_name, auth_code)
        if code:
            # 如果激活失败，就将用户删除。以免产生多个用户
            user.delete()
            raise CodeMsgException(code, message)
        else:
            return Response({})

    @action(detail=False, methods=['get'])
    def get_disk_stats(self, request):
        """
        Return disk stats in GB
        """
        if settings.IS_DEPLOYED:
            s = os.statvfs('/')
            stats = {
                'size': s.f_bsize * s.f_blocks / (1 << 30),
                'free': s.f_bsize * s.f_bavail / (1 << 30)
            }
        else:
            stats = {'size': 1e3, 'free': 3.5e2}
        return Response(stats)

    @action(detail=False, methods=['get'])
    def get_device_info(self, request):
        di = {
            'memory': deviceinfo.memory_stat(),
            'cpu': deviceinfo.cpu_stat(),
            'load': deviceinfo.load_stat(),
            'uptime': deviceinfo.uptime_stat(),
            'net': deviceinfo.net_stat(),
            'disk': deviceinfo.disk_stat(),
            'release': deviceinfo.release_stat(),
            'host': deviceinfo.host_stat(),
            'uname': deviceinfo.uname_stat(),
        }
        return Response(di)

    @action(detail=False, methods=['post'])
    def start_upgrade(self, request):
        with open(settings.UPGRADE_FLAG_FILE, 'wt') as f:
            f.write('network-upgrade')

        return Response({})

    @action(detail=False, methods=['post'])
    def start_upgrade_manual(self, request):
        filename = request.data.get('filename', '')
        file_path = settings.UPLOAD_FILE_DIR.joinpath(filename)

        if not filename or not file_path.exists():
            raise CodeMsgException(ErrorCode.UPGRADE_FILE_NOT_FOUND, '升级文件不存在')

        with open(settings.UPGRADE_FLAG_FILE, 'wt', encoding='utf8') as f:
            f.write(str(file_path))

        return Response({})

    @staticmethod
    def start_reset_device():
        with open(settings.RESET_FLAG_FILE, 'wt') as f:
            f.write('start reset')

    @action(detail=False, methods=['post'])
    def reset_device(self, request):
        self.start_reset_device()
        return Response({})

    @action(detail=False, methods=['post'])
    def reset_params(self, request):
        ChannelAlgorithm.delete_all()
        AlgorithmDefaultParameters.delete_all()

        with open(settings.RESET_FLAG_FILE, 'wt') as f:
            f.write('start reset')

        return Response({})

    @staticmethod
    def delete_all_data():
        image_dir = settings.ALERT_IMAGE_DIR
        if platform.system().lower() == 'linux':
            del_cmd = f'rm -rf {image_dir}/*'
        else:
            del_cmd = rf'del /F/S/Q {image_dir}\*'

        os.system(del_cmd)

    @action(detail=False, methods=['post'])
    def factory_reset(self, request):
        Alert.delete_all()
        ChannelAlgorithm.delete_all()
        Channel.delete_all()
        Algorithm.delete_all()
        AlgorithmDefaultParameters.delete_all()
        ProjectInfo.delete_all()
        User.objects.all().delete()
        self.delete_all_data()

        with open(settings.RESET_FLAG_FILE, 'wt') as f:
            f.write('start reset')

        return Response({})

    @action(detail=False, methods=['get'])
    def get_network_settings(self, request):
        result = NetworkSetting.get_network_settings_from_yaml()
        return Response(result)

    @action(detail=False, methods=['post'])
    def save_network_and_reset(self, request):
        NetworkSetting.set_network_settings(request.data)
        self.start_reset_device()
        return Response({})


class UserViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = User

    @action(detail=False, methods=['post'])
    def logout(self, request):
        try:
            Token.objects.filter(user=request.user).delete()
        except:
            pass

        return Response({})

    @action(detail=False, methods=['post'])
    def change_password(self, request):
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')
        if not request.user.check_password(old_password):
            raise CodeMsgException(ErrorCode.INVALID_PASSWORD, '旧密码错误')
        try:
            request.user.set_password(new_password)
            request.user.save()
        except:
            raise CodeMsgException(ErrorCode.INVALID_PASSWORD, '新密码格式不正确')
        return Response({})


class ImageIconViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = ImageIcon

    @action(detail=False, methods=['post'])
    def save_or_update(self, request):
        name = request.data.get('name')
        file_name = request.data.get('file_name')
        if not name or not file_name:
            raise CodeMsgException(ErrorCode.INVALID_ICON_OR_FILE, '名称为空')

        self.model.save_or_update(name, file_name)
        return Response({})

    @action(detail=False, methods=['get'])
    def get_all_icon_images(self, request):
        image_paths = [
            pathlib.Path(settings.BASE_DIR).joinpath('static').joinpath('images'),
            settings.UPLOAD_IMAGE_DIR
        ]
        image_types = ['*.jpg', '*.png', '*.JPG', '*.PNG']
        images = []
        for ip in image_paths:
            for it in image_types:
                files = ip.glob(it)
                images.extend(map(lambda x: x.name, files))
        return Response({'names': images})


class SystemInfoViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = SystemInfo


router = routers.DefaultRouter()
router.register('projectinfos', ProjectInfoViewSet)
router.register('users', UserViewSet)
router.register('imageicons', ImageIconViewSet)
router.register('systeminfos', SystemInfoViewSet)

