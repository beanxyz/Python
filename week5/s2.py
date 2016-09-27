#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li

# import week5.s1
import sys

# sys.path()
# #添加路径到当前的列表中
# sys.path.append('e:\\')
# for item in sys.path:
# print(sys.path)

#命名不要崇明
#导入模块，可以是文件，或者文件夹
#导入路径 system.path
# week5.s1.f1()


# import os
# if os.path.isfile("c:/temp/test.csv"):
#     print("exist")
# else:
#     print("False")
#
#
# if os.path.isfile(os.path.join("c:/temp","test.csv")):
#     print("true")
# else:
#     print("false")
#
#
# fp=open('c:/temp/test.csv','r')
# for line in fp:
#     print(line)


# # import 导入
# from week5.s1 import *
from week5.s1 import f1
f1()
#建议通过import导入 避免冲突 （适合单目录，同一个目录）
from week5 import s1
s1.f1()

#安装 pip3,yum,源码，apt-get,request
# C:\Program Files\py35\Scripts

#pip3 install requests
#cd E:\XXXX
# python3 setup.py install

import requests


"""
序列化  把数据类型转化为字符串
反序列化 把字符串转换为数据类型

# """
import json
dic={"k1":"v1"}
print(dic,type(dic))
#
#通过dumps把 python基本数据类型转换为字符串形式
result=json.dumps(dic)
print(result,type(result))
#
import json,pickle
s='{"k1":"v1"}'
dic=json.loads(s)
dic2=eval(s)
# dic3=pickle.loads(s)
print(dic,type(dic))
print(dic2,type(dic2))
# print(dic3,type(dic3))

import requests,json
# r=requests.get('http://api.openweathermap.org/data/2.5/weather?q=sydney,au')
# r.encoding='utf-8'
# h=json.loads(r.text)
# print(h)
#py基本类型转换字符串
#注意dumps和dump的区别
r=json.dumps([1,2,3])
print(r,type(r))

#反序列化的时候，内部用双引号！！
li='["alex","eric"]'
ret=json.loads(li)
print(ret,type(ret))

#
# json.dump()
# json.load()

#多一步，序列化之后写入一个文件
li=[1,2,3]
json.dump(li,open('db','w'))


li=json.load(open('db','r'))
print(li,type(li))


#pickle只有python能用的特殊字符串，json可以不同语言同样

import pickle
li=[1,2,3]
r=pickle.dumps(li)
print(r)#特殊字符串

result=pickle.loads(r)
print(result)

# pickle.dump(li,open('db','wb'))

#json只支持基本数据类型，列表，字典，字符串等等
# json._default_encoder

#存档游戏，pickle,复杂类操作，版本