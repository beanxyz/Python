#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li

import socket

ip_port = ('127.0.0.1', 8009)
s = socket.socket()
s.connect(ip_port)

data = s.recv(1024)

print(data.decode())
while True:
    send_data = input("Data>>>")
    s.send(bytes(send_data, encoding='utf-8'))
    recv_data = s.recv(1024)
    print(recv_data.decode())
