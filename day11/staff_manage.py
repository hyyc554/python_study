# -*- coding: utf-8 -*-

import sys
import os
# 读取用户信息
staff_file = open('staff_table.txt', 'r+',encoding='utf-8')
staff_lines = staff_file.readlines()
staff_data_list = []


def print_count(z):
    print('本次共对%s条数据进行了处理'%z)


def get_age(age):  # 用来获取用户所有的信息表，并返回值
    print('所有的大于%s的员工信息如下：'%age)
    target_age_staff = {}
    count = 0
    for staff_line in staff_lines:
        staff_data_list = staff_line.strip('\n').split(',')
        if int(staff_data_list[2]) > age:
            target_age_staff[staff_data_list[1]] = staff_data_list[2]
            count += 1
    print_count(count)
    for key, value in target_age_staff.items():
        print('姓名：%s    年龄：%s' % (key, value))


def seek_dept(xx):  # 部门查找
    count = 0
    for staff_line in staff_lines:
        staff_data_list = staff_line.strip('\n').split(',')
        if staff_data_list[4] == xx:
            print('ID:%s姓名：%s年龄;%sPHONE:%s部门：%s入职日期：%s'%(staff_data_list[0],staff_data_list[1],staff_data_list[2],
                  staff_data_list[3],staff_data_list[4],staff_data_list[5]))
            count += 1
    print_count(count)


def seek_date(date):
    count = 0
    for staff_line in staff_lines:
        staff_data_list = staff_line.strip('\n').split(',')
        if date in staff_data_list[5]:
            print('ID:%s,姓名：%s,年龄;%s,PHONE:%s,部门：%s,入职日期：%s'%(staff_data_list[0], staff_data_list[1], staff_data_list[2],
                  staff_data_list[3], staff_data_list[4], staff_data_list[5]))
            count += 1
    print_count(count)


while True:
    print('''
------欢迎进入员工管理界面------
1.查找某年龄段的员工
2.查找某一部门的员工
3.查找某年入职的员工
4.添加员工
5.删除某员工
6.修改员工信息表中的某一部门的名称
7.修改某个用户的年龄
8.退出程序''')
    choice = int(input('选择你要行使的功能：').strip())
    if choice == 1:
        target_age = int(input('请输入目标年龄，将搜索大于此年龄的所有员工：').strip())
        get_age(target_age)

    elif choice == 2:
        target_dept = input('请输入目标:').strip()
        seek_dept(target_dept)
    elif choice == 3:
        target_date = input('请输入目标:').strip()
        seek_date(target_date)
    elif choice == 4:
        new_stuff = input('请以‘Alex Li,22,13651054608,IT,2013-04-01’为模板输入员工信息：').strip().split(',')
        for staff_line in staff_lines:
            staff_data_list = staff_line.strip('\n').split(',')
            if new_stuff[2] in staff_data_list:
                print('该用户已存在')
                break
        else:
            new_id = str(len(staff_lines) + 1)
            new_stuff.insert(0, new_id)
            b = ','.join(new_stuff)
            staff_file.write('\n'+b)
            staff_file.close()
    elif choice == 5:
        del_id = input('请输入要删除的员工的ID：')
        new_stuff_file = open("staff_table.txt", "w", encoding="utf-8")
        for staff_line in staff_lines:
            staff_data_list = staff_line.strip('\n').split(',')
            if del_id == staff_data_list[0]:
                continue
            new_stuff_file.write(staff_line)
    elif choice == 6:
        old_dept = input('请输入你所要修改的部门：').strip()
        new_dept = input('请输入新的部门名称：').strip()
        new_stuff_file = open("staff_table.txt", "w", encoding="utf-8")
        count = 0
        for staff_line in staff_lines:
            staff_data_list = staff_line.strip('\n').split(',')
            if old_dept == staff_data_list[4]:
                new_dept_line = staff_line.replace(old_dept,new_dept)
                new_stuff_file.write(new_dept_line)
                count += 1
            else:
                new_stuff_file.write(staff_line)
        new_stuff_file.close()
        print_count(count)
    elif choice == 7:
        old_dept = input('请输入你所要修改的用户：').strip()
        new_dept = input('请输入新的年龄：').strip()
        new_stuff_file = open("staff_table.txt", "w", encoding="utf-8")
        count = 0
        for staff_line in staff_lines:
            staff_data_list = staff_line.strip('\n').split(',')
            if old_dept == staff_data_list[1]:
                new_dept_line = staff_line.replace(staff_data_list[2],new_dept)
                new_stuff_file.write(new_dept_line)
                count += 1
            else:
                new_stuff_file.write(staff_line)
        new_stuff_file.close()
        print_count(count)
    else:
        sys.exit()