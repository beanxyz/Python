#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li

import sys

#顶级目录：河南，四川；
#次级目录-河南目录：漯河；
#次级目录-四川目录：成都；
#三级目录-漯河目录：舞阳县，舞钢县
#三级目录-成都目录：大邑县，郫县
province=['1.HeNan','2.SiChuan']
Henan=['1.LuoHe']
SiChuang=['1.ChengDu']
LuoHe=['1.WuYuang']
Chengdu=['1.DaYi','2.PiXian']

#一些变量
level=1
ProvinceName=""
CityName=""
ZoneName=""
action1=""
action2=""
action3=""
action4=""

#回到上一级目录
def Back():
    global level,action2
    level=level-1
    #print(level, ProvinceName, CityName)
    if level==1:
        ProvinceInfo()
        ChooseProvince()
    elif level==2 and ProvinceName=="HeNan":
        HeNanInfo()
       # ChooseProvince()
    elif level==2 and ProvinceName=="SiChuan":
        SichuanInfo()
        ChooseCitySichuan()
       # ChooseProvince()

    elif level==3 and CityName=="LuoHe" and ProvinceName=="HeNan":
        LuoHeInfo()
    elif level==3 and CityName=="Chengdu" and ProvinceName=="SiChuan":
        ChengduInfo()


#省份名称
def ProvinceInfo():
    global level
    level=1
    number=len(province)
    for i in range(number):
        print(province[i])

#河南的信息
def HeNanInfo():
    global ProvinceName,level
    level=2
    ProvinceName="HeNan"
    print("You choose HeNan Province!")
    number=len(Henan)
    for i in range(number):
        print(Henan[i])

#四川的信息
def SichuanInfo():
    global ProvinceName,level
    level=2
    ProvinceName="SiChuan"
    #print("You Choose SiChuan Province!")
    number=len(SiChuang)
    for i in range(number):
        print(SiChuang[i])

#漯河的信息
def LuoHeInfo():
    global CityName,level
    level=3
    CityName="LuoHe"
    number=len(LuoHe)
    for i in range(number):
        print(LuoHe[i])


#成都的信息
def ChengduInfo():
    global CityName,level
    level=3
    CityName="Chengdu"
    number = len(Chengdu)
    for i in range(number):
        print(Chengdu[i])

#舞阳的信息
def WuYangInfo():
    global level,ZoneName
    ZoneName="WuYang"
    print("WuYang is a nice place!")
    level=4

#郫县的信息
def PiXianInfo():
    global level,ZoneName
    ZoneName="PiXian"
    print("PiXian is famous for the chili paste!")
    level=4

#大邑县
def DaYiInfo():
    global level,ZoneName
    ZoneName="DaYi"
    print("DaYi is close to XiNing Snow Mountain!")
    level=4


#错误信息
def errhandler ():
   print ("Your input has not been recognised")

#选择省份，比如河南，四川
def ChooseProvince():
    global level,action1
    action1=input("Please choose your Options, or q to quit: ")
    ProvinceAction.get(action1,errhandler)()


#选择河南省的城市
def ChooseCityHeNan():
    global level,action2
    action2 = input("Chose your option, or press b to back or q to quit: ")
    HeNanAction.get(action2, errhandler)()

#选择四川省的城市
def ChooseCitySichuan():
    global level,action2
    action2 = input("Chose your option, or press b to back or q to quit:  ")
    SiChuangAction.get(action2, errhandler)()

def ChooseZoneChengdu():
    global level,action3
    action3 = input("Please choose your destination, or press b to back or q to quit:")
    ChengduAction.get(action3,errhandler)()

def destination():
    global action4
    action4 = input("You arrived the destination, please press b to retrun or q to quit!")
    if action4=='b': Back()
    elif action4=='q':sys.exit()

ProvinceAction = {
    "1": HeNanInfo,
    "2": SichuanInfo,
    "b": Back,
    "q": sys.exit
    }

HeNanAction={
    "1":LuoHeInfo,
    "b":Back,
    "q":sys.exit
}

SiChuangAction={
    "1":ChengduInfo,
    "b":Back,
    "q":sys.exit
}

LuoHeAction={
    "1":WuYangInfo,
    "b":Back,
    "q":sys.exit


}

ChengduAction={
    "1":DaYiInfo,
    "2":PiXianInfo,
    "b":Back,
    "q":sys.exit
}


#显示省份信息
print("--------------")

ProvinceInfo()

ChooseProvince()

while True:
#    print("\naction1",action1)
#    print("action2",action2)
#    print("action3",action3)
#    print("level",level)

#如果是河南省
    if action1=='1':
        ChooseCityHeNan()
#如果是漯河
        if action2=='1':
            action3=input("Please choose your destination, or press b to back or q to quit:")
#如果是舞阳
            if action3=='1':
                WuYangInfo()
                destination()
            elif action3=='b':
                Back()

#如果是四川省
    elif action1=='2':
#如果是成都市
        if level <3:
            ChooseCitySichuan()
        elif level >=3 and action2=='1':

            ChooseZoneChengdu()
            destination()




