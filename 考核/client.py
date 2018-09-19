# -*- coding: utf-8 -*-


from socket import *
ADDR= ('127.0.0.1',9662)
ss = socket(AF_INET,SOCK_STREAM)
ss.connect(ADDR)
while True:

    ss.send('Hello world'.encode('utf-8'))

    msg = ss.recv(1024)
    print(msg.decode('utf-8'))
ss.close()