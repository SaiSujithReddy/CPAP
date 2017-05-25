#!/usr/bin/env python

from socket import *

HOST = raw_input('Enter host: ')
if not HOST:
    HOST = 'localhost'
PORT = int(raw_input('Enter port: '))
if not PORT:
    PORT = 21567

BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input('> ')
    if not data:
        break
    udpCliSock.sendto(data, ADDR)
    data, ADDR = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print data

udpCliSock.close()
