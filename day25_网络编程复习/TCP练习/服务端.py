# -*- coding: utf-8 -*-

from socket import *

HOST = '127.0.0.1'
PORTS = 9662
BUFFSIZE = 1024
ADDR = (HOST,PORTS)

ss = socket(AF_INET,SOCK_STREAM)
ss.listen(5)
ss.bind(ADDR)

while True:
    coon,addr = ss.accept()
    print('connect from %s'%str(addr))
    with coon:
        msg = coon.recv(BUFFSIZE)
        print(msg.deconde('utf-8'))

