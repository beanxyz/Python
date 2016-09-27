#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li
#同名的函数，后面的会覆盖前面的
def f1():
    print(123)

def f1():
    print(456)

f1()

#函数作为参数传入另外一个函数
def f3():
    print(123)

def f4(xxx):
    xxx()

f4(f3)