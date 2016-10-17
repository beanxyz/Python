#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li
import socket
import subprocess

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

            if len(recv_data) == 0: break
            print(str(recv_data, encoding='utf-8'))

            # ret=subprocess.Popen(str(recv_data,encoding='utf8'),shell=True,stdout=subprocess.PIPE)
            p = subprocess.Popen(str(recv_data, encoding='utf8'), shell=True, stdout=subprocess.PIPE)
            ret = p.stdout.read()  # bytes
            print(str(ret, encoding='gbk'))

            if len(ret) == 0:
                send_data = 'Cmd Err'

            else:
                send_data = str(ret, encoding='gbk')

            # send_data=recv_data.upper()
            print(send_data)
            conn.send(bytes(send_data, encoding='utf8'))
        except Exception as ex:
            break
    conn.close()
