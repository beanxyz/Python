#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li

# from story import person,rich,poor

class careers:
    def __init__(self, name, people):
        self.name = name
        self.people = people
        self.exp = 0
        self.level = 1


class public_servant(careers):
    # 职业等级

    path = {
        "1": {"name": "办事员", "salary": 5000},
        "2": {"name": "科长", "salary": 10000},
        "3": {"name": "处长", "salary": 20000},
        "4": {"name": "省长", "salary": 40000},
        "5": {"name": "部长", "salary": 80000}

    }

    def check_level(self):
        if self.exp < 50:
            lv = 1
        elif self.exp < 100:
            lv = 2
        elif self.exp < 300:
            lv = 3
        elif self.exp < 400:
            lv = 4
        else:
            lv = 5

        if lv > self.level:
            print("%s 升值为%s" % (self.people.name, self.path[str(lv)]["name"]))
            self.level = lv
        else:
            print("职务无变化，请继续努力")

    def work(self):
        self.exp += 99
        # print(self.path)
        s = self.path[str(self.level)]['salary']
        self.people.money += s
        print("收到薪水%d" % s)
        self.check_level()


class farmer(careers):
    # 职业等级

    path = {
        "1": {"name": "初级农民", "salary": 2000},
        "2": {"name": "中级农民", "salary": 4000},
        "3": {"name": "高级农民", "salary": 6000},

    }

    def check_level(self):
        if self.exp < 50:
            lv = 1
        elif self.exp < 100:
            lv = 2
        else:
            lv = 3

        if lv > self.level:
            print("%s 升职为%s" % (self.people.name, self.path[str(lv)]["name"]))
            self.level = lv
        else:
            print("职务无变化，请继续努力")

    def work(self):
        self.exp += 99
        # print(self.path)
        s = self.path[str(self.level)]['salary']
        self.people.money += s
        print("收到薪水%d" % s)
        self.check_level()
