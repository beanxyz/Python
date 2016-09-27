# # #!/usr/bin/env python
# # # -*- coding:utf-8 -*-
# # # Author Yuan Li
# #
# # # str=input("please input string")
# # #
# # # print(str,type(str))
# #
# # import json
# # # json_acceptable_string = str.replace("'", "\"")
# #
# # str='{"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}'
# # file=json.loads(str)
# #
# # print(file,type(file))
# #
# # inp_str = "[11,22,33,44]"
# # inp_list = json.loads(inp_str)
# # print(inp_list,type(inp_list))
#
#
# #读取配置文件里面的backend节点信息
# backendname=input("please input the name")
# file=open('config','r',encoding='utf-8')
#
# flag=0
# for line in file:
#     # print(line)
#     line=line.strip()
#     if flag==1:
#         if line.startswith("backend"):
#             flag=0
#             continue
#         elif line.startswith("server"):
#             print(line)
#
#
#         # print(line)
#         flag=1
#         continue
#     else:
#         continue
#
#
#
# #
#
#
# #添加信息
# 搜索backend的节点：
# 1。如果存在，添加信息；
# flag=0
# for line in f1,f2:
#     if flag==1 and line.startwith("server"):
#         write f1.line to f2
#         # write new_str to f2
#
#
#     if exist backend:
#         flag=1
#         continue
#
#
#

#
# 2。如果不存在，创建节点，添加信息
#
#
#
#
# import json
# # backendname=input("Name: ")
# #
# # dic=json.loads(backendname)

string='{"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}'
# dic=json.loads(str)
# print (dic,type(dic))
# record=dic['record']
# backend=dic['backend']
# # print(backend)
#
# import re
# # string=input("input a string: ")
# pattern='{"backend": ".+","record":{"server": ".+","weight": \d+,"maxconn": \d+}}'
# re=re.match(pattern,string)
# if re !=None:
#     print(re.group())
# else:
#     print("Invalid Input")
#
# backend www.oldboy.org
# server 100.1.7.9 100.1.7.9 weight 20 maxconn 3000

import json

string=input("input:　")
try:
    dic=json.loads(string)
    bk=dic["backend"]
    rd=dic["record"]
    server=rd['server']
    weight=rd["weight"]
    maxconn=rd["maxconn"]
    print("backend %s"%bk)
    print("rd %s"%rd)
    print("server %s weight %d maxconn %d"%(server,weight,maxconn) )

except:
    print("Invalid format")