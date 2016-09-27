#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li

# import s2
#
# print(vars(s2))

#
# __file__ 当前文件的路径
# __doc__  文件注释
# __cached__  pycache的路径（字节码存放位置）
# __name__
# __package__





"""
我是注释
"""
#获取文件的注释
print(__doc__)

#当前运行的文件所在的路径
print(__file__)

#
from bin import admin
print(__package__)
print(admin.__package__) #显示包
#只有执行当前文件时候，当前文件的特殊变量__name__==__main__  导入不等，执行才等
#__name__ ==__main__

def run():
    print('run')


#只有执行本文件，才执行；导入不会执行
if __name__=='__main__':
    run()

#sys j


import  hashlib


obj=hashlib.md5()
# obj.update('1232') 2.76
obj.update(bytes('123',encoding='utf-8'))
res=obj.hexdigest()
print(res)