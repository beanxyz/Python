#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li

import json
fp=open('result.json','r+')
userinfo=json.load(fp)

#print(userinfo)

for k,v in userinfo.items():
    print(k,v)
    if 'Yuan' in v['name'] and 'hhh' in v['password']:
        print("User Yuan's key is ",k)
        userinfo[k]['balance']=9999999


print(userinfo)

fp=open('result.json','w')
json.dump(userinfo,fp)