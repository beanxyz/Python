#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li

import time

print(time.time()) #时间戳，1970年到现在的秒数

print(time.ctime()) #当前系统时间字符串格式
print(time.ctime(time.time()-86400)) #根据时间戳算时间
print(time.gmtime())
time_obj=time.gmtime()
#显示的是格林威治时间
print(time_obj.tm_year,time_obj.tm_mon)
#显示本地时间
print(time.localtime())
#必须传入一个时间对象的参数，把structure time转换成时间戳
print(time.mktime(time_obj))
#延时多少秒
time.sleep(4)

#把时间对象转成字符串格式
print(time.strftime("%Y-%m-%d %H:%M:%S",time_obj))

#把字符串格式转换为时间对象
tm=time.strptime("2016-05-10 15:04:20","%Y-%m-%d %H:%M:%S")
print(tm)

print(time.mktime(tm))



print("--------------")


import  datetime
print(datetime.date.today())#输出当前日期
currenttime=datetime.datetime.now()#输出当前时间，最常用
print(currenttime)

#比当前时间加10天
new_date=datetime.date.today()+datetime.timedelta(days=10)
print(new_date)

#比当前时间少1个小时
new_date=datetime.datetime.now()+datetime.timedelta(hours=-1)
print(new_date)

#直接替换
print(currenttime.replace(2014,9,12))
print(currenttime.replace(year=2015))

time_obj=currenttime.replace(2015)

print(time_obj,type(time_obj))
print(currenttime>time_obj)