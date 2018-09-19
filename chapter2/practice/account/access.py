# -*- coding: utf-8 -*-

# 1. 用户名为json文件名，密码为 password。
# 2. 登陆成功后，打印“登陆成功”，三次登陆失败，status值改为1，并且锁定账号。
import json, os,hashlib

def hash_mod(avrg):
    md5_key = hashlib.md5()
    json_str = json.dumps(avrg)
    md5_key.update(json_str.encode('utf-8'))
    key = md5_key.hexdigest()
    return key


def get_in(path):  #  用户登陆函数
    user_name = input('请输入用户名：').strip()
    file_name = '%s.json'%user_name
    with open('%s/account/%s'%(path,file_name), 'r') as user_file:
        userdata = json.load(user_file)
        user_file.close()
    password = hash_mod(userdata)
    if userdata["status"]:
        print('账户已经被锁定')
        return False

    count = 0
    while count < 3:
        user_key = input('\033[1;31;40m请输入您的密码>>>\033[0m').strip()
        userdata['password'] = user_key
        user_word = hash_mod(userdata)

        if user_word == password:
            print('\033[1;32;40m密码正确\033[0m')
            return True
        else:
            count += 1
            print("\033[1;36;46m输入错误%s次，三次后将退出，并锁定用户！\033[0m" % count)
            if count == 3:
                userdata["status"] = 1
                new_file_name = '%s_new.json'%file_name
                new_user_file = open('%saccount//%s'%(path,new_file_name),'w',encoding='utf-8')
                new_user_file.write(json.dumps(userdata))
                new_user_file.close()
                os.replace('%saccount//%s'%(path,new_file_name),'%s/account/%s'%(path,file_name))
