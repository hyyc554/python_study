# -*- coding: utf-8 -*-
from socket import *
import struct
import json
import os
from config.setting import DATA_BASE


class MyTCPSocket:
    HOST = '127.0.0.1'
    PORT = 9966
    BUFSIZE = 8096
    ADDR = (HOST, PORT)
    CODING = 'utf-8'
    request_queue_size = 5
    allow_reuse_address = False

    def __init__(self, server_address):
        self.server_address = server_address
        self.socket = socket(AF_INET, SOCK_STREAM)

    def server_bind(self):
        """Called by constructor to bind the socket.
        """
        if self.allow_reuse_address:
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(self.server_address)

    def server_activate(self):
        """Called by constructor to activate the server.
        """
        self.socket.listen(self.request_queue_size)

    def server_close(self):
        """Called to clean-up the server.
                """
        self.socket.close()

    def get_request(self):
        """Get the request and client address from the socket.
        """
        return self.socket.accept()

    def close_request(self, request):
        """Called to clean up an individual request."""
        request.close()

    def run(self):
        while True:
            conn, client_addr = self.get_request()
            print('from client ', client_addr)
            while True:
                try:
                    rest = conn.recv(self.BUFSIZE)
                    if not rest:
                        break
                        # 这里规定所有的指令均为至少有一个，'get 1.map4'
                        # 解析指令
                    cmd = rest.decode('utf-8').split()
                    cmd_word = cmd[0]
                    if hasattr(self, cmd_word):
                        func = getattr(self, cmd_word)
                        # 这里为了保证后面程序的流畅度，直接把返回的元祖形式的命令行反馈给服务器类
                        func(cmd)
                    else:
                        print('不存在')
                    head_dic = {'cmd': 'put', 'filename': 'a.txt', 'filesize': 123123}
                except Exception:
                    break
                #     if not rest:
                #         break
                #     # 这里规定所有的指令均为至少有一个，'get 1.map4'
                #     # 解析指令
                #     cmd = rest.decode('utf-8').split()
                #     cmd_word = cmd[0]
                # if hasattr(self, cmd):
                #     func = getattr(self, cmd)
                #     func(head_dic)
                # else:
                #     print('不存在')
                # head_dic={'cmd':'put','filename':'a.txt','filesize':123123}

    def copy(self, cmd):
        filename = cmd[1]
        file_path = os.path.join(DATA_BASE['share_path'], filename)
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
