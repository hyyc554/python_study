# -*- coding: utf-8 -*-

"""
基于udp协议编写程序，实现功能

执行指定的命令，让客户端可以查看服务端的时间

执行指定的命令，让客户端可以与服务的的时间同步
"""
from socket import *
from time import ctime

HOST = '127.0.0.1'
POST = 9516
BUFFSIZE = 1024
ADDR = (HOST,POST)

ss = socket(AF_INET,SOCK_DGRAM)
ss.bind(ADDR)

while True:
    msg,addr = ss.recvfrom(BUFFSIZE)
    if msg.decode('utf-8') == 'time':
        ss.sendto(('server time is %s'%ctime()).encode('utf-8'),addr)
        break
    else:
        print('erro')
ss.close()