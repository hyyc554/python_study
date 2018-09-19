#!/usr/bin/env:python
# -*- coding: utf-8 -*-
#.__anthour__:."Huang YC"
#.date:.2018/4/13

# -*- coding: utf-8 -*-
import sys
import os


# 读取用户信息
with open('staff_table.txt', 'r') as staff_file:
    staff_lines = staff_file.readlines()
    staff_file.close()


# def target_function(num):

staff_data_list = []


def for_list(func):
    for staff_line in staff_lines:
        staff_data_list = staff_line.strip('\n').split(',')
        func( )
    return True


def update(new_phone):
    if new_phone in staff_data_list:
        print('该用户已存在')
        return False
    update(new_stuff[2])


#查找


flag = True
while flag:
    print('''
------欢迎进入员工管理界面------
1.查找某年龄段的员工
2.查找某一部门的员工
3.查找某年入职的员工
4.添加员工
5.删除某员工
6.修改员工信息
6.退出程序''')
    choice = int(input('选择你要行使的功能：').strip())
    if choice == 1:
        pass


    elif choice == 4:
        new_stuff = input('请以‘Alex Li,22,13651054608,IT,2013-04-01’为模板输入员工信息：').strip().split(',')























