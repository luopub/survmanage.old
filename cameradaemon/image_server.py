import socketserver
from django.conf import settings


class ImageServerHandler(socketserver.BaseRequestHandler):
    def __init__(self, *args, **kwargs):
        super(ImageServerHandler, self).__init__(*args, **kwargs)

    def handle(self):
        print('self.server.handler', self.server.handler)
        print("{} wrote:".format(self.client_address[0]))

        # self.request is the TCP socket connected to the client
        data = self.request.recv(1024).strip()
        print(data)
        if self.server.handler:
            res = self.server.handler(data)

        if not self.server.handler or not res:
            res = 'Not processeded!'.encode('utf8')

        self.request.sendall(res)


class ImageServer(socketserver.TCPServer):
    def __init__(self, handler):
        super(ImageServer, self).__init__((settings.IMAGE_SERVER_HOST, settings.IMAGE_SERVER_PORT), ImageServerHandler)
        self.handler = handler

    @classmethod
    def serve(cls, handler=None):
        with cls(handler) as server:
            server.serve_forever()
