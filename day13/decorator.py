# -*- coding: utf-8 -*-
def log(time):
    def top(func):
        def inner(*s, **ss):
            print(time)
            return func(*s, **ss)
        return inner
    return top


@log('17.11')
def date(x):
    print(x)


date('2018/4/25')
