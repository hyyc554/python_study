# -*- coding: utf-8 -*-


# 用户信息保存在UserList.txt中，格式为XX,XXXXXX,XXXXX用逗号分隔
# 被锁定的用名保存在LockList.txt中
import sys,os
locked_user = open('LockList.txt','r+')
locked_name = locked_user.readlines()
with open('UserList.txt', 'r') as user_file:
    user_list = user_file.readlines()
count = 0
while count < 3:
    username = input("请输入你的用户名：")
    for locked_line in locked_name:
        if username == locked_line.strip('\n'):
            print('该用户已被锁定')
            sys.exit()

    for user_line in user_list:
        data_list = user_line.strip('\n').split(',')
        print(data_list)
        user = data_list[0]
        passkey = data_list[1]
        if user == username:
            password = input("请输入你的密码：")
            if password == passkey:
                print("欢迎您的到来！")

                # 进入用户信息修改功能

                def print_data():
                    ifo = '''-------welcome to my city------
                    name:   %s
                    age :   %s
                    job :   %s
                    Dept:   %s
                    Phone:  %s
                    ''' % (data_list[0], data_list[2], data_list[3], data_list[4], data_list[5])
                    return print(ifo)
                def change_data():
                    f_name = 'UserList.txt'
                    f_new_name = "%s.new" % f_name
                    f = open(f_name, 'r+', encoding="utf-8")

                    f_new = open(f_new_name,'w+',encoding='utf-8')
                    current_data = [data_list[0],data_list[2],data_list[3],data_list[4],data_list[5]]
                    choice_list = enumerate(current_data)
                    print(choice_list)
                    num = int(input('请输入你所需要更改的项目序号：'))
                    new_str = input('请输入你的新信息：')
                    current_data[num] = new_str  # 进行内容的替换
                    current_data.insert(1,data_list[1])
                    map(str,current_data)
                    new_str = ','.join(current_data)

                    for line in f.readlines():
                        old_list = line.strip('\n').split(',')
                        old_line = line.strip('\n')
                        current_user = old_list[0]
                        if current_user == username:
                            new_line = line.replace(old_line,new_str)
                        else:
                            new_line = line
                        f_new.write(new_line)
                    f.close()
                    f_new.close()

                    os.replace(f_new_name, f_name)
                # 开始进入修改程序
                while True:
                    print('''-----欢迎来的新世界-------
                    1.修改个人信息
                    2.打印个人信息
                    3.修改密码
                    ''')
                    choice = int(input('请输入你的选择：'))
                    if choice == 1:
                        change_data()
                        continue
                    elif choice == 2:
                        print_data()
                        continue
                    elif choice == 3:
                        continue
                    else:
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
