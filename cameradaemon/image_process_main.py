import time
from django.conf import settings

from channel.models import Channel, ChannelAlgorithm
from alert.models import Alert

from .db_keep_alive_thread import DbKeepAliveThread
from .image_read_process import ImageProcess
from .image_server import ImageServer
from .image_server_code import *
from .utils import save_raw_frame

from utils.logutils import get_logger
logger = get_logger(__file__)


class ImageChannelsManager:
    def __init__(self, channels_num):
        # 通道编号转换成索引
        self.channels_num = channels_num
        self.image_processes = [ImageProcess(c+1, model_path=settings.MODEL_PATH, model_device=settings.MODEL_DEVICE) for c in range(self.channels_num)]

    def config_channels(self):
        for ip in self.image_processes:
            cas = ChannelAlgorithm.get_cas_params(ip.cno)
            ip.set_params(cas)

        # 读取通道数据，设置camera地址
        channels = Channel.objects.all()
        for c in channels:
            if c.cno > self.channels_num:
                continue
            self.set_channel_camera(c.cno, c.url)

    def start_channels(self):
        for ip in self.image_processes:
            ip.start()

    def set_channel_camera(self, cno, camera):
        """
        :param cno: channel number - 1 = index
        :param camera: camera is the rtsp url
        :return:
        """
        if cno > len(self.image_processes):
            return False
        self.image_processes[cno - 1].set_camera(camera)
        return True

    def set_channel_algorithms(self):
        pass

    def get_latest_image(self, ip):
        frame = ip.get_latest_image()

        return save_raw_frame(frame, cno=ip.cno)

    def get_ip_from_cmd(self, data):
        """
        Get cno and ip and result if not valid cno
        """
        try:
            cno = data['data']['cno']
            ips = list(filter(lambda x: x.cno == cno, self.image_processes))
            if ips:
                ip = ips[0]
                res = None
            else:
                ip = None
                res = {
                    'code': IMG_CODE_CHANNEL_NOT_FOUND,
                    'data': {}
                }
        except:
            cno, ip, res = 0, None, None
        return cno, ip, res

    def handlers(self, data):
        """
        所有命令应该是json格式:
        {
            cmd: int,
            data: dict
        }
        返回值：
        {
            code: int,
            data: dict
        }
        成功返回code=0
        """

        if not data:
            return None

        def success_result(data_={}):
            return {
                'code': IMG_CODE_SUCCESS,
                'data': data_
            }

        res = {
            'code': IMG_CODE_INVALID_CMD,
            'data': {}
        }
        try:
            # 因为大部分操作都是针对通道进行的，所以在这里统一获取参数
            cno, ip, res = self.get_ip_from_cmd(data)
            cmd = data['cmd']
            if cmd == IMG_CMD_OBJECT_DETECTED:
                cno = data['data']['cno']
                img = data['data']['img']
                img_unmark = data['data']['img_unmark']
                predicts = data['data']['predicts']
                Alert.add_alerts(cno=cno, img_unmark=img_unmark, img=img, predicts=predicts)
                res = success_result()
            elif cmd == IMG_CMD_GET_LATEST_IMAGE:
                if ip:
                    res = success_result(data_={'filename': self.get_latest_image(ip)})
            elif cmd == IMG_CMD_CHANNEL_ALG_CHANGED:
                if ip:
                    cas = ChannelAlgorithm.get_cas_params(ip.cno)
                    ip.set_params(cas)
                    res = success_result()
            elif cmd == IMG_CMD_CHANNEL_CONFIGURED:
                if ip:
                    try:
                        channel = Channel.objects.get(cno=cno)
                        ip.set_camera(channel.url)
                        res = success_result()
                    except Channel.DoesNotExist:
                        res = {
                            'code': IMG_CODE_CHANNEL_NOT_FOUND,
                            'data': {}
                        }
            elif cmd == IMG_CMD_CHANNEL_DELETED:
                if ip:
                    ip.set_camera('')
                    res = success_result()
            elif cmd == IMG_CMD_CHANNEL_GET_ONLINE:
                if ip:
                    res = success_result(data_={'online': not not ip.get_online()})
            elif cmd == IMG_CMD_DB_KEEP_ALIVE:
                alert_count = Alert.objects.count()
                logger.info(f'DbKeepAliveThread, alerts count = {alert_count}')
                res = success_result()
        except Exception as e:
            logger.warning(f'Exception happened for command: {type(e)}, {e}')
        return res

    def main_loop(self):
        self.start_channels()

        time.sleep(5)

        self.config_channels()

        DbKeepAliveThread().start()
        ImageServer.serve(self.handlers)
        # while True:
        #     time.sleep(1)

    @staticmethod
    def main(**kwargs):
        max_camera = int(kwargs.get('max_camera', '2'))

        rtsp_url = 'rtsp://admin:qwer123456@192.168.0.6:554/h264/ch1/main/av_stream'

        icm = ImageChannelsManager(max_camera)

        icm.main_loop()
