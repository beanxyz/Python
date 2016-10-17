#!/usr/bin/env python
# # -*- coding:utf-8 -*-
# # Author Yuan Li
# class Province:
#
#     country = 'China'
#
#     def __init__(self, name, count):
#         self.name = name
#         self.count = count
#
#     def func(self, *args, **kwargs):
#         print ('func')
#
# # 获取类的成员，即：静态字段、方法、
# print (Province.__dict__)
# # 输出：{'country': 'China', '__module__': '__main__', 'func': <function func at 0x10be30f50>, '__init__': <function __init__ at 0x10be30ed8>, '__doc__': None}
#
# obj1 = Province('HeBei',10000)
# print (obj1.__dict__)
# # 获取 对象obj1 的成员
# # 输出：{'count': 10000, 'name': 'HeBei'}
#
# obj2 = Province('HeNan', 3888)
# print (obj2.__dict__)
# # 获取 对象obj1 的成员
# # 输出：{'count': 3888, 'name': 'HeNan'}

# class Foo:
#
#     def __str__(self):
#         return 'hhh'
#
#
# obj = Foo()
# # print(obj)
# # # 输出：wupeiq
#
# # !/usr/bin/env python
# # -*- coding:utf-8 -*-
#
# class Foo(object):
#     def __getitem__(self, key):
#         print('__getitem__', key,type(key))
#
#     def __setitem__(self, key, value):
#         print('__setitem__', type(key), type(value))
#
#     def __delitem__(self, key):
#         print('__delitem__', key)
#
#
# obj = Foo()
# result=obj[0:3]
# print(result)
# obj[1:3]=[2,3,4,5,6,7]
# del obj[2:3]
#
#
#
# # result = obj['k1']  # 自动触发执行 __getitem__
# # obj['k2'] = 'bb'  # 自动触发执行 __setitem__
# # del obj['k1']  # 自动触发执行 __delitem__
#
#
# class Foo(object):
#
#     def __init__(self, sq):
#         self.sq = sq
#
#     def __iter__(self):
#         return iter(self.sq)
#
# obj = Foo([11,22,33,44])
#
# for i in obj:
#     print(i)

# a=100
# assert a>10
# print("Ok")
# assert a<40,print("oh wrong")
# print("wrong")
import subprocess

ret = subprocess.Popen('ipconfig /all', shell=True, stdout=subprocess.PIPE)

ss = ret.stdout.read()

print(str(ss))
