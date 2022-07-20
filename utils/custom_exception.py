from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response

from django.db import IntegrityError
from django.core.exceptions import ValidationError as DJ_ValidationError
from django.http.response import Http404

from .code_message_exception import CodeMsgException


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    errors_406 = (ValueError, IntegrityError, DJ_ValidationError)
    errors_403 = (AttributeError, )

    if isinstance(exc, CodeMsgException):
        return exc.to_response()
    elif not response:
        if isinstance(exc, errors_406):
            return Response(data={'message': exc.args[0]}, status=status.HTTP_406_NOT_ACCEPTABLE)
        elif isinstance(exc, errors_403):
            return Response(data={'message': exc.args[0]}, status=status.HTTP_403_FORBIDDEN)
    if isinstance(exc, Http404) or str(type(exc)).find('.DoesNotExist') > 0:
        return Response(data={'message': exc.args[0]}, status=status.HTTP_404_NOT_FOUND)
    if isinstance(exc, ValidationError):
        return Response(data={'message': exc.args[0]}, status=response.status_code)

    if isinstance(exc, ValidationError):
        response.data['code'] = response.status_code
        response.data['data'] = []
        if isinstance(response.data, dict):
            response.data['message'] = list(dict(response.data).values())[0][0]

            for key in dict(response.data).keys():

                if key not in ['code', 'data', 'message']:
                    response.data.pop(key)

        else:
            response.data['message'] = '输入有误'

        return response

    if response is not None:
        response.data.clear()
        response.data['code'] = response.status_code
        response.data['data'] = []

        if response.status_code == 404:
            try:
                response.data['message'] = response.data.pop('detail')
                response.data['message'] = "未找到"
            except KeyError:
                response.data['message'] = "未找到"

        if response.status_code == 400:

            response.data['message'] = '输入错误'

        elif response.status_code == 401:
            response.data['message'] = '未认证'

        elif response.status_code >= 500:
            response.data['message'] = "服务器错误"

        elif response.status_code == 403:
            response.data['message'] = "权限不允许"

        elif response.status_code == 405:
            response.data['message'] = '请求不允许'
        else:
            response.data['message'] = '未知错误'
    return response
