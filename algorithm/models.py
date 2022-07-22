from django.db import models


MAX_ALGORITHM_NAME_LEN = 32


class Algorithm(models.Model):
    name = models.CharField(max_length=MAX_ALGORITHM_NAME_LEN, verbose_name='英文名称')
    name_ch = models.CharField(max_length=MAX_ALGORITHM_NAME_LEN, verbose_name='中文名称')


class AlgorithmParametersMixin:
    analyze_interval = models.IntegerField(default=1000, verbose_name='分析问题(ms)')
    alert_interval = models.IntegerField(default=30, verbose_name='报警间隔')
    alert_threshold = models.IntegerField(default=0.5, verbose_name='报警阈值')
    alert_week_start = models.IntegerField(default=1, verbose_name='每周报警时间开始(1-7)')
    alert_week_end = models.IntegerField(default=7, verbose_name='每周报警时间结束(1-7)')
    alert_day_start = models.IntegerField(default=0, verbose_name='每日报警时间开始(0-23)')
    alert_day_end = models.IntegerField(default=23, verbose_name='每日报警时间结束(0-23)')


class AlgorithmParameters(models.Model, AlgorithmParametersMixin):
    # This model hold the global parameters for the algorithm
    pass
