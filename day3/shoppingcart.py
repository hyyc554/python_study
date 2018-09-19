#_*_coding:utf-8_*_


#第一部分的用户登陆程序
#用户名与密码保存在UserList.txt中，格式为XX:XXXXXX
#被锁定的用名保存在LockList.txt中

import sys,os

count = 0
while count < 3:
    username = input("请输入你的用户名：")
    locked_user = open('LockList.txt','r+')
    locked_name = locked_user.readlines()
    for locked_line in locked_name:
        if username == locked_line.strip('\n'):
            print('该用户已被锁定')
            sys.exit()

    user_numb = 1
    for user_line in user_list:
        user_numb += 1
        user_data = user_line.strip('\n').split(':')
        user = user_data[0]
        passkey = user_data[1]
        if user == username:
            password = input("请输入你的密码：")
            if password == passkey:
                print("欢迎您的到来！")


                #进入到购物界面了
                #判断用户是否之前存在购物行为,并完成用户余额的初始赋值
                with open('ShoppingCart.txt', 'r', encoding='utf-8') as s, \
                        open('balance.txt', 'r', encoding='utf-8') as b:
                    goos_in_cart = s.read()
                    old_balance = int(b.read())
                if old_balance == 0:#如果是第一次登陆将采集用户的工资作为可用余额
                        balance = int(input("请输入你的工资："))
                else:#如果余额不为初始化值，将使用上次购物所剩余额，作为本次购物的可用余额
                    balance = old_balance
                    print('#################购物清单###############')
                    print('购物清单：%s' % goos_in_cart, '\033[1;32;43m 剩余金额:%s \033[0m!' % old_balance)

                # 购物列表的输出
                goods = [
                    {"name": "电脑", "price": 1999},
                    {"name": "鼠标", "price": 10},
                    {"name": "游艇", "price": 20},
                    {"name": "美女", "price": 998},
                ]
                shopping_cart = []
                index = 0
                print('---------商品列表----------')
                for p in goods:
                    print("%s. %s    %s" % (index, p['name'], p['price']))
                    index += 1

                # 请用户做出选择
                print("请根据商品编号选购商品")
                exit_flag = False
                while not exit_flag:
                    print('你需要其他商品吗？')
                    choice = input("商品编号：")
                    if choice.isdigit():
                        choice = int(choice)
                        balance = int(balance) - int(goods[choice]['price'])

                        if balance > 0:
                            if choice >= 0 and choice < len(goods):
                                shopping_cart.append(goods[choice]['name'])
                                print(" \033[1;32;43m %s 加入购物车！ \033[0m" % (goods[choice]['name']))
                            else:
                                print("商品不存在")
                        else:
                            print('余额不足，将退出程序')
                            exit_flag = True

                    else:#用户选择退出
                        new_balance = balance
                        if len(shopping_cart) > 0:#如果买了东西，就保存余额，以及购物车
                            print("-------你已购买以下商品-------")
                            for p in shopping_cart:
                                print(p)
                                with open("ShoppingCart.txt", 'a', encoding='utf-8') as f:
                                    f.write('商品：' + p[0] +'\n')
                            print("\033[1;32;43m 您的余额为：%s  \033[0m"%new_balance)
                            with open('balance.txt', 'w', encoding='utf-8') as f:
                                f.write(str(new_balance))
                        sys.exit()
                        #购物车程序的末尾

            else:#回到了用户登陆的分支
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