#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li


import json,os

if os.path.isfile('myfile.json'):
    file=open('myfile.json','r+')
    China=json.load(file)
else:
    print("Critical Error: file is missing!")
    exit()


ProvinceFlag = True
CityFlag = True
ZoneFlag = True


while ProvinceFlag == True:
    for item in sorted(China):
        print(item,China[item]['name'])

    ProvinceNameid = input("Please Input the Province Option: ")
    CityFlag=True

    while CityFlag == True:
        if ProvinceNameid in China:
            CityMap=China[ProvinceNameid]['City']
            #print(CityMap)

            for cities in sorted(CityMap):
                print(cities,CityMap[cities]['name'])
            CityNameid = input("Please input the City Option: ")
            ZoneFlag=True



            if CityNameid in CityMap:
                #print(CityMap[CityNameid])
                ZoneMap=CityMap[CityNameid]

                while ZoneFlag == True:
                    for zone in sorted(ZoneMap):
                        print(zone,ZoneMap[zone])

                    choice= input("Please input the option:(b to back,q to quit)")

                    if choice=='b':
                        ZoneFlag=False

                    elif choice=='q': exit()

            if CityNameid=='b':
                CityFlag=False

            elif CityNameid=='q': exit()

