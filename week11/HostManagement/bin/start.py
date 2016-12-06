#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li
import os, sys
from sqlalchemy import create_engine, and_, or_, func, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, DateTime
from  sqlalchemy.orm import sessionmaker, relationship

parent_path = os.path.abspath(os.pardir)

#path = parent_path + "\src"

path=os.path.join(parent_path,'src')

# print(path)
sys.path.append(path)

import remoteControl,databaseControl

def run():
    msg="""
    1. 用户主机操作
    2. 管理员操作
    3. 退出
    """

    while True:
        print(msg)
        choice=input('请输入选项')
        if choice=='1':
            remoteControl.run()
        elif choice=='2':
            databaseControl.ManageData()
        elif choice=='3':
            exit()


if __name__ == '__main__':
    run()