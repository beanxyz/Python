#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li
import socket

ip_port = ('127.0.0.1', 5555)
s = socket.socket()
s.connect(ip_port)
while True:
    data = input('>>').strip()
    if len(data) == 0: continue
    # 如果直接输入空格或者回车，直接会卡住，因为服务器方面recv不会接受,会导致阻塞
    s.send(bytes(data, encoding='utf8'))
    if data == 'exit': break
    recv_data = s.recv(1024)
    print(str(recv_data, encoding='utf8'))
s.close()
