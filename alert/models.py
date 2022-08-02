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

    class Meta:
        unique_together = (('channel', 'algorithm', 'date_time'), )

    pred_name_to_alg_name = {
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
    def get_algorithm_by_predict(cls, predict):
        """
        将预测结果类名转换成算法类名，并获取算法记录
        """
        alg_name = cls.pred_name_to_alg_name.get(predict['name'])
        try:
            return Algorithm.objects.get(name=alg_name)
        except Algorithm.DoesNotExist:
            pass

    @classmethod
    def add_alerts(cls, cno=None, filename=None, predicts=[]):
        try:
            channel = Channel.objects.get(cno=cno)
        except Channel.DoesNotExist:
            return

        for predict in predicts:
            algorithm = cls.get_algorithm_by_predict(predict)
            if not algorithm:
                continue
            cls.objects.create(channel=channel, algorithm=algorithm, img=filename)
