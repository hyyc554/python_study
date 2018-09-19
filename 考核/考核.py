# -*- coding: utf-8 -*-

# a = ['alex', 'egon', 'yuan', 'wusir', '666']
# a[-1] = '999'
# b = a.index('yuan')
# c = a[-3:]
# print(a,b,c)

# #将字符串"www.luffycity.com"给拆分成列表：li=['www','luffycity','com'] （编程）
# a = "www.luffycity.com"
#
# b = a.split(".")
# print(b)

# dic = {"Development": "开发小哥", "OP": "运维小哥", "Operate": "运营小仙女", "UI": "UI小仙女"}
# del dic['Development']
# print(dic)
#
# dic['Development'] = "开发小哥"
# print(dic)
# a = dic.keys()
# b = dic.values()
# print(a,b)
# print(dic.items())

#需求：等待用户输入名字、地点、爱好，根据用户的名字和爱好进行任意实现
#如：敬爱可爱的xxx，最喜欢在xxx地方干xxx

# name = input("名字：")
# place = input('地点：')
# hobite = input('爱好：')
#
# print('敬爱的%s，最喜欢在%s地方于%s'%(name,place,hobite))


#切割字符串"luffycity"为"luffy","city"
# a = 'luffycity'
#
# b = a[0:5]
# c = a[5:]
#
# print(b,c)

#将列表['alex', 'steven', 'egon'] 中的每一个元素使用 ‘\_’ 连接为一个字符串（编程）
# a = ['alex', 'steven', 'egon']
#
# b = '\_'.join(a)
# print(b)

#有如下字符串：n = "路飞学城"（编程题）

#    - 将字符串转换成utf-8的字符编码的字节，再将转换的字节重新转换为utf-8的字符编码的字符串
#    - 将字符串转换成gbk的字符编码的字节，再将转换的字节重新转换为utf-8的字符编码的字符串

n = "路飞学城"
b = n.encode('utf-8')
c = b.decode('utf-8')
print(b,c)

d = n.encode('gbk')
f = d.decode('gbk')
e = f.encode('utf-8')
g = e.decode('utf-8')
print(d,g)












