#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li


number=25
counter=0

for i in range(10):

    counter+=1
    if counter <= 3:
        guess=int(input("Input your guess number please "))
        if guess == number:
            print("Correct")
            break
        elif guess > number:
            print("Please guess smaller")
        else:
            print("Please guess bigger")
    else:
        confirm=input("Do you want to continue. y/n")
        if confirm == "y":
            counter =0
            continue
        else:
            print("Bye")
            break