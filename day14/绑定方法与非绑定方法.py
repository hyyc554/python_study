# -*- coding: utf-8 -*-

'''
在类内部定义的函数分为两大类：
一绑定方法:绑定给谁，就应该由谁调用。谁调用就会把谁当做第一个参数自动传入
    1.绑定到类的方法：在类内定义的没有被任何装饰器修饰的

    2.绑定到对象的方法：在类内部定义的，被装饰器classmethod修饰的方法

二.非绑定方法：没有自动传值,就是类中的一个普通工具
    不与任何对象或类绑定

'''

class Foo:
    def __init__(self,name):
        self.name = name

    def tell(self):
        print(self.name)

    @classmethod
    def func(cls):
        print(cls)

    @staticmethod
    def func1(x,y):
        print(x+y)

t= Foo('yc')
# print(Foo.tell)
# Foo.tell(t)

# print(t.tell)

# t.tell()

# print(Foo.func)
# Foo.func()

Foo.func1(1,3)
t.func1(2,4)
















