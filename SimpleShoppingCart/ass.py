#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li


#salary=input("Please input your salary")
#if salary.isdigit():
#    salary=int(salary)

# userinfo={
#     1:{
#         'name':'Alex',
#         'password':'password',
#         'balance':99999
#     },
#     2:{'name':'Jay',
#        'password':'pp',
#        'balance':9999
#        },
#     3:{'name':'Yuan',
#        'password':'hhh',
#        'balance':99999
#        }
# }


import json
import time
import os
# with open('result.json', 'w') as fp:
#     json.dump(userinfo, fp)

userIndex=''
fp=open('result.json','r+')
userinfo=json.load(fp)
history={}
info=userinfo.values()


login_flag=False

while login_flag is False:
    usr=input("Please input your username:")
    pwd=input("Please input your password:")


    for user in info:
        #print(user['name'],user['password'])
        balance=user['balance']
        if user['name']==usr and user['password']==pwd:
            print("Login Successfully!")
            print("Your Balance is ",balance)
            login_flag=True
            break
        else:
            continue




    if login_flag is True:
        for k, v in userinfo.items():
            #print(k, v)
            if usr in v['name'] and pwd in v['password']:
                #print("User %s key is "%usr, k)
                userIndex=k
    else:
        print("Login Failed. Please try again")



menu= [
    {"category":"Car",
     "products":[
         {"name":"Mazda3","price":120000},
         {"name":"BMW6","price":400000},
         {"name":"Golf","price":20000},
     ]
    },
    {"category":"Furtunre",
     "products":[
         {"name":"Table","price":500},
         {"name":"Wardrobe","price":600},
         {"name":"Chair","price":200},
     ]
     },

    {"category":"Computer",
     "products":[
         {"name":"Surface Pro3","price":6000},
         {"name":"Macbook Pro","price":9000},
         {"name":"Dell laptop","price":5000},
     ]
     },

    ]


category_flag=False
shop_cart=[]


while category_flag is not True and login_flag is True:

    print("Welcome to the Shopping Center".center(40, '-'))

    for item in enumerate(menu):
        index=item[0]
        category=item[1]["category"]
        print(index,category)


    print("End".center(40,'-'))
    category=input("Choose your Shopping Category (digit:shopping;'q':quit;'c':checkout; 'h':history display):")

    if category.isdigit():
        if int(category)<len(menu):
            p_item=menu[int(category)]['products']

            for car_item in enumerate(p_item):
                index=car_item[0]
                name=car_item[1]['name']
                price=car_item[1]['price']
                print(index,name,price)





            productid=input("please choose the product number")
            number=input("please choose how many do you want?")
            if number.isdigit():
                number=int(number)
            if productid.isdigit():
                productid=int(productid)

            #print(p_item[productid]['name'],p_item[productid]['price'])
            s1={}
            s1['name']=p_item[productid]['name']
            s1['price']=p_item[productid]['price']
            s1['number']=number
            #     shop_cart.append(p_item[productid]['name'])

            shop_cart.append(s1)



        else: print("You input an invalid number, please try again")

    elif category=='c':
        print("You Purchase summary".center(40,'-'))
        #print(shop_cart)
        totalcost=0

        print("Name   Quantity   Price/Unit")
        for item in shop_cart:
            print((item['name'],item['number'],int(item['price'])))
            totalcost+=int(item['price'])*int(item['number'])
        print("The Total cost is %s, your balance is %s "%(totalcost,balance))
        if totalcost>balance:
            print("Sorry, you don't have enough balance")

            charge=input("Do you want charge your balance?(y=charge/n=quit)")


            if charge=='y':
                money=input("please input the how much money you want to charge: ")
                if money.isdigit():
                    money=int(money)

                else: print("Invalid type")

                balance=balance+money

        else:
            Confirm=input("Do you want to checkout? (y/n)")
            if Confirm=='y':
                balance=balance-totalcost

            # 更新用户余额，保存到result.json
            print("Your balance will be updated.")
            userinfo[userIndex]['balance']=balance

            fp = open('result.json', 'w')
            json.dump(userinfo, fp)

            #获取当前时间，保存到user_history.json
            checkouttime=time.strftime("%d/%m/%Y %H:%M:%S")
            d=dict()
            d[checkouttime]=shop_cart
            print(d)
            filename="%s_history.json"%usr

            if os.path.isfile(filename):
                #print("History file exists, it will be updated")
                fp=open(filename,'r')
                file=json.load(fp)
                file[checkouttime]=shop_cart

                fp=open(filename,'w')
                json.dump(file,fp)

                print("Thanks for Shopping. See you next time!:)")
                exit()

            else:
                fp = open(filename, 'w')
                json.dump(d, fp)

                #login_flag=True
                print("Thanks for Shopping. See you next time!:)")
                exit()



        #with open('purchase.json', 'w') as fp:
        # json.dump(shop_cart, fp)

    elif category=='h':
        print("Your history shopping record".center(40,'-'))
        filename = "%s_history.json" % usr
        fp = open(filename, 'r')
        historyinfo=json.load(fp)
        #print(historyinfo)
        for i in sorted(historyinfo):
            print(i,historyinfo[i])

    elif category == 'q':
        print("See you next time!")
        exit()
