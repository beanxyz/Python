#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li


China = {
    "1": {
        "name": "SiChuan",
        "info": "四川是个好地方",
        "City": {
            "1": {
                "name": "Chengdu",
                "info": "成都的妹子都很漂亮",
                "Destination": {
                    "1": {
                        "name": "DaYiXian",
                        "info": "Nice Hot Spring!"
                    }
                },
            "2":{
                "name":"DeYang",
                "info":"DeYang is a clean city",
                "Destination":{
                    "1":{}
                }
            }
            }
        }
     },
    "2":{
    "name":"HeNan",
    "info":"HeNan is a large province",
    "City":{
        "1":{
            "name":"LuoHe",
            "info":"LuoHe is small",
            "Destination":{}
        },
        "2":{}
    }
    }


}


for i in sorted(China):
#print(China["1"])
    print(i,China[i]["name"])
#    print(China[i]["info"])
print(China["1"]["City"])
#print(China["1"]["City"]["1"]["name"])
provinceid=input("Please choose the province code:")

if int(provinceid)>0 and int(provinceid)<=len(China):

    for j in sorted(China[provinceid]):
        print(China[provinceid]["City"]["j"]["name"])

