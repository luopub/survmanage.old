import time
from threading import Thread

from cameradaemon.image_client import ImageClient

from .image_server_code import IMG_CMD_DB_KEEP_ALIVE

from utils.logutils import get_logger
logger = get_logger(__file__)


class DbKeepAliveThread(Thread):
    """
    # Mysql will close connection each 8 hours (show variables like '%timeout%';)
    """
    def __init__(self):
        super(DbKeepAliveThread, self).__init__(target=self.loop)

    @staticmethod
    def loop():
        while True:
            time.sleep(600)
            ImageClient(IMG_CMD_DB_KEEP_ALIVE).do_request(wait_result=False)
