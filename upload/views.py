import pathlib
import os
import gc
import tempfile
from django.contrib.auth.models import User
from rest_framework import routers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from django.conf import settings

from utils.rest_mixins import GroupbyMixin
from utils.rest_utils import MyModelViewSet, SimpleViewSetBase
from utils.error_code import ErrorCode
from utils.code_message_exception import CodeMsgException
from utils.md5 import get_file_digest

from system.models import ProjectInfo


class UploadViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
    model = ProjectInfo  # This is only a placeholder, so do not worry
    # parser_classes = [*super().parser_classes, FileUploadParser]

    @action(detail=False, methods=['post'])
    def common(self, request):
        """
        Upload a chunk of file
        """
        files = request.FILES.getlist('file_field')
        file = files[0]
        filename = request.data.get('filename')
        if '.' not in filename:
            raise CodeMsgException(ErrorCode.UNKNOWN_FILE_TYPE, '未知文件类型')

        tfd, tmppath = tempfile.mkstemp(suffix='.' + filename.split('.')[-1], dir=settings.UPLOAD_IMAGE_DIR)
        with os.fdopen(tfd, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)

        tmppath = pathlib.Path(tmppath).resolve()
        digest = get_file_digest(tmppath)

        new_name = digest + '.' + filename.split('.')[-1]
        filepath = settings.UPLOAD_IMAGE_DIR.joinpath(new_name)
        if filepath.exists():
            tmppath.unlink()
        else:
            tmppath.rename(filepath)

        return Response({'filename': new_name})

    @action(detail=False, methods=['post'])
    def chunk(self, request):
        """
        Upload a chunk of file
        """
        files = request.FILES.getlist('file_field')
        file = files[0]
        filename = request.data.get('filename')
        chunk_number = request.data.get('chunkNumber')
        filepath = settings.UPLOAD_FILE_DIR.joinpath(f'{filename}{chunk_number}')
        with open(filepath, 'wb') as f:
            for chunk in file.chunks():
                f.write(chunk)

        # 尽快释放内存
        gc.collect()

        chunk_num = self.get_uploaded_chunk_num(request.data)

        return Response({'uploaded': chunk_num})

    @action(detail=False, methods=['post'])
    def merge(self, request):
        """
        Merge latest uploaded file chunks
        """
        max_chunk_size = 65536
        file_info = request.data
        filename = file_info.get('filename')
        chunk_num = self.get_uploaded_chunk_num(file_info)

        if chunk_num != file_info.get('totalChunks'):
            raise CodeMsgException(ErrorCode.UPLOAD_CHUNK_MISSING, '分块不足')

        file_path = settings.UPLOAD_FILE_DIR.joinpath(filename)
        with open(file_path, 'wb') as fw:
            for c in range(chunk_num):
                file_path_c = settings.UPLOAD_FILE_DIR.joinpath(f'{filename}{c}')
                with open(file_path_c, 'rb') as fr:
                    while True:
                        chunk = fr.read(max_chunk_size)
                        if len(chunk) == 0:
                            break
                        fw.write(chunk)

                # Delete the chuck file
                file_path_c.unlink()

        # 尽快释放内存
        gc.collect()

        if get_file_digest(file_path) != file_info.get('identifier'):
            raise CodeMsgException(ErrorCode.UPLOAD_CONTENT_ERROR, '内容有错')

        return Response({})

    @staticmethod
    def get_uploaded_chunk_num(file_info):
        files = [f.name for f in settings.UPLOAD_FILE_DIR.glob(rf'{file_info.get("filename")}*')]

        blocks = [f.replace(file_info.get("filename"), '') for f in files]
        blocks = sorted([int(b) for b in blocks if b.isdigit()])
        chunk_num = int(file_info.get('totalChunks'))
        for i in range(chunk_num):
            if i not in blocks:
                chunk_num = i
                break

        return chunk_num

    @action(detail=False, methods=['post'])
    def check_chunk_exist(self, request):
        """
        Check upload status of file
        """
        file_info = request.data

        chunk_num = self.get_uploaded_chunk_num(file_info)

        all_upload_success = False
        merge_success = False
        file_path = settings.UPLOAD_FILE_DIR.joinpath(file_info.get("filename"))
        if file_path.exists() and get_file_digest(file_path) == file_info.get('identifier'):
            all_upload_success = True
            merge_success = True
        elif chunk_num == file_info.get('totalChunks'):
            all_upload_success = True

        return Response({'allUploadSuccess': all_upload_success, 'mergeSuccess': merge_success, 'uploaded': chunk_num})


router = routers.DefaultRouter()
router.register('uploads', UploadViewSet)
