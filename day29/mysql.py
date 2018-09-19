# -*- coding: utf-8 -*-


import pymysql

# user = input('用户名: ').strip()
# # pwd = input('密码: ').strip()
#
# # 链接
# conn = pymysql.connect(host='localhost', user='root', password='123', database='mysql_homework', charset='utf8')
# # 游标
# cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
# # cursor=conn.cursor(cursor=pymysql.cursors.DictCursor)


# # 执行sql语句
# sql = 'select * from class'# 注意%s需要加引号
# print(sql)
# res = cursor.execute(sql)
# print(res)
# sql = 'select * from userinfo where user="%s" and psd="%s"' % (user, pwd)  # 注意%s需要加引号
# print(sql)
# res = cursor.execute(sql)  # 执行sql语句，返回sql查询成功的记录数目
# print(res)
#
# cursor.close()
# conn.close()
#
# if res:
#     print('登录成功')
# else:
#     print('登录失败')
#
# sql='select * from userinfo;'
# rows=cursor.execute(sql) #执行sql语句，返回sql影响成功的行数rows,将结果放入一个集合，等待被查询
#
# # cursor.scroll(3,mode='absolute') # 相对绝对位置移动
# # cursor.scroll(3,mode='relative') # 相对当前位置移动
# # res1=cursor.fetchone()
# # res2=cursor.fetchone()
# # res3=cursor.fetchone()
# # res4=cursor.fetchmany(2)
# res5=cursor.fetchall()
# # print(res1)
# # print(res2)
# # print(res3)
# # print(res4)
# print(res5)
# print('%s rows in set (0.00 sec)' %rows)
#
#
#
# conn.commit() #提交后才发现表中插入记录成功
# cursor.close()
# conn.close()
import pymysql
#链接
conn=pymysql.connect(host='localhost',user='root',password='123',database='mysql_homework')
#游标
cursor=conn.cursor()

#执行sql语句
#part1
# sql='insert into userinfo(name,password) values("root","123456");'
# res=cursor.execute(sql) #执行sql语句，返回sql影响成功的行数
# print(res)

#part2
# sql='insert into userinfo(name,password) values(%s,%s);'
# res=cursor.execute(sql,("root","123456")) #执行sql语句，返回sql影响成功的行数
# print(res)

#part3
sql='insert into userinfo(name,password) values(%s,%s);'
res=cursor.executemany(sql,[("root","123456"),("lhf","12356"),("eee","156")]) #执行sql语句，返回sql影响成功的行数
print(res)


# sql='select * from userinfo;'
# rows=cursor.execute(sql) #执行sql语句，返回sql影响成功的行数rows,将结果放入一个集合，等待被查询

# cursor.scroll(3,mode='absolute') # 相对绝对位置移动
# cursor.scroll(3,mode='relative') # 相对当前位置移动
# res1=cursor.fetchone()
# res2=cursor.fetchone()
# res3=cursor.fetchone()
# res4=cursor.fetchmany(2)
res5=cursor.fetchall()
# print(res1)
# print(res2)
# print(res3)
# print(res4)
print(res5)
print('%s rows in set (0.00 sec)' %rows)
conn.commit() #提交后才发现表中插入记录成功
cursor.close()
conn.close()