# -*- coding: utf-8 -*-
import subprocess
import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
phone.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  # 解决端口被占用的问题
phone.bind(('127.0.0.1', 8081))

phone.listen(5)
while True:
    print('starting....')
    conn, client_addr = phone.accept()

    while True:
        try:
            cmd = conn.recv(1024)
            # if not data:break #  Linux 系统的解决办法
            print('客户端数据',cmd)
            # 执行远端发送来的命令
            rst = subprocess.Popen(cmd.decode('utf-8'),shell= True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            stdout = rst.stdout.read()
            stderr = rst.stderr.read()
            conn.send(stdout+stderr)
        except ConnectionResetError:
            print('客户端已关闭')
            break

    conn.close()

phone.close()
