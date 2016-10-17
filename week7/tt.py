# print ("Welcome to the Student Management Program")
# import pickle
# class Student:
#     def __init__ (self, name, age, gender):
#          self.name   = name
#          self.age    = age
#          self.gender = gender
#
#
#
#
# a =[];
# while True:
#
#     choice = int(input("Make a Choice: "))
#     if (choice==1):
#
#         name = input("Enter Name: ")
#         age = input("Enter Age: ")
#         sex = input("Enter Sex: ")
#
#         s = Student(name, age, sex)
#         a.append(s)
#
#     elif(choice==2):
#
#         pickle.dump(a, open('file', 'wb'))
#
#     elif(choice==3):
#
#         for item in a:
#             print(item.name,item.age,item.gender)
#
#     elif (choice==4):
#
#         fp = pickle.load(open('file', 'rb'))
#         print(fp)
#         for item in fp:
#             print(item.name)
#
#
#
#
import random
import sys
import time


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()  # defeat buffering
        time.sleep(random.random() * 0.1)


msg = """
故事即将开始，John经过努力，成功的考入了本市的一所大学。
在大学的新生晚会上，John意外邂逅了一个美丽的女孩Liz
现在，我们将镜头切换到John

John（心理活动）:好靓的妞儿，我要去认识一下！
"""

slowprint(msg)
