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
        'person': 'person',
        'bicycle': 'bicycle',
        'car': 'car',
        'motorcycle': 'motorcycle',
        'airplane': 'airplane',
        'bus': 'bus',
        'train': 'train',
        'truck': 'truck',
        'boat': 'boat',
        'traffic light': 'traffic light',
        'fire hydrant': 'fire hydrant',
        'stop sign': 'stop sign',
        'parking meter': 'parking meter',
        'bench': 'bench',
        'bird': 'bird',
        'cat': 'cat',
        'dog': 'dog',
        'horse': 'horse',
        'sheep': 'sheep',
        'cow': 'cow',
        'elephant': 'elephant',
        'bear': 'bear',
        'zebra': 'zebra',
        'giraffe': 'giraffe',
        'backpack': 'backpack',
        'umbrella': 'umbrella',
        'handbag': 'handbag',
        'tie': 'tie',
        'suitcase': 'suitcase',
        'frisbee': 'frisbee',
        'skis': 'skis',
        'snowboard': 'snowboard',
        'sports ball': 'sports ball',
        'kite': 'kite',
        'baseball bat': 'baseball bat',
        'baseball glove': 'baseball glove',
        'skateboard': 'skateboard',
        'surfboard': 'surfboard',
        'tennis racket': 'tennis racket',
        'bottle': 'bottle',
        'wine glass': 'wine glass',
        'cup': 'cup',
        'fork': 'fork',
        'knife': 'knife',
        'spoon': 'spoon',
        'bowl': 'bowl',
        'banana': 'banana',
        'apple': 'apple',
        'sandwich': 'sandwich',
        'orange': 'orange',
        'broccoli': 'broccoli',
        'carrot': 'carrot',
        'hot dog': 'hot dog',
        'pizza': 'pizza',
        'donut': 'donut',
        'cake': 'cake',
        'chair': 'chair',
        'couch': 'couch',
        'potted plant': 'potted plant',
        'bed': 'bed',
        'dining table': 'dining table',
        'toilet': 'toilet',
        'tv': 'tv',
        'laptop': 'laptop',
        'mouse': 'mouse',
        'remote': 'remote',
        'keyboard': 'keyboard',
        'cell phone': 'cell phone',
        'microwave': 'microwave',
        'oven': 'oven',
        'toaster': 'toaster',
        'sink': 'sink',
        'refrigerator': 'refrigerator',
        'book': 'book',
        'clock': 'clock',
        'vase': 'vase',
        'scissors': 'scissors',
        'teddy bear': 'teddy bear',
        'hair drier': 'hair drier',
        'toothbrush': 'toothbrush',
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
