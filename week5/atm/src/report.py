#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li
import os,datetime,time
parent_path=os.path.abspath(os.path.pardir)
loglocation_file=os.path.join(parent_path,'config','loglocation.conf')


#根据日志生成过去30天的报告记录，报告记录以当天时间命名
def Generate_report():
    fp=open(loglocation_file,'r')
    for line in fp:
        log_name=line.strip()
        temp=log_name.split('\\')
        x=temp[0:-1]
        log_address="\\".join(x)
        new_name=log_address+"\\"+str(datetime.date.today())
        print(log_name,type(log_name))
        last_month = datetime.datetime.today() + datetime.timedelta(days=-30)
        # print(new_date)

        if not os.path.isfile(log_name):pass
        else:
            with open(log_name,'r') as old,open(new_name,'w') as new:
                for line1 in old:
                    t=line1.split(" ")

                    ts=datetime.datetime.strptime(t[0], "%m/%d/%Y")
                    if ts<last_month:
                        print("记录:%s"%line1)
                        new.write(line1)




Generate_report()