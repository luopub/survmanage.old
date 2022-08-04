import time
from django.db import models


MAX_ALGORITHM_NAME_LEN = 32
MAX_TIME_SEGS_LEN = 256 * 7


class Algorithm(models.Model):
    name = models.CharField(max_length=MAX_ALGORITHM_NAME_LEN, verbose_name='英文名称')
    name_ch = models.CharField(max_length=MAX_ALGORITHM_NAME_LEN, verbose_name='中文名称')

    model_to_alg_name = {
        'person': 'human',
        'bicycle': '',
        'car': 'vehicle',
        'motorcycle': 'motor',
        'airplane': '',
        'bus': 'vehicle',
        'train': '',
        'truck': 'vehicle',
        'boat': '',
        'traffic light': '',
        'fire hydrant': '',
        'stop sign': '',
        'parking meter': '',
        'bench': '',
        'bird': 'animal',
        'cat': 'animal',
        'dog': 'animal',
        'horse': 'animal',
        'sheep': 'animal',
        'cow': 'animal',
        'elephant': 'animal',
        'bear': 'animal',
        'zebra': 'animal',
        'giraffe': 'animal',
        'backpack': '',
        'umbrella': '',
        'handbag': '',
        'tie': '',
        'suitcase': '',
        'frisbee': '',
        'skis': '',
        'snowboard': '',
        'sports ball': '',
        'kite': '',
        'baseball bat': '',
        'baseball glove': '',
        'skateboard': '',
        'surfboard': '',
        'tennis racket': '',
        'bottle': '',
        'wine glass': '',
        'cup': '',
        'fork': '',
        'knife': '',
        'spoon': '',
        'bowl': '',
        'banana': '',
        'apple': '',
        'sandwich': '',
        'orange': '',
        'broccoli': '',
        'carrot': '',
        'hot dog': '',
        'pizza': '',
        'donut': '',
        'cake': '',
        'chair': '',
        'couch': '',
        'potted plant': '',
        'bed': '',
        'dining table': '',
        'toilet': '',
        'tv': '',
        'laptop': '',
        'mouse': '',
        'remote': '',
        'keyboard': '',
        'cell phone': 'mobile',
        'microwave': '',
        'oven': '',
        'toaster': '',
        'sink': '',
        'refrigerator': '',
        'book': '',
        'clock': '',
        'vase': '',
        'scissors': '',
        'teddy bear': '',
        'hair drier': '',
        'toothbrush': '',
    }
    
    @classmethod
    def map_alg_name_to_model_name(cls, alg_name):
        for k, v in cls.model_to_alg_name.items():
            if v == alg_name:
                return k

    @classmethod
    def get_algorithm_by_predict(cls, predict):
        """
        将预测结果类名转换成算法类名，并获取算法记录
        """
        alg_name = cls.model_to_alg_name.get(predict['name'])
        try:
            return Algorithm.objects.get(name=alg_name)
        except Algorithm.DoesNotExist:
            pass


class AlgorithmParametersMixin:
    # No use!!! Only for normal running
    pass


class AlgorithmParametersBase(models.Model):
    analyze_interval = models.IntegerField(default=1000, verbose_name='分析问题(ms)')
    alert_interval = models.IntegerField(default=30, verbose_name='报警间隔')
    alert_threshold = models.FloatField(default=0.5, verbose_name='报警阈值')
    # 每天报警时段打包成字符串：00:00-08:00;11:30-16:00;20:00-24:00
    # 每周的报警时段以json格式打包:
    """
    [
        {
            enabled: <0 or 1>,
            segs: [(start1, end1), (start2, end2), ...]
        }
    ]
    """
    alert_times = models.CharField(max_length=MAX_TIME_SEGS_LEN, null=True, verbose_name='报警时段')

    class Meta:
        abstract = True
