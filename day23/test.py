# -*- coding: utf-8 -*-

# class People(object):
#
#    def __init__(self):
#        print("__init__")
#
#    # def __new__(cls, *args, **kwargs):
#    #     print("__new__")
#    #     return object.__new__(cls, *args, **kwargs)
#
# People()
# class A(object):
#    def __init__(self):
#        print('A')
#        super(A, self).__init__()
#
# class B(object):
#    def __init__(self):
#        print('B')
#        super(B, self).__init__()
#
# class C(A):
#    def __init__(self):
#        print('C')
#        super(C, self).__init__()
#
# class D(A):
#    def __init__(self):
#        print('D')
#        super(D, self).__init__()
#
# class E(B, C):
#    def __init__(self):
#        print('E')
#        super(E, self).__init__()
#
# class F(B,C, D ):
#    def __init__(self):
#        print('F')
#        super(F, self).__init__()
#
# class G(D, B):
#    def __init__(self):
#        print('G')
#        super(G, self).__init__()
#
# if __name__ == '__main__':
#    g = G()
#    f = F()
#    print(F.__mro__)
# 一切皆文件
import abc  # 利用abc模块实现抽象类


class All_file(metaclass=abc.ABCMeta):
    all_type = 'file'

    @abc.abstractmethod  # 定义抽象方法，无需实现功能
    def read(self):
        '子类必须定义读功能'
        pass

    @abc.abstractmethod  # 定义抽象方法，无需实现功能
    def write(self):
        '子类必须定义写功能'
        pass


# class Txt(All_file):
#     pass
#
# t1=Txt() #报错,子类没有定义抽象方法

class Txt(All_file):  # 子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('文本数据的读取方法')

    def write(self):
        print('文本数据的读取方法')


class Sata(All_file):  # 子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('硬盘数据的读取方法')

    def write(self):
        print('硬盘数据的读取方法')


class Process(All_file):  # 子类继承抽象类，但是必须定义read和write方法
    def read(self):
        print('进程数据的读取方法')

    def write(self):
        print('进程数据的读取方法')


wenbenwenjian = Txt()

yingpanwenjian = Sata()

jinchengwenjian = Process()

# 这样大家都是被归一化了,也就是一切皆文件的思想
wenbenwenjian.read()
yingpanwenjian.write()
jinchengwenjian.read()

print(wenbenwenjian.all_type)
print(yingpanwenjian.all_type)
print(jinchengwenjian.all_type)
