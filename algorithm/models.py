import json
from django.conf import settings
from django.db import models


MAX_ALGORITHM_NAME_LEN = 32
MAX_TIME_SEGS_LEN = 256 * 7


class Algorithm(models.Model):
    name = models.CharField(max_length=MAX_ALGORITHM_NAME_LEN, unique=True, verbose_name='英文名称')
    name_ch = models.CharField(max_length=MAX_ALGORITHM_NAME_LEN, verbose_name='中文名称')
    event_type = models.IntegerField(null=True)

    # 这是一个映射表，将yolov5的类目映射成我们所需要的类目英文名称
    with open(settings.MODEL_TO_ALG_FILE, encoding='utf-8') as f:
        model_to_alg_name = json.load(f)

    @classmethod
    def delete_all(cls):
        cls.objects.all().delete()

    @classmethod
    def refresh(cls, algorithms, delete_old=True):
        """
        algorithms as arrays of {name, name_ch, event_type} dict
        """
        if delete_old:
            new_names = set([a['name'] for a in algorithms])
            rm_names = set([obj.name for obj in cls.objects.all() if obj.name not in new_names])

            cls.objects.filter(name__in=rm_names).delete()

        for a in algorithms:
            cls.objects.update_or_create(name=a['name'], defaults={'name_ch': a['name_ch'], 'event_type': a['event_type']})

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


class AlgorithmDefaultParameters(AlgorithmParametersBase):
    """
    This saves only one record
    """

    @classmethod
    def delete_all(cls):
        cls.objects.all().delete()
