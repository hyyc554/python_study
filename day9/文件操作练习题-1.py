#!/usr/bin/env:python
# -*- coding: utf-8 -*-


# 练习题1 —— 全局替换程序：
#
# 写一个脚本，允许用户按以下方式执行时，即可以对指定文件内容进行全局替换
#
#   `python your_script.py old_str new_str filename`
# 替换完毕后打印替换了多少处内容
import os
old_str = input("请输入要被替换的内容:").strip()
new_str = input("请输入替换内容：").strip()
file_name = input("请输入你要更改文件得名称：").strip()

file_name_new = '%s.new'%file_name
f = open(file_name,"r+",encoding='utf-8')
f_new = open(file_name_new,'w+',encoding='utf-8')


for line in f:
    if old_str in line:
        line = line.replace(old_str,new_str)
    f_new.write(line)

f.close()
f_new.close()

os.replace(file_name_new,file_name)