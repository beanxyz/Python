#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li

# # 封闭开放原则：不要去修改函数
# #装饰器
# def outer(func):
#     def inner():
#         print("log")
#         # return func()
#         ret=func()  获取原函数的返回值
#         print('after')
#         return ret  重新把原函数的返回值赋值给f1
#     return inner


#def outer(func):
#     # print(123,func)
# def outer(func):
#     return "111"

def outer(func):
    def inner(aa):
        print("before")
        func(aa)
        print("after")
    return inner



#@+函数名
#功能：
#1. 自动执行outer函数并且将下面的函数名f1当做参数传递
#2. 将outer函数的返回值，重新赋值给f1

@outer
def f1(aa):
    print("F1"+aa)


#f1="111"
# #print(f1)
#
# @outer
# def f2():
#     print("F2")


#如果有参数，装饰器也需要有,如果参数个数不等，可以使用万能参数