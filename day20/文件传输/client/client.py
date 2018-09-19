# -*- coding: utf-8 -*-
import socket
import struct
import json
import os

down_path = r'E:\迅雷下载\python_study\day20\文件传输\client\download'
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8081))

while True:
    cmd = input(">>>:").strip()
    if not cmd:
        continue
    phone.send(cmd.encode('utf-8'))
    lent_bytes = phone.recv(4)
    head_lent = struct.unpack('i', lent_bytes)[0]
    json_bytes = phone.recv(head_lent)
    head_dict = json.loads(json_bytes.decode('utf-8'))
    print(head_dict)
    total_size = head_dict['total_size']
    file_name = head_dict['filename']
    file_path = os.path.join(down_path, file_name)

    with open(file_path, 'wb') as fb:
        recv_size = 0
        while recv_size < total_size:

            line = phone.recv(1024)
            fb.write(line)
            recv_size += len(line)
            print('文件总大小:%s,当前已完成%s' % (total_size, recv_size))

phone.close()
