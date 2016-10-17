#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li
import socket

ip_port = ('127.0.0.1', 5555)
s = socket.socket()
s.bind(ip_port)
s.listen(5)  # 代表可以挂起的数目，比如现在通信一个，还可以最多挂起5个
while True:
    conn, addr = s.accept()
    while True:
        try:
            recv_data = conn.recv(1024)
            if str(recv_data, encoding='utf-8') == 'exit': break
            print(str(recv_data, encoding='utf8'))
            send_data = recv_data.upper()
            conn.send(send_data)
        except Exception as ex:
            break
    conn.close()
