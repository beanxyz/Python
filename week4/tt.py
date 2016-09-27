#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li

def outer(func):
    def innner(*args,**kwargs):
        print(func)
        a=func(*args,**kwargs)
        print("装饰1")
        return a
    return innner


def outer2(func):
    def inner(*args,**kwargs):
        print(func)
        a=func(*args,**kwargs)
        print("装饰2")
        return a
    return inner



@outer2
@outer
def f1():
    print("原函数")
    return "hee"

f1()




