#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li

#一级菜单 四川，河南，直辖市
#二级菜单：成都，自贡，漯河，北京，重庆
#三级菜单：大邑县，郫县，富顺县，海淀区，渣滓洞

China={
    "SiChuan":{"Chengdu":{"DaYiXian":"Nice Hot Spring!","PiXian":"Famous chili source"},"ZiGong":{"FuShun":"Product of Salt"}},
    "HeNan":{"LuoHe":{"WuYang":"Small Town","WuGang":"Beautiful!"}},
    "Municipality":{"BeiJing":{"HaiDian":"Most Famous Zone."},"ChongQing":{"ZaZiDong":"History site"}}

}
CityName=""
level=""
direction="down"
#Print out Province Name

while True:
    print("--------China Map Sample---------")
    for i in China:
        print(i)

    ProvinceName=input("Please Input the Province Option: ")
    if ProvinceName in China:
        cities=China[ProvinceName].keys()
#        print("Debug cities:",cities)
# Print out City Name

        while True:
            print("-----Province",ProvinceName,"Map---------")
            for i in cities:
                print(i)
            CityName=input("Please input the City Option:　")
    # Print out Zone Name
            if CityName in cities:
                Zone=China[ProvinceName][CityName].keys()
                #print("Debug Zones: ",Zone)
                level=2
                direction="down"

                while True:
                    print("---------City",CityName,"Map-----------")
                    for j in Zone:
                        print(j)
                    DestinationName = input("Please input the destination Option: ")
                           # Print out Zone Information

                    if DestinationName in Zone:
                        info = China[ProvinceName][CityName][DestinationName]
                        while True:
                            print("Destination Info: ", info)
                            level = 3
                            choice = input("Please press b to back or q to quit!")

                            if choice == 'b':
                                direction = "up"
                                break

                            elif choice == 'q':
                                exit()
                    elif DestinationName == 'b':
                        break
                    elif DestinationName == 'q':
                        exit()

                    else:

                        print("Wrong Zone Name, Please enter again:　")

            elif CityName=='b':
                break
            elif CityName=='q':
                exit()

    elif ProvinceName=='q': exit()
    else:
        print("Please input the correct Command!")


