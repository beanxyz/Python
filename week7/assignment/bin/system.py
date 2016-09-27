#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li

import os,sys

parent_path=os.path.abspath(os.pardir)

path=parent_path+"\src"

sys.path.append(path)
# print(sys.path)

teachpath = os.path.join(parent_path, 'db', 'teacher')
courepath=os.path.join(parent_path,'db','training')
stupath=os.path.join(parent_path,'db','student')

import admin
from admin import student,teacher,training
import stu

#主入口
def main():
    while True:
        choice=input("请选择\n1:管理员\n2:学生\n3.退出\n>>>>>")
        if choice=='1':admin.run()
        elif choice=='2':stu.run()
        elif choice=='3':exit()
main()