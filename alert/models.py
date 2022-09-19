from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

from channel.models import Channel
from algorithm.models import Algorithm

from utils.logutils import get_logger

logger = get_logger('alert_model')


MAX_FILE_LEN = 256


class Alert(models.Model):
    channel = models.ForeignKey(Channel, verbose_name='报警通道', on_delete=models.CASCADE)
    algorithm = models.ForeignKey(Algorithm, verbose_name='算法', on_delete=models.CASCADE)
    date_time = models.DateTimeField(default=timezone.now, verbose_name='报警时间')
    img = models.CharField(max_length=MAX_FILE_LEN, verbose_name='报警图片')
    img_unmark = models.CharField(max_length=MAX_FILE_LEN, null=True, verbose_name='未标注图片')
    is_misreported = models.BooleanField(default=False, verbose_name='误报')

    class Meta:
        unique_together = (('channel', 'algorithm', 'date_time'), )

    post_save_handlers = []

    @classmethod
    def add_post_save_handler(cls, handler):
        cls.post_save_handlers.append(handler)

    @classmethod
    def delete_all(cls):
        cls.objects.all().delete()

    @classmethod
    def add_alerts(cls, cno=None, img_unmark=None, img=None, predicts=[]):
        try:
            channel = Channel.objects.get(cno=cno)
        except Channel.DoesNotExist as e:
            logger.info('Unknown channel %s' % cno)
            return

        for predict in predicts:
            algorithm = Algorithm.get_algorithm_by_predict(predict)
            if not algorithm:
                logger.info(f'Unknown algorithm, {cno}, {predict}')
                continue
            obj = cls.objects.create(channel=channel, algorithm=algorithm, img_unmark=img_unmark, img=img)
            if not obj:
                logger.info(f'Object create failed: {cno}, {predict}')


@receiver(post_save, sender=Alert)
def on_alert_post_save(sender, **kwargs):
    for handler in Alert.post_save_handlers:
        handler(kwargs['instance'])
