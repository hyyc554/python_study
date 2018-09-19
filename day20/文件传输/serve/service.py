# -*- coding: utf-8 -*-
import subprocess
import socket
import struct
import json
import os

Share_path = r'E:\迅雷下载\python_study\day20\文件传输\serve\share'

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 解决端口被占用的问题
phone.bind(('127.0.0.1', 8081))

phone.listen(5)
while True:
    print('starting....')
    conn, client_addr = phone.accept()

    while True:
        try:
            #
            rest = conn.recv(8096)
            # if not data:break #  Linux 系统的解决办法

            # 解析指令
            cmd = rest.decode('utf-8').split()  # 'get 1.map4'
            filename = cmd[1]

            # 以读的方式打开文件，读取文件内容发送给客户端
            # 第一步，制作固定长度的报头
            file_path = os.path.join(Share_path, filename)
            head_dict = {
                'filename': filename,
                'mad5': 'xxxxxx',
                'total_size': os.path.getsize(file_path)
            }
            head_json = json.dumps(head_dict)
            head_bytes = head_json.encode('utf-8')
            head_lent = len(head_bytes)
            lent_bytes = struct.pack('i', head_lent)
            conn.send(lent_bytes)
            conn.send(head_bytes)

            # 传送文件
            with open(file_path, 'rb') as f:
                for line in f:
                    conn.send(line)

        except ConnectionResetError:
            print('客户端已关闭')
            break

    conn.close()

phone.close()
