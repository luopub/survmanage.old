import cv2 as cv
from PIL import Image
import numpy as np
import time
from django.conf import settings
from utils.md5 import get_digest


def save_image(image, cno=None, digest=''):
    """
    保存图片到系统目录
    """
    if cno:
        filename = f'{cno}-{time.strftime("%Y%m%d%H%M%S", time.localtime())}-{digest}.jpg'
    else:
        filename = f'{time.strftime("%Y%m%d%H%M%S", time.localtime())}-{digest}.jpg'

    filepath = settings.ALERT_IMAGE_DIR.joinpath(filename)

    image.save(filepath)

    return filename


def save_raw_frame(raw_frame, cno=None, cvt_color=True):
    """
    保存摄像头原始像素图片
    """
    # 格式转变，BGRtoRGB
    if cvt_color:
        frame = cv.cvtColor(raw_frame, cv.COLOR_BGR2RGB)
    else:
        frame = raw_frame

    digest = get_digest(frame.tobytes())

    # 转变成Image
    image = Image.fromarray(np.uint8(frame))

    filename = save_image(image, cno=cno, digest=digest)

    return filename
