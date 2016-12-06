#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li
import os, sys

parent_path = os.path.abspath(os.pardir)

path = parent_path + "\src"

sys.path.append(path)

import client,server

def run():
    msg = """
    1.启动服务器
    2.启动客户端
    3.退出
    """

    while True:
        print(msg)

        choice = input("请选择服务")
        if choice == '1':
            server.execute()
        elif choice == '2':
            client.run()
        elif choice == '3':
            exit()


if __name__ == '__main__':
    run()
