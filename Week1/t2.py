#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li

file = open('credential.txt', 'r')
for line in file:
    puser = line.strip().split()[0]
    ppassword = line.strip().split()[1]

    print("user is :",puser)
    print("password is :",ppassword)


file2=open('credential.txt','w')
file2.write(file2)
    print(i.strip())

