# -*- coding: utf-8 -*-

# 用户信息保存在UserList.txt中，格式为XX,XXXXXX,XXXXX用逗号分隔
# 被锁定的用名保存在LockList.txt中

import sys
import os
locked_user = open('LockList.txt','r+')
locked_name = locked_user.readlines()


def get_data(x):  # 用来获取用户所有的信息表，并返回值
    with open('UserList.txt', 'r') as user_file:
        user_list = user_file.readlines()
        user_file.close()
        for user_line in user_list:
            data_list = user_line.strip('\n').split(',')
            user = data_list[0]
            if user == x:
                return data_list
        else:
            return False


def print_data():  # 用来打印用户信息的工具
    data_list = get_data(username)
    ifo = '''-------welcome to my city------
    name:   %s
    age :   %s
    job :   %s
    Dept:   %s
    Phone:  %s
    ''' % (data_list[0], data_list[2], data_list[3], data_list[4], data_list[5])
    return print(ifo)


def change_data(x):  # 用来修改用户信息的工具，包括修改密码
    data_list = get_data(username)
    f_name = 'UserList.txt'
    f_new_name = "%s.new" % f_name
    f = open(f_name, 'r+', encoding="utf-8")
    f_new = open(f_new_name, 'w+', encoding='utf-8')

    current_data = [data_list[0], data_list[2], data_list[3], data_list[4], data_list[5]]
    if x == 1:
        for index,item in enumerate(current_data):
            print(index,item)
        num = int(input('请输入你所需要更改的项目序号：'))
        new_str = input('请输入你的新信息：')
        current_data[num] = new_str  # 进行内容的替换
        current_data.insert(1, data_list[1])

    else:
        num = 1
        new_str = input('请输入你的新信息：')
        current_data.insert(1,new_str)
    map(str, current_data)
    str_line = ','.join(current_data)

    for line in f.readlines():
        old_list = line.strip('\n').split(',')
        old_line = line.strip('\n')
        current_user = old_list[0]
        if current_user == username:
            new_line = line.replace(old_line, str_line)
        else:
            new_line = line
        f_new.write(new_line)
    f.close()
    f_new.close()
    os.replace(f_new_name, f_name)


count = 0
while count < 3:
    username = input("请输入你的用户名：")
    for locked_line in locked_name:
        if username == locked_line.strip('\n'):
            print('该用户已被锁定')
            sys.exit()
    data_list = get_data(username)

    if data_list:
        passkey = data_list[1]
        password = input("请输入你的密码：")
        if password == passkey:
            print("欢迎您的到来！")

            # 进入用户信息修改功能
            while True:
                print('''
-------欢迎来的新世界-------
1.修改个人信息
2.打印个人信息
3.修改密码
4.退出程序
                ''')
                choice = int(input('请输入你的选择：'))
                if choice == 1:
                    change_data(1)
                    continue
                elif choice == 2:
                    print_data()
                    continue
                elif choice == 3:
                    change_data(3)
                    continue
                else:  # 输入其他选项将退出程序
                    sys.exit()

            else:
                count += 1
                print("输入错误%s次，三次后将退出，并锁定用户！"%count)
                if count == 3:
                    locked_user.write(username + '\n')
                    locked_user.close()
                    sys.exit()
                break
    else:
        print("该用户不存在")
        count += 1
        continue