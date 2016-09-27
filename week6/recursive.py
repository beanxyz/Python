#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li

#1*2*3*4*5.。。


def func(num):
    if num==1:
        return 1

    return num*func(num-1)

print(func(7))


#1+2+3+4+100


def func2(num):
    if num==1:
        return 1

    return num+func2(num-1)

print(func2(100))