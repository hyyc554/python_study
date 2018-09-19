# -*- coding: utf-8 -*-

from threading import Thread
import time


# def sayhi(name):
#     time.sleep(2)
#     print('%s say hi' % name)
#
#
# if __name__ == '__main__':
#     t = Thread(target=sayhi, args=('hyc',))
#     t.start()
#     print('主线程结束')


class Sayhi(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(2)
        print('%s say hi' % self.name)


if __name__ == '__main__':
    t = Sayhi('hyc')
    t.start()
    print('主线程结束')
