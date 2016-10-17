#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li
for i in range(10):
    name = i

print(name)


# Python里面没有块级别的作用域
# python是以函数为作用域

def func():
    # global name
    name = 'alex'


func()
print(name)


# 作用域链 ， 由内向外找，直到找不到报错
def f1():
    name = 'a'

    def f2():
        name = 'b'
        print(name)

    f2()
    print(name)


f1()

# 在函数没有执行之前，作用域已经确定了，作用域链也已经确定了

name = 'alex'


def f0():
    print(name)


def f1():
    name = 'bbb'
    f0()


def f2():
    name = 'eric'
    f1()


f2()

li = [x + 100 for x in range(10)]
print(li)

li = [x + 100 for x in range(10) if x > 6]
print(li)

# li列表里面的元素[函数，函数，函数]，函数在没有执行前，内部代码不执行
li = [lambda: x for x in range(10)]
print(li)

print(li[0]())
# li[0],函数
# 函数（）



li = []
for i in range(10):
    def f1():
        return i


    li.append(f1)

# li是列表，内部元素是相同功能的函数
# i
print(i)
## f1 没有调用之前，内部代码不执行；因此li内部都是函数
##真正执行（） 时候，他会返回i，内部没有i，往上找，i已经是9了，因此返回9
print(li[0]())
print(li[2]())

li = []
for i in range(10):
    def f1(x=i):
        return x


    li.append(f1)

# li是列表，内部元素是相同功能的函数
# i
print(i)
## f1 没有调用之前，内部代码不执行；因此li内部都是函数
##真正执行（） 时候，他会返回i，内部没有i，往上找，i已经是9了，因此返回9
print(li[0]())
print(li[2]())
