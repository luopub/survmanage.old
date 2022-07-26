import socket
import json
from django.conf import settings

from utils.logutils import get_logger
logger = get_logger(__file__)


class ImageClient:
    def __init__(self, cmd, **kwargs):
        self.cmd = cmd
        self.data = kwargs

    def do_request(self, wait_result=True):
        logger.info(f"Sending to server: cmd={self.cmd}, data={self.data}")

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                # Connect to server and send data
                sock.connect((settings.IMAGE_SERVER_HOST, settings.IMAGE_SERVER_PORT))
                data = {
                    'cmd': self.cmd,
                    'data': self.data
                }
                sock.sendall(json.dumps(data).encode('utf8'))

                logger.info("Sent to server: {}".format(data))

                if wait_result:
                    # Receive data from the server and shut down
                    received = str(sock.recv(1024), "utf8")

                    logger.info("Result received: {}".format(received))

                    return json.loads(received)
        except Exception as e:
            logger.info(f'Fail to connect to {settings.IMAGE_SERVER_HOST}, {settings.IMAGE_SERVER_PORT}, {str(e)}')
