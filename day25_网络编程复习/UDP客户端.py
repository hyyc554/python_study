# -*- coding: utf-8 -*-
from socket import *


ADDR = ('127.0.0.1', 9667)
BuffSize = 1024
ss = socket(AF_INET, SOCK_DGRAM)

while True:
    print('connectting...TO %s' %str(ADDR))
    ss.sendto(input('>>>:').strip().encode('utf-8'), ADDR)
    msg, addr = ss.recvfrom(BuffSize)
    print(msg.decode('utf-8'))

ss.close()

