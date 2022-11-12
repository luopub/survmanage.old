from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
import collections

from channel.models import Channel
from algorithm.models import Algorithm

from utils.logutils import get_logger

logger = get_logger(__file__)


MAX_FILE_LEN = 256


class Alert(models.Model):
    channel = models.ForeignKey(Channel, verbose_name='报警通道', on_delete=models.CASCADE)
    algorithm = models.ForeignKey(Algorithm, verbose_name='算法', on_delete=models.CASCADE)
    date_time = models.DateTimeField(default=timezone.now, verbose_name='报警时间')
    img = models.CharField(max_length=MAX_FILE_LEN, verbose_name='报警图片')
    img_unmark = models.CharField(max_length=MAX_FILE_LEN, null=True, verbose_name='未标注图片')
    is_misreported = models.BooleanField(default=False, verbose_name='误报')
    num_objects = models.IntegerField(default=1, verbose_name="目标数量")

    class Meta:
        unique_together = (('channel', 'algorithm', 'img'), )

    post_save_handlers = []

    @classmethod
    def add_post_save_handler(cls, handler):
        cls.post_save_handlers.append(handler)

    @classmethod
    def delete_all(cls):
        cls.objects.all().delete()

    @classmethod
    def add_alerts(cls, cno=None, img_unmark=None, img=None, predicts=[]):
        alert_ids = []

        try:
            channel = Channel.objects.get(cno=cno)
        except Channel.DoesNotExist as e:
            logger.info('Unknown channel %s' % cno)
            return alert_ids

        # Get count for each algorithm
        try:
            alg_ids = [Algorithm.get_algorithm_by_predict(predict).id for predict in predicts]
            obj_counts = dict(collections.Counter(alg_ids))
        except Exception as e:
            obj_counts = dict()
            logger.info(f'Unknown algorithm found, {cno}, {img}')

        saved = set()
        for predict in predicts:
            algorithm = Algorithm.get_algorithm_by_predict(predict)
            if not algorithm:
                logger.info(f'Unknown algorithm, {cno}, {predict}')
                continue

            if algorithm.id in saved:
                logger.info(f'Duplicate algorithm object will be saved only once: {algorithm.id}')
                continue

            try:
                # 同一时刻同一通道同一类别多个目标检测结果只保存一条记录
                saved.add(algorithm.id)

                obj = cls.objects.create(channel=channel, algorithm=algorithm, img_unmark=img_unmark, img=img, num_objects=obj_counts.get(algorithm.id, 1))
                alert_ids.append(obj.id)
            except Exception as e:
                logger.info(f'Object create failed: {cno}, {predict}, {e}')

        return alert_ids


@receiver(post_save, sender=Alert)
def on_alert_post_save(sender, **kwargs):
    for handler in Alert.post_save_handlers:
        handler(kwargs['instance'])
