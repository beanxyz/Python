#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li

内置函数
abs()绝对值
print(abs(-1))
all()
any()

0,None,"",[],{},() 都是false,布尔值
print(bool(None))
print(bool(()))

all里面传入的可迭代的对象，里面每一个对象为真，结果为真
n=all([1,2,3,4,None])
print(n)

#只要有真就为真
m=any([1,0,""])
print(m)

ascii,自动执行对象的_repr_方法
ascii()

bin() 10进制转2进制
oct() 10进制转8进制
hex() 10进制转16进制

print(bin(5))
print(oct(9))
print(hex(15))

byte()
utf-8 1个汉字是3个字节，gbk一个汉字 2个字节

utf-8,一个字节8位，一个汉字3个字节，所以一个汉字24位
s="李杰"
#把字符串转换成字节类型
n=bytes(s,encoding="utf-8")
print(n)

n=bytes(s,encoding="gbk")
print(n)

#字节转换成字符串
m=str(bytes(s,encoding="utf-8"),encoding="utf-8")
print(m)

#打开文件
f=open('db','r') 只读
f=open('db','w') 清空重写
f=open('db','w') 清空重写
f=open('db','a') 追加

#注意打开时候的编码方式
f=open('db','r',encoding="utf-8")
data=f.read()
print(data,type(data))
f.close()

# #b告诉python，不要给我处理，直接处理二进制,表现形式则为字节类型
f=open('db','rb')
data=f.read()
print(data,type(data))

# #会报错，因为加了b，字符串不能换成二进制字节
f=open("db",'ab')
f.write("hello")
f.close()
#
#
f=open("db",'ab')
f.write(bytes("哈",encoding="utf-8"))
f.close()

# "+"表示可以同时读写，r+最常用
# #如果打开模式没有b，那么read 按照字符读取
f=open("db",'r+',encoding="utf-8")
data=f.read(2)
print(data)
print(f.tell())#获取当前指针位置（字节）
#
# #调整位置（字节的位置），如果有中文，就会硬分开，导致乱码。往后写的时候会覆盖之前的位置
f.seek(1)
#当前指针位置开始向后面覆盖
f.write("7777")
f.close()
#
#
# # w+ 先清空才写，然后才读之后写入的内容
# # a+ 永远是在最后添加
#
# #
# # #操作文件,ctrl点击，通过源码查看功能
# # # f.read() 无参数，读取全部； 有参数，有b. 按照字节； 无b，按照字符
# #  tell(),获取当前位置（字节）
# #  seek(1),跳到指定位置（字节）
# #write() 写数据，b,字节； 没b,字符
# # close()
# # fileno 文件描述符，判断是否变化
# # flush 强刷到硬盘
# #
f=open('db','a')
f.write('123')
f.flush()  #没有close 但是内容写入了硬盘
input("hhhh")
#
# #判断是否可读
f=open('db','w')
print(f.readable())
# #
# #
# # #readline（）只读取一行
f=open('db','r')
f.readline()#注意指针的变化
f.readline()
#
# #truncate 截断，清空指针后面的内容
#
f=open('db','r+',encoding='utf-8')
f.seek(3)
f.truncate()
#
for循环文件
f=open('db','r+',encoding='utf-8')
for line in f:
    print(line)
#
#
# #
#关闭文件
f.close()
#
# #自动关闭
with open('db') as f:
    pass
# #
# # #2.7之后可以同时打开两个文件
with open('db1','r',encoding="utf-8") as f1,open('db2','w',encoding='utf-8') as f2:
    times=0
    for line in f1:
        times+=1
        if times <=10:
            f2.write(line)
        else:
            break
#
#
# #替换
# with open('db','r+',encoding="utf-8") as f1,open('db2','w',encoding='utf-8') as f2:
#     for line in f1:
#         # new_str=line.replace("alex","erics")
#         # f1.write(line)
#         if line=="XXX":
#             f2.write()
#             f2.write()
#
