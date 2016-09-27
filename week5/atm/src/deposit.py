#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li

#根据用户文件，自动充值


import os,json,logging
parent_path=os.path.abspath(os.path.pardir)
loglocation_file=os.path.join(parent_path,'config','userfilelocation.conf')

def auto_deposit():
    fp=open(loglocation_file,'r')
    for line in fp:
        #每一行line都是一个用户信息文件的地址

        fp1=open(line.strip(),'r')
        temp=json.load(fp1)
        if temp['auto_deposit']>0:
            temp['balance']+=temp['auto_deposit']
            fp1=open(line.strip(),'w')
            json.dump(temp,fp1)
            print("账户%s自动充值%s"%(temp['id'],temp['auto_deposit']))

            lst=line.split("\\")[0:-2]
            temp_path="\\".join(lst)
            logfile_path=os.path.join(temp_path,'log','user.log')
            logging.basicConfig(filename=logfile_path, level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
            logging.info("Account%s auto desposit %s"%(temp['id'],temp['auto_deposit']))

    fp.close()

auto_deposit()
