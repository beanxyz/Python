#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li

'''
print("Hello World!")

name="yuan li"
print(name)

username=input("Plese input your name: ")
print(username)

'''
account=input("Please intput your account: ")
age =int(input("Please intput your age: "))
job =input("Please intput your job: ")

msg='''
User Information
----------------
Account : %s
Age     : %d
Job     : %s

------END--------
''' % (account,age,job)

print(msg)