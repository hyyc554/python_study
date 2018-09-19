# -*- coding: utf-8 -*-


# 请写一个包含10个线程的程序，主线程必须等待每一个子
# 线程执行完成之后才结束执行，
# 每一个子线程执行的时候都需要打印当前线程名、当前活跃线程数量；

# from threading import Thread, active_count
# import time
#
#
# def run():
#     print('running')
#     time.sleep(10)
#
#
# for i in range(10):
#     t = Thread(target=run, args=())
#     t.start()
#
#     print(t.name, active_count())

# from multiprocessing import Process, Queue
# import time, random, os
#
#
# def consumer(q, name):
#     while True:
#         res = q.get()
#         if res is None: break
#         time.sleep(random.randint(1, 3))
#         print('%s 吃 %s' % (name, res))
#
#
# def producer(q, name, food):
#     for i in range(3):
#         time.sleep(random.randint(1, 3))
#         res = '%s%s' % (food, i)
#         q.put(res)
#         print('%s 生产了 %s' % (name, res))
#
#
# if __name__ == '__main__':
#     q = Queue()
#     # 生产者们:即厨师们
#     p1 = Process(target=producer, args=(q, 'egon', '包子'))
#
#     # 消费者们:即吃货们
#     c1 = Process(target=consumer, args=(q, 'alex'))
#
#     # 开始
#     p1.start()
#     c1.start()
#
#     p1.join()
#     q.put(None)
#     print('主')

# from threading import Thread,active_count
# from queue import Queue
# import time
#
# def run(q):
#     num= q.get()
#     print(num,'running')
#     time.sleep(10)
# q = Queue(5)
#
#
# for i in range(10):
#     t = Thread(target=run, args=(q,))
# num =0
# while True:
#     num+=1
#     q.put(num)

from threading import Thread
# from threading import currentThread
# from concurrent.futures import ThreadPoolExecutor
# import time
# import random
#
#
# def task():
#     print(currentThread().getName())
#     time.sleep(random.randint(1, 3))
#
#
# if __name__ == '__main__':
#     pool = ThreadPoolExecutor(5)
#     for i in range(10):
#         pool.submit(task)

# from threading import Thread, active_count
# import time
#
#
# def run():
#     print('running')
#     time.sleep(10)
#
#
# print('main sleep')
# time.sleep(10)
# print('main weak')
# for i in range(10):
#     t = Thread(target=run, args=())
#     t.start()
#     print(t.name, active_count())


from gevent import monkey;monkey.patch_all()
import gevent

from queue import Queue
import time, random, os


def consumer(q, name):
    while True:

        res = q.get()
        if res is None:
            break
        time.sleep(random.randint(1, 3))
        print('\033[43m%s 吃 %s\033[0m' % (name, res))



def producer(q, name, food):
    for i in range(3):
        time.sleep(random.randint(1, 3))
        res = '%s%s' % (food, i)
        q.put(res)
        print('\033[45m%s 生产了 %s\033[0m' % (name, res))


if __name__ == '__main__':
    q = Queue()

    # 生产者们:即厨师们
    p1 = gevent.spawn(producer, q=q, name='egon', food='包子')

    # 消费者们:即吃货们
    c1 = gevent.spawn(consumer, q=q, name='alex')
    p1.join()
    q.put(None)
    c1.join()
    print('main')



# from gevent import monkey;monkey.patch_all()
# import gevent
# import time
# def eat():
#     print('eat food 1')
#     time.sleep(2)
#     print('eat food 2')
#
# def play():
#     print('play 1')
#     time.sleep(1)
#     print('play 2')
#
# g1=gevent.spawn(eat)
# g2=gevent.spawn(play)
# gevent.joinall([g1,g2])
# print('主')