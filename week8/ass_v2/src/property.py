#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li
class house:
    def __init__(self, name, add, value):
        self.name = name
        self.add = add
        self.value = value
        self.owner = ''


houseobj1 = house('金地小区110', '人民南路', 50000)
houseobj2 = house('锦绣花园201', '人民东路', 60000)
houseobj3 = house('锦绣花园202', '人民东路', 61000)

houselist = list()
houselist.append(houseobj1)
houselist.append(houseobj2)
houselist.append(houseobj3)
