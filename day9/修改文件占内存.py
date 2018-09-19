#!/usr/bin/env:python
# -*- coding: utf-8 -*-
#.__anthour__:."Huang YC"
#.date:.2018/4/10

f = open('fix_test.txt','r+',encoding='utf-8')  # 打开文件
old_str = '黄咏驰'
new_str = '关谷神奇'
data = f.read() # 读取原始文件中的所有数据到内存
print(data,type(data))
f.seek(0)
if old_str in data:
    data = data.replace(old_str,new_str)
f.write(data)
f.close()