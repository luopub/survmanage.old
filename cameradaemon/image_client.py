import socket
import json
from django.conf import settings


class ImageClient:
    def __init__(self, cmd, **kwargs):
        self.cmd = cmd
        self.data = kwargs

    def do_request(self):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                # Connect to server and send data
                sock.connect((settings.IMAGE_SERVER_HOST, settings.IMAGE_SERVER_PORT))
                data = {
                    'cmd': self.cmd,
                    'data': self.data
                }
                sock.sendall(json.dumps(data).encode('utf8'))

                # Receive data from the server and shut down
                received = str(sock.recv(1024), "utf-8")

                print("Sent:     {}".format(data))
                print("Received: {}".format(received))

                return json.loads(received)
        except:
            pass