# -*- coding: utf-8 -*-
import socket
import struct

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8081))

while True:
    cmd = input(">>>:").strip()
    if not cmd:
        continue
    phone.send(cmd.encode('utf-8'))
    head = phone.recv(4)
    size = struct.unpack('i', head)[0]
    recv_size = 0
    recv_data = b''

    while recv_size < size:
        data = phone.recv(1024)
        print(data.decode('gbk'))
        recv_size += len(data)

phone.close()
