#!/usr/bin/env:python
# -*- coding: utf-8 -*-
#.__anthour__:."Huang YC"
#.date:.2018/4/14


import sys
import os
# 读取用户信息

def where(content,where):
    if content == 1:
        where


def seek(file,content,where):
    with open(file,'r') as f:
        r=f.readline()
        line=r.strip('\n').split(',')
        if line[2] >where:
            print(line[1],line[2])
        while r:
            r=f.readline()
            line.append(r.strip('\n').split(','))


def get_age(age):  # 用来获取用户所有的信息表，并返回值
    print('所有的大于%s的员工信息如下：'%age)
    target_age_staff = {}
    for staff_line in staff_lines:
        staff_data_list = staff_line.strip('\n').split(',')
        if int(staff_data_list[2]) > age:
            target_age_staff[staff_data_list[1]] = staff_data_list[2]
    for key, value in target_age_staff.items():
        print('姓名：%s    年龄：%s' % (key, value))
    return len(target_age_staff)  # 返回查询次数