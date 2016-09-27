#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li

# import commons
# inp=input("input:\n>>>>")


def run():
    inp=input("Please input the Url.\n>>>>")

    m, f = inp.split('/')


    obi=__import__("lib."+m,fromlist=True)
    obj=__import__(m)

    if hasattr(obj,f):
        func=getattr(obj,f)
        func()
    else:
        print("404")

if __name__ == '__main__':
    run()