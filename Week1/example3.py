#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li

pusername="yuan"
ppassword="123"

username=input("Please Input your name:")
password=input("Please Input your password:")

if username==pusername and password == ppassword:
    print("Login Successfully!")
else:
    print("Invalid username or password")