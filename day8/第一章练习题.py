#!/usr/bin/env:python
# -*- coding: utf-8 -*-
#.__anthour__:."Huang YC"
#.date:.2018/4/4

# 1、请用代码实现：利用下划线将列表的每一个元素拼接成字符串，li＝['alex', 'eric', 'rain']
# li = ['alex', 'eric', 'rain']
# a = '_'.join(li)
# print(a)
#
# 2、查找列表中元素，移除每个元素的空格，并查找以a或A开头并且以c结尾的所有元素。
#
# li = ["alec", " aric", "Alex", "Tony", "rain"]
#
# tu = ("alec", " aric", "Alex", "Tony", "rain")
#
# dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}
# li = ["alec", " aric", " Alex", " Tony", " rain"]
#
#
# for i in range(len(li)):
#
#     li[i] = li[i].strip()
#     if li[i][0] == 'a'or li[i][0] =='A':
#         if li[i][-1] =='c':
#              print(li[i])
#
# print(li)
#
#
# tu = ("alec", " aric", "Alex", "Tony", "rain")
#
# dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}
#
# 3、写代码，有如下列表，按照要求实现每一个功能
#
# # li＝['alex', 'eric', 'rain']
# li = ['alex', 'eric', 'rain']
#
# # 计算列表长度并输出
# print(len(li))
# # 列表中追加元素“seven”，并输出添加后的列表
# li.append('senve')
# print(li)
#
# # 请在列表的第1个位置插入元素“Tony”，并输出添加后的列表
# li.insert(0,"tony")
# print(li)
# # 请修改列表第2个位置的元素为“Kelly”，并输出修改后的列表
# # li.insert(1,"Kelly")
# # li.pop(2)
# # print(li)太智障了
# li[1] = "Kelly"
#
#
# # 请删除列表中的元素“eric”，并输出修改后的列表
# li.remove('eric')
# print(li)
# # 请删除列表中的第2个元素，并输出删除的元素的值和删除元素后的列表
# a=li.pop(1)
# print(a,li)
# # 请删除列表中的第3个元素，并输出删除元素后的列表
# del li[2]
# print(li)
# # 请删除列表中的第2至4个元素，并输出删除元素后的列表
#
# # 请将列表所有的元素反转，并输出反转后的列表
# li.reverse()
# print(li)
# li = ['tony', 'alex', 'eric', 'rain', 'senve']
# # 请使用for、len、range输出列表的索引
# for i in range(len(li)):
#     print(i)
#
# # 请使用enumrate输出列表元素和序号（序号从100开始）
# for i,key in enumerate(li):
#     print(100+i,key)
#
# # # 请使用for循环输出列表的所有元素
# # for key in li :
# #     print(key)
# # 4、写代码，有如下列表，请按照功能要求实现每一个功能
# #
# # li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]
# #
# # 请根据索引输出“Kelly”
# li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]
# print(li[2][1][1])
# # 请使用索引找到'all'元素并将其修改为“ALL”，如：li[0][1][9]...
# li[2][2] = 'ALL'
# print(li)
# # 5、写代码，有如下元组，请按照功能要求实现每一个功能
# #
# # tu＝('alex', 'eric', 'rain')
# #
# # 计算元组长度并输出
# tu=('alex', 'eric', 'rain')
# print(len(tu))
# # 获取元组的第2个元素，并输出
# print(tu[1])
# # 获取元组的第1-2个元素，并输出
# print(tu[0:2])
# # 请使用for输出元组的元素
# for i in tu:
#     print(i)
# # 请使用for、len、range输出元组的索引
# for l in range(len(tu)):
#     print(l)
# # 请使用enumrate输出元祖元素和序号（序号从10开始）
# for l,key in enumerate(tu):
#     print(10+l,key)
# # 6、有如下变量，请实现要求的功能
# #
# # tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
# #
# # 讲述元祖的特性
# #元祖的特性包括：不可修改，有序，偏移来去数据
# # 请问tu变量中的第一个元素“alex”是否可被修改？
# #不可以，元祖是不可修改的
# # 请问tu变量中的"k2"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素“Seven”
# #是字典，可以修改
# tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])

# 请问tu变量中的"k3"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素“Seven”
# 7、字典
#
# dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
#
# 请循环输出所有的key
# dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# for k in dic:
#     print(k)
# # 请循环输出所有的value
# for k in dic:
#     print(dic[k])
# # 请循环输出所有的key和value
# for k in dic:
#     print(k,dic[k])
# # 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
# dic["k4"] = "v4"
# print(dic)
# # 请在修改字典中“k1”对应的值为“alex”，输出修改后的字典
# dic['k1'] = 'alex'
# print(dic)
# # 请在k3对应的值中追加一个元素44，输出修改后的字典
# dic["k3"].append(44)
# print(dic)
# # 请在k3对应的值的第1个位置插入个元素18，输出修改后的字典
# dic['k3'].insert(0,18)
# print(dic)
# 8、转换
#
# 将字符串s = "alex"转换成列表
# s = "alex"
# # s=list(s)
# # print(s)
# # 将字符串s = "alex"转换成元祖
# s = tuple(s)
# print(s)
# # 将列表li = ["alex", "seven"]转换成元组
# li = ["alex", "seven"]
# li = tuple(li)
# print(li)
# # 将元祖tu = ('Alex', "seven")转换成列表
# li = list(li)
# print(li)
# # 将列表li = ["alex", "seven"]转换成字典且字典的key按照10开始向后递增
# dic={}
# for i in range(len(li)):
#     dic[10+i] = li[i]
# print(dic)

# 9、元素分类
#
# 有如下值集合[11,22,33,44,55,66,77,88,99,90]，将所有大于66的值保存至字典的第一个key中，将小于66的值保存至第二个key的值中。
#
# 即：{'k1':大于66的所有值, 'k2':小于66的所有值}
# a=[11,22,33,44,55,66,77,88,99,90]
# a.sort()
# dic={}
# dic[a[0:(a.index(66))]]

# 10、输出商品列表，用户输入序号，显示用户选中的商品
#
# 商品li = ["手机", "电脑", '鼠标垫', '游艇']
#
# 允许用户添加商品
# 用户输入序号显示内容
# li = ["手机", "电脑", '鼠标垫', '游艇']
# for k in li:
#     a= li.index(k)
#     print("商品序号:%s      "%a,  "商品名称： %s"%k)
# choice = int(input("请输入你要购买商品的序号："))
# print("你购买的商品是：%s"%li[choice])

# 11、用户交互显示类似省市县N级联动的选择
#
# 允许用户增加内容
# 允许用户选择查看某一个级别内容
# 12、列举布尔值是False的所有值
#bool（...)里面的参数如果是：None，""，()，[]，{}，0中的一个的时候，返回值是Fasle
# 􏰱􏰲􏰳􏰢􏰴􏰵13、有两个列表
#
l1 = [11,22,33]

l2 = [22,33,44]
#
# 获取内容相同的元素列表
set1 = set(l1)
set2 = set(l2)
a = set1.intersection(set2)
print(a)

# 获取l1中有，l2中没有的元素列表
b = set1.difference(set2)
print(b)
# 获取l2中有，l3中没有的元素列表
# 获取l1和l2中内容都不同的元素
c = set1.symmetric_difference(set2)
print(c)
# 14、利用For循环和range输出
#
# For循环从大到小输出1 - 100
# for i in range(-100,0,):
#     print(-i)
# For循环从小到到输出100 - 1

# While循环从大到小输出1 - 100

# While循环从小到到输出100 - 1


# 15、利用for循环和range输出9 * 9乘法表
for i in range(1,10):
    k=[]
    for b in range(1,i+1):
        a=[b,'*',i,'=',b*i]
        k.append(a)
    print(k)

print('\n'.join([ ' '.join([ "%d*%d=%2s" %(y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))


# 16、求100以内的素数和。（编程题）
#
# 17、将[1,3,2,7,6,23,41,24,33,85,56]从小到大排序（冒泡法）（编程）

a = [1,3,2,7,6,23,41,24,33,85,56]
for i in range(len(a)-1):
    for k in range(len(a)-1-i):
        if a[k]>a[k+1]:
            a[k],a[k+1] = a[k+1], a[k]
print(a)
