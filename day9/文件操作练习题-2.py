# -*- coding: utf-8 -*-

# 练习题2 —— 模拟登陆：
#
# 用户输入帐号密码进行登陆
# 用户信息保存在文件内
# 用户密码输入错误三次后锁定用户，下次再登录，检测到是这个用户也登录不了
import sys


data = open('User_Data.txt', 'r+', encoding='utf-8')
data_line = data.readlines()
data.close()
lock_name = open('Locklist.txt','r+',encoding='utf-8')

lock_line = lock_name.readlines()
count = 0
while count < 3:
    count += 1
    name = input("please input your user name：")
    for line in lock_line:
        if name == line.strip('\n'):
            print('This account have been locked!')
            sys.exit()

    for user_line in data_line:
        (user,key) = user_line.strip('\n').split(',')

        if name == user:
            password = input('please input your password：')
            if password == key:
                print("Welcome to the new world!")
                sys.exit()
            else:  # 输入密码错误以后的结果
                print('you have inputed a wrong password,%s times remaining'%(3-count))
                if count == 3:  # 如果错误次数已经到了三次,记录违规的用户名，并退出程序
                    lock_name.write(user + '\n')
                    lock_name.close()
                    sys.exit()
                break

    else:
        print('you have inputed a wrong username,%s times remaining!'%(3-count))
        continue