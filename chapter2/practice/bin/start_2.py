# -*- coding: utf-8 -*-
import json, os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

user_status = False #用户登录了就把这个改成True


def log_func(avrgs):
    import logging
    #  console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    #  file handler
    fh = logging.FileHandler('../logs/bank.log',encoding='utf-8')
    #  fh.setLevel(logging.WARNING)

    #  formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #  bind formatter to ch
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger = logging.getLogger("bank")
    logger.setLevel(logging.DEBUG) #  logger 优先级高于其它输出途径的

    #  add handler to logger instance
    logger.addHandler(ch)
    logger.addHandler(fh)

    logger.info(avrgs)


def login(func): #把要执行的模块从这里传进来
    def inner(*args, **kw):
        from account import access
        access.get_in(BASE_DIR)
        return func(*args, **kw)
    return inner


@login
def draw_func():  # 提现函数
    from core import withdraw
    withdraw.with_draw(user_data)
    rewrite(user_path, user_data)

@login
def transfer_accounts():  # 转账函数

    tesla_account['profit'] += 750000
    user_data['balance'] -= (750000 * 1.05)
    print(user_data['balance'])
    rewrite(user_path, user_data)
    rewrite(shopping_path, tesla_account)




def rewrite(file_path,file_data):
    new_file_name = '%s_new.json' % file_path
    old_file_name = file_path.split('/')[-1]
    new_file = open('../account/%s'%new_file_name, 'w', encoding='utf-8')
    new_file.write(json.dumps(file_data))
    new_file.close()
    os.replace('../account/%s'%new_file_name,'../account/%s'%old_file_name)

print('''
--------- Luffy Bank ---------
1. 账户信息
2.转账
3.提现
''')
user_path = "../account/luffy.json"

user_data = json.load(open(user_path, 'r'))

shopping_path = "../account/tesla.json"
tesla_account = json.load(open(shopping_path,'r'))

choice = input('请输入你的选择：').strip()
if choice.isdigit():
    choice = int(choice)
    if choice == 1:
        ifo = '''
该账户当余额:     %d
该账户信用额度：   %d
'''%(user_data['balance'],user_data['credit_line'])
        print(ifo)
    elif choice == 2:
        transfer_accounts()
    elif choice == 3:
        draw_func()
        log_func('完成了一次提现')

else:
    print('您的输入有误！')
