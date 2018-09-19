# -*- coding: utf-8 -*-
from threading import Thread, Lock
import time

li = [1, 2, 3, 4]


def a(l):
    l.acquire()
    time.sleep(5)
    li.append(5)
    print(li)
    l.release()


def b():
    li.append(6)
    print(li)


if __name__ == '__main__':
    l = Lock()
    t1 = Thread(target=a, args=(l,))
    t2 = Thread(target=b)
    t1.start()
    t2.start()
