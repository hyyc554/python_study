# # -*- coding: utf-8 -*-
import os
with open('123.txt','r',encoding='utf-8') as fp:
    f = fp.read()
with open('123-1.txt','w',encoding='utf-8') as c:
    b = f.replace('：', '')
    c.write(b)
os.replace('123-1.txt','123.txt')


print(b)
# # print(a)
#     a = fp.readlines()
# a.remove(a[1])
# print(a)
# new
# # b= []
# # count = 0
# # for line in a:
# #     count+=1
# #     newline = line
# #     if count == 1:
# #         continue
# #     b.append(newline)
# # #
# #
# # print(b)
#
# # import time
# #
# #
# # def add(x, y):
# #     time.sleep(3)
# #     return x + y
# #
# # def new_time(func):
# #     def inner(*x,**y):
# #         start_time = time.time()
# #         ret = func(*x,**y)
# #         end_time = time.time()
# #         total_time = end_time - start_time
# #         print(total_time)
# #         print(ret)
# #     return inner
# #
# def test():
#     print(luffy)
#     luffy = 'hello'
#
#
# luffy = "the king of sea."

#
# test()
# #
# #
#
# # li = [1, 2, 3, 5, 5, 6, 7, 8, 9, 9, 8, 3] 利用生成器，写一个所有数值乘以2的功能。（编程）
# li = [1, 2, 3, 5, 5, 6, 7, 8, 9, 9, 8, 3]
# len(li)
# a = (li[x]*2 for x in range(0,len(li)))
#
# for b in a:
#     print(b)
#
# 字符串“Luffy”，将小写字母全部转换成大写字母，将大写字幕转换成小写字幕，然后输出到一个磁盘文件"test"中保存。(编程)
import string
a ='Luffy'
c = ''
count = 0
for b in a :
    if b.islower():
        b= b.upper()
    else:
        b = b.lower()
    c = c +b
print(c)






#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# num = 20
#
#
# def show_num(x=num):
#     print(x)
#
#
# show_num()
# num = 30
# show_num()
# 有列表 li = ['alex', 'egon', 'smith', 'pizza', 'alen'], 请以列表中每个元素的第二个字母倒序排序；
li = ['alex', 'egon', 'smith', 'pizza', 'alen']
sorted(li,key=lambda x:x[1],reverse =True)