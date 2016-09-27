#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li
#%s,%d占位符,+
s="%(name)+10s is hhh, age is %(age)+10d"%{'name':'jkls','age':22}
print(s)

#保留小数点后几位
k="%.2f"%5.67
print(k)


s="%d %%"%22

print(s)

s="--------{:a^20s}".format('alex')
print(s)


#2.7直接返回结果，3.x返回一个可以生成能力的对象
li=[11,22,33]
rest=filter(lambda x:x>22,li)

for i in rest:
    print(i)

def f1():
    print("1")
    yield 22
    print("2")
    yield 33
    print("3")
    yield 44

r=f1()
print(r,type(r))
print(r.__next__())
print(r.__next__())
print(r.__next__())

for item in r:
    print(item)


#
# s="{:*^20}".format("Welcome")
# print(s)
#
# s="{:+0},{:+1}".format(-234,222)
# print(s)
#
#
# s="I am %s, I am %d years old"%("Bean",20)
# print(s)
#
# s="I am %(name)s, I am %(age)d old"%{"name":"bean","age":20}
# print(s)
#
# s="i complete %f%% of the project"%99.9
# print(s)
#
# s="i complete %.2f%% of the projects"%99.9
# print(s)
#
# s="i have $%g"%100
# s2="i have $%g"%100000000
# print(s+"\n"+s2)
#
#
# s="I am {},my age is {}".format("Beanxyz", 20)
# print(s)
#
# s="Hi,{0},I am {0}, my age is {1}".format("Beanxyz",20)
# print(s)
#
# s="Hi,{0},I am {0}, my age is {1}".format(*["Beanxyz",20])
# print(s)
#
# s="Hi,{name},I am {name}, my age is {age}".format(name="Bean",age=20)
# print(s)
#
#
# s="Hi,{name},I am {name}, my age is {age},{age}".format(**{"name":"beanxyz","age":20})
# print(s)
#
# s = "i am {:s}, age {:f}".format(*["seven", 18])
# print(s)
#
# s="二进制{:b},八进制{:o},十进制{:d},16进制{:x}，百分比{:.0%}".format(100,100,100,100,0.2)
# print(s)

def nrange(num):
    temp = -1
    while True:
        temp = temp + 1
        if temp >= num:
            return
        else:
            yield temp

r=nrange(5)
print(r)

for item in r:
    print(item)