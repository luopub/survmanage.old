import json
from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response

from django.db import IntegrityError
from django.core.exceptions import ValidationError as DJ_ValidationError
from django.http.response import Http404

from .code_message_exception import CodeMsgException
from .error_code import ErrorCode


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    errors_406 = (ValueError, IntegrityError, DJ_ValidationError)
    errors_403 = (AttributeError, )

    if isinstance(exc, CodeMsgException):
        return exc.to_response()
    elif not response:
        if isinstance(exc, errors_406):
            return CodeMsgException(ErrorCode.HTTP_406_NOT_ACCEPTABLE, exc.args[0]).to_response()
        elif isinstance(exc, errors_403):
            return CodeMsgException(ErrorCode.HTTP_403_FORBIDDEN, exc.args[0]).to_response()
    if isinstance(exc, Http404) or str(type(exc)).find('.DoesNotExist') > 0:
        return CodeMsgException(ErrorCode.HTTP_404_NOT_FOUND, exc.args[0]).to_response()
    if isinstance(exc, ValidationError):
        return CodeMsgException(ErrorCode.VALIDATION_ERROR, json.dumps(exc.args[0], ensure_ascii=False)).to_response()

    if response is not None:
        if response.status_code == 404:
            try:
                message = response.data.pop('detail')
            except KeyError:
                message = "未找到"

        elif response.status_code == 400:

            message = '输入错误'

        elif response.status_code == 401:
            message = '未认证'

        elif response.status_code >= 500:
            message = "服务器错误"

        elif response.status_code == 403:
            message = "权限不允许"

        elif response.status_code == 405:
            message = '请求不允许'
        else:
            message = '未知错误'

        return CodeMsgException(ErrorCode.SYSTEM_ERROR_BASE+response.status_code, message).to_response()

    return response
