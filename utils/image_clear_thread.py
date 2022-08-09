import os
import time
from threading import Thread, Event, Semaphore

from django.conf import settings


class ImageClearThread(Thread):
    """
    This is to clear temporary images generated by getting realtime images
    """
    def __init__(self):
        super(ImageClearThread, self).__init__(target=self.loop)
        self.images = set()
        self.event = Event()
        self.semaphore = Semaphore()

    def put_image(self, image, time_to_clear=30):
        with self.semaphore:
            self.images.add((image, time_to_clear, time.time()))
            self.event.set()

    def loop(self):
        while True:
            self.event.wait(timeout=5)
            with self.semaphore:
                deleted = []
                for item in self.images:
                    if time.time() - item[2] >= item[1]:
                        filepath = settings.ALERT_IMAGE_DIR.joinpath(item[0])
                        print('Removing image', filepath)
                        try:
                            os.remove(filepath)
                        except Exception as e:
                            print('Fail to delete image file: ', filepath)
                        deleted.append(item)
                for item in deleted:
                    self.images.remove(item)
                self.event.clear()


print('ImageClearThread Inited')
image_clear_thread = ImageClearThread()
image_clear_thread.start()
