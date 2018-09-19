# -*- coding: utf-8 -*-

#item系列
# class Foo:  #dict
#     def __init__(self,name):
#         self.name = name
#
#     def __getitem__(self, item):
#         return self.__dict__[item]
#
#     def __setitem__(self, key, value):
#         self.__dict__[key] = value
#
#     def __delitem__(self, key):
#         del self.__dict__[key]
#
# obj = Foo('yc')
#
# print(obj['name'])
#
# obj['age']= 18
# print(obj.__dict__)
#
# del obj['name']
# print(obj.__dict__)