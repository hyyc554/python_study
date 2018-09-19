# encoding：utf-8


import socket
import threading
import time


def tcplink(sock, addr):
    print('accepting new connection from %s:%s' % addr)
    sock.send(b'Welcome')
    while True:
        data = sock.recv(1024)
        print(data)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('connection close')


# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
# 和监听端口
s.bind(('127.0.0.1', 9998))
s.listen(5)
print('Waiting for connection...')
while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
