from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK


class CodeMsgException(Exception):
    def __init__(self, code, message):
        super().__init__()
        self.code = code
        self.message = message

    def to_response(self):
        return Response(data={'code_message': {'code': self.code, 'message': self.message}}, status=HTTP_200_OK)
