#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li
import os,json
if os.path.isfile("hhh.json"):
    fp = open("hhh.json", 'r')
    historyinfo = json.load(fp)

    historyinfo['time1'] = "aaaa"

    fp = open("hhh.json", 'w')
    json.dump(, fp)