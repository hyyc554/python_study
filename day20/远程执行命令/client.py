# -*- coding: utf-8 -*-
import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8081))

while True:
    cmd = input(">>>:").strip()
    if not cmd:continue
    phone.send(cmd.encode('utf-8'))
    data = phone.recv(1024)
    print(data.decode('gbk'))

phone.close()
