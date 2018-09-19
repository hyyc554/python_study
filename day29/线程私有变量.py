# -*- coding: utf-8 -*-
import threading
import time
import random

threading_namespace = threading.local()  # 命名空间


def print_name():
    thread_name = threading.current_thread().getName()
    name = threading_namespace.name  # 获取变量
    print('{}  {}'.format(thread_name, name))


def my_func(name):
    threading_namespace.name = name  # 设置变量

    for i in range(4):
        time.sleep(random.randrange(1, 7))
        print_name()


if __name__ == '__main__':

    names = ['alex1','alex2','alex3','alex4','alex5','alex6','alex7','alex8','alex9','alex10']

    threads = []
    for n in names:
        threads.append(threading.Thread(target=my_func, args=(n,)))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

