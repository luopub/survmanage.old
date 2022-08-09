from django.db import models
from django.utils import timezone

from channel.models import Channel
from algorithm.models import Algorithm


MAX_FILE_LEN = 256


class Alert(models.Model):
    channel = models.ForeignKey(Channel, verbose_name='报警通道', on_delete=models.CASCADE)
    algorithm = models.ForeignKey(Algorithm, verbose_name='算法', on_delete=models.CASCADE)
    date_time = models.DateTimeField(default=timezone.now, verbose_name='报警时间')
    img = models.CharField(max_length=MAX_FILE_LEN, verbose_name='报警图片')
    img_unmark = models.CharField(max_length=MAX_FILE_LEN, null=True, verbose_name='报警图片')

    class Meta:
        unique_together = (('channel', 'algorithm', 'date_time'), )

    @classmethod
    def add_alerts(cls, cno=None, img_unmark=None, img=None, predicts=[]):
        try:
            channel = Channel.objects.get(cno=cno)
        except Channel.DoesNotExist:
            return

        for predict in predicts:
            algorithm = Algorithm.get_algorithm_by_predict(predict)
            if not algorithm:
                continue
            cls.objects.create(channel=channel, algorithm=algorithm, img_unmark=img_unmark, img=img)
