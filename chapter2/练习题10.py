# -*- coding: utf-8 -*-

#写一个6位随机验证码程序（使用random模块),要求验证码中至少包含一个数字、一个小写字母、一个大写字母.

import random
import string


def indentiying_code(): #  定义一个验证码的函数
    identifying_code = ''.join(random.sample(string.ascii_lowercase + string.ascii_uppercase + string.digits, 6))

    print('identifying code:', identifying_code)
    input_code = input('please input the identifying code:').strip()

    if input_code == identifying_code:
        print('OK')
    else:
        print('not ok')

indentiying_code()