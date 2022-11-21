import json
import socketserver
from django.conf import settings

from utils.logutils import get_logger
logger = get_logger(__file__)


class ImageServerHandler(socketserver.BaseRequestHandler):
    def __init__(self, *args, **kwargs):
        super(ImageServerHandler, self).__init__(*args, **kwargs)

    def handle(self):
        try:
            logger.info(f'Request to be receive')
            # self.request is the TCP socket connected to the client
            data = self.request.recv(1024).strip()
            if data:
                data = json.loads(data.decode('utf8'))

                logger.info(f"{self.client_address[0]}:{self.client_address[1]} request received: {data}")

                res = self.server.handler(data)

                if res:
                    res = json.dumps(res).encode('utf8')
                    self.request.sendall(res)
        except Exception as e:
            logger.warning(f'Fail to receive from request: {str(e)}')


class ImageServer(socketserver.TCPServer):
    def __init__(self, handler):
        super(ImageServer, self).__init__((settings.IMAGE_SERVER_HOST, settings.IMAGE_SERVER_PORT), ImageServerHandler)
        self.handler = handler

    @classmethod
    def serve(cls, handler=None):
        with cls(handler) as server:
            server.serve_forever()
