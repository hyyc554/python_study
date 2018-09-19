# -*- coding: utf-8 -*-

"""
练习1：定义MySQL类

要求：

1.对象有id、host、port三个属性

2.定义工具create_id，在实例化时为每个对象随机生成id，保证id唯一

3.提供两种实例化方式，方式一：用户传入host和port 方式二：从配置文件中读取host和port进行实例化

4.为对象定制方法，save和get_obj_by_id，save能自动将对象序列化到文件中，文件路径为配置文件中DB_PATH,
文件名为id号，保存之前验证对象是否已经存在，若存在则抛出异常，;get_obj_by_id方法用来从文件中反序列化出对象
"""
import time
import pickle
import hashlib


class MySQL:
    @staticmethod
    def create_id():
        idd = hashlib.md5()
        idd.update(str(time.time()).encode('utf-8'))
        return idd.hexdigest()

    def __init__(self, *args):
        self.id = MySQL.create_id()
        if args:
            self.host, self.port = args
        else:
            self.host, self.port = (231231, 12212)


a = MySQL()
print(a.id, a.host, a.port)
