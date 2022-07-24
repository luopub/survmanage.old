from django.db import models


MAX_ALGORITHM_NAME_LEN = 32
MAX_TIME_SEGS_LEN = 256 * 7


class Algorithm(models.Model):
    name = models.CharField(max_length=MAX_ALGORITHM_NAME_LEN, verbose_name='英文名称')
    name_ch = models.CharField(max_length=MAX_ALGORITHM_NAME_LEN, verbose_name='中文名称')


class AlgorithmParametersMixin:
    # No use!!! Only for normal running
    pass


class AlgorithmParametersBase(models.Model):
    analyze_interval = models.IntegerField(default=1000, verbose_name='分析问题(ms)')
    alert_interval = models.IntegerField(default=30, verbose_name='报警间隔')
    alert_threshold = models.IntegerField(default=0.5, verbose_name='报警阈值')
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
