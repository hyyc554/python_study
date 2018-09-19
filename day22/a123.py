# -*- coding: utf-8 -*-
def log(func):
    def wrapper(*args, **kw):
        print('log')
        func(*args, **kw)
    return wrapper
@log
def r():
    print('ok')
    return True

