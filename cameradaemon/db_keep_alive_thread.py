import time
from threading import Thread

from alert.models import Alert

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
            logger.info(f'DbKeepAliveThread, alerts count = {Alert.objects.count()}')
