# -*- coding: utf-8 -*-


from socket import *
from time import ctime
HOST = '127.0.0.1'
POST = 9516
BUFFSIZE = 1024
ADDR = (HOST,POST)

ss = socket(AF_INET,SOCK_DGRAM)

while True:
    ss.sendto('time'.encode('utf-8'),ADDR)
    msg,addr = ss.recvfrom(BUFFSIZE)
    print('服务器时间是：%s'%msg.decode('utf-8'))
    break

ss.close