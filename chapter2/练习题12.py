# -*- coding: utf-8 -*-

# 1. 用户名为json文件名，密码为 password。
# 2. 判断是否过期，与expire_date进行对比。
# 3. 登陆成功后，打印“登陆成功”，三次登陆失败，status值改为1，并且锁定账号。
import json, os, hashlib


def hash_mod(avrg):
    md5_key = hashlib.md5()
    json_str = json.dumps(avrg)
    md5_key.update(json_str.encode('utf-8'))
    key = md5_key.hexdigest()
    return key


def get_data(x):  # 用来获取用户所有的信息表，并返回值
    file_name = '%s.json' % x
    with open(file_name, 'r') as user_file:
        userdata = json.load(user_file)
        user_file.close()
    password = hash_mod(userdata)
    if userdata["status"]:
        print('账户已经被锁定')
        return False

    count = 0
    while count < 3:
        user_key = input('请输入您的密码：').strip()
        userdata['password'] = user_key
        user_word = hash_mod(userdata)

        if user_word == password:
            print('密码正确')
            return True
        else:
            count += 1
            print("输入错误%s次，三次后将退出，并锁定用户！" % count)
            if count == 3:
                userdata["status"] = 1
                new_file_name = '%s_new.json'%file_name
                new_user_file = open(new_file_name,'w',encoding='utf-8')
                new_user_file.write(json.dumps(userdata))
                new_user_file.close()
                os.replace(new_file_name,file_name)


user_name = input('请输入用户名：').strip()
get_data(user_name)
