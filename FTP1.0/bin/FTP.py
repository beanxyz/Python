#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li
import os, sys

parent_path = os.path.abspath(os.pardir)

path = parent_path + "\src"

sys.path.append(path)

import ftp_client, ftp_server, user_mgmt


def run():
    msg = """
    1.管理用户
    2.启动服务器
    3.启动客户端
    """

    while True:
        print(msg)

        choice = input("请选择服务")
        if choice == '1':
            user_mgmt.run()
        elif choice == '2':
            ftp_server.run()
        elif choice == '3':
            ftp_client.run()


if __name__ == '__main__':
    run()
