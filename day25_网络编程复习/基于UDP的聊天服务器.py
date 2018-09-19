# -*- coding: utf-8 -*-

from socket import *

iP = ('127.0.0.1', 9667)
BuffSize = 1024
ss = socket(AF_INET, SOCK_DGRAM)

ss.bind(iP)
while True:

    msg, addr = ss.recvfrom(BuffSize)
    print('connectting...from %s' % str(addr))
    print(msg.decode('utf-8'))

    ss.sendto(input('>>>:').strip().encode('utf-8'), addr)


ss.close()
