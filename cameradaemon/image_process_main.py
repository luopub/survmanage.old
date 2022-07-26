import time
from django.conf import settings
from threading import Thread
import os

from channel.models import Channel, ChannelAlgorithm
from alert.models import Alert

from .db_keep_alive_thread import DbKeepAliveThread
from .image_read_process import ImageProcess
from .image_server import ImageServer
from .image_server_code import *
from .utils import save_raw_frame

from utils.logutils import get_logger
logger = get_logger(__file__)

CHANNEL_PER_PROCESS = 2


class ImageChannelsManager:
    def __init__(self, channels_num):
        # 通道编号转换成索引
        self.channels_num = channels_num
        self.image_processes = [None for _ in range((self.channels_num // CHANNEL_PER_PROCESS) + (1 if (self.channels_num % CHANNEL_PER_PROCESS) else 0))]

    def start_channel_starter(self):
        def starter():
            while True:
                for i, ip in enumerate(self.image_processes):
                    if ip and ip.is_alive():
                        continue

                    # 如果对象存在，释放资源
                    if ip:
                        try:
                            ip.close()
                        except:
                            pass

                    cnos = [j + 1 for j in range(i * CHANNEL_PER_PROCESS, (i + 1) * CHANNEL_PER_PROCESS)]

                    logger.info(f"{i}-{cnos}-ImageProcess is not alive, start it")

                    cas = [ChannelAlgorithm.get_cas_params(cno) for cno in cnos]
                    cameras = [Channel.objects.get(cno=cno).url for cno in cnos]

                    self.image_processes[i] = ip = ImageProcess(cnos, model_path=settings.MODEL_PATH, model_device=settings.MODEL_DEVICE, cas=cas, cameras=cameras)

                    ip.start()

                    time.sleep(1)

                # 每分钟检查一圈
                time.sleep(60)

        Thread(target=starter).start()

    def set_channel_camera(self, cno, camera):
        """
        :param cno: channel number - 1 = index
        :param camera: camera is the rtsp url
        :return:
        """
        if cno > len(self.image_processes):
            return False
        self.image_processes[cno - 1].set_camera(cno, camera)
        return True

    def get_latest_image(self, ip, cno):
        frame = ip.get_latest_image(cno)
        if frame is not None:
            return save_raw_frame(frame, cno=cno)

    def get_ip_from_cmd(self, data):
        """
        Get cno and ip and result if not valid cno
        """
        try:
            cno = data['data']['cno']
            ips = list(filter(lambda x: x.has_channel(cno), self.image_processes))
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

    def cmd_handler(self, data):
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
                    res = success_result(data_={'filename': self.get_latest_image(ip, cno)})
            elif cmd == IMG_CMD_CHANNEL_ALG_CHANGED:
                if ip:
                    cas = ChannelAlgorithm.get_cas_params(cno)
                    ip.set_params(cno, cas)
                    res = success_result()
            elif cmd == IMG_CMD_CHANNEL_CONFIGURED:
                if ip:
                    try:
                        channel = Channel.objects.get(cno=cno)
                        ip.set_camera(cno, channel.url)
                        res = success_result()
                    except Channel.DoesNotExist:
                        res = {
                            'code': IMG_CODE_CHANNEL_NOT_FOUND,
                            'data': {}
                        }
            elif cmd == IMG_CMD_CHANNEL_DELETED:
                if ip:
                    ip.set_camera(cno, '')
                    res = success_result()
            elif cmd == IMG_CMD_CHANNEL_GET_ONLINE:
                if ip:
                    res = success_result(data_={'online': not not ip.get_online(cno)})
            elif cmd == IMG_CMD_DB_KEEP_ALIVE:
                alert_count = Alert.objects.count()
                logger.info(f'DbKeepAliveThread, alerts count = {alert_count}')
                res = success_result()
        except Exception as e:
            logger.warning(f'Exception happened for command: {type(e)}, {e}')
        return res

    def main_loop(self):
        self.start_channel_starter()

        DbKeepAliveThread().start()
        while True:
            server_thread = Thread(target=ImageServer.serve, args=[self.cmd_handler])
            server_thread.start()
            server_thread.join()
            logger.warning('Imager server_thread exited. Restart it.')
        # ImageServer.serve(self.cmd_handler)
        # while True:
        #     time.sleep(1)

    @staticmethod
    def main(**kwargs):
        logger.info(f'Image process main: {os.getpid()}')

        max_camera = int(kwargs.get('max_camera', '2'))

        rtsp_url = 'rtsp://admin:qwer123456@192.168.0.6:554/h264/ch1/main/av_stream'

        icm = ImageChannelsManager(max_camera)

        icm.main_loop()
