#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li

salary=input("input your salary:")
if salary.isdigit():
    salary=int(salary)
else:
    exit("Invalid")


welcome_msg="Welcome to Shopping Mall".center(50,'-')
print(welcome_msg)
product_list=[
    ('iphone',5888),
    ('Mac Air',8000),
    ('Mac Pro',9000),
    ('XiaoMi 2',19.9),
    ('Coffee',30),
    ('Telsla',820000),
    ('Bike',700),
    ('Cloth',200)
]

shop_cart=[]

exit_flag=False
while exit_flag is not True:
    print("production list".center(50,'-'))
    for item in enumerate(product_list):
        index=item[0]
        p_name=item[1][0]
        p_price=item[1][1]
        print(index,p_name,p_price)

    user_choice=input("[q=quit,c=check]What do you want to Buy:")
    if user_choice.isdigit():
#Choose goods
        user_choice=int(user_choice)
        if user_choice < len(product_list):
            p_item=product_list[user_choice]
            if p_item[1] <= salary:
#affordable
                shop_cart.append(p_item)
                salary-=p_item[1]
                print("Added [%s] into shop cart, your current balance is [%s]" %
                      (p_item,salary)
                      )
            else:
                print("Your balance is [%s], cannot afford this," %salary)

    else:
        if user_choice == 'q' or user_choice == 'quit':
            print("purchased products as below".center(40,'*'))
            for item in shop_cart:
                print(item)
            print("End".center(40,'*'))
            print("Your Balance is %s"%salary)
            exit_flag=True
        elif user_choice=='c' or user_choice=='check':
            print("purchased products as below".center(40, '*'))
            for item in shop_cart:
                print(item)
            print("End".center(40, '*'))


