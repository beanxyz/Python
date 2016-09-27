#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li

name=["james","kevin","alex","bean","Sam"]
name.insert(3,"ali")
name.insert(4,"hhh")
print(name)
name.append("xyz")
print(name)
name.remove("bean")
print(name)
name.reverse()
print(name)
print(name[3:6])

del name[4:]
print(name)


name2=[1,2,3,2,2,3,5,44,[3,5,5]]
print("name2",name2)
for i in range(name2.count(5)):
    index=name2.index(5)
    name2[index]=2222
print("new naem2",name2)

for i in range(name2.count(3)):
    index=name2.index(3)
    name2.pop(index)
print("name2 remove",name2)