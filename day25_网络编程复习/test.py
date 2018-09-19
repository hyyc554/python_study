# -*- coding: utf-8 -*-

# a = 10
# b = 20


def f(a):
    c = a + b
    print(id(a))
    print(locals())
    return c


f(a)
# print(id(a))
# print(globals())
