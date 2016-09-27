#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li
import os,logging,sys,json
import schedule


LOGIN_USER={"is_login":False,"user_id":'anonymous',"status":'active'}

#获取atm目录的绝对路径
parent_path = os.path.abspath(os.path.pardir)

#装饰器判断用户是否登录
def outer(func):
    def inner(*args, **kwargs):
        if LOGIN_USER['is_login']:
            r = func(*args,**kwargs)
            return r
        else:
            print("请登录".center(40,'-'))
            login()

    return inner

#装饰器判断用户是否被冻结
def outer1(func):
    def inner(*args, **kwargs):
        if LOGIN_USER['status']=="active":
            r = func(*args,**kwargs)
            return r
        else:
            print("该用户账户被冻结，无法进行金钱操作".center(40,'-'))


    return inner

#登录
def login():
    global LOGIN_USER

    user_id=input("请输入卡号\n>>>>")
    user_profile = os.path.join(parent_path, 'db', 'user', user_id)

    if not os.path.isdir(user_profile):
        print("该用户ID不存在")
        return False

    logging.basicConfig(filename=os.path.join(parent_path,'db','user',user_id,'log','user.log'), level=logging.INFO,
                        format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


    LOGIN_USER['user_id']=user_id
    user_password=input("请输入密码\n>>>>")
    fp=open(os.path.join(parent_path,'db','user',user_id,'record','user_info.json'),'r')
    temp=json.load(fp)
    if temp['id']==user_id and temp['pwd']==user_password:
        print("用户{}登录成功！".format(temp['name']))
        LOGIN_USER['is_login']=True
        LOGIN_USER['status']=temp['status']
        logging.info("Account {}  login successfully".format(temp['id']))
        return True
    else:
        print("用户名或者密码错误!\n")
        logging.warning("Account {} login Failed".format(temp['id']))
        return False


#存钱
@outer1
@outer
def save():
    path = os.path.join(parent_path, 'db', 'user', LOGIN_USER['user_id'], 'record', 'user_info.json')
    # print(path)
    fp = open(path, 'r')
    temp = json.load(fp)
    logging.basicConfig(filename=os.path.join(parent_path, 'db', 'user', LOGIN_USER['user_id'], 'log', 'user.log'),
                        level=logging.INFO,
                        format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    while True:
        print("您当前余额是%d" % temp['balance'])
        save_money=input("请输入你需要存钱的金额\n>>>>>>>")
        if save_money.isdigit():
            save_money=int(save_money)
            break
        else:
            print("请输入合法的数字")
            continue


    new_balance=temp['balance']+save_money
    temp['balance']=new_balance

    print("您的余额现在是{}".format(new_balance))
    fp = open(path, 'w+')
    json.dump(temp, fp)
    print("存钱成功！")
    logging.info("Account {} deposit {}, current balance is {}".format(temp['id'],save_money,temp['balance']))

#取钱
@outer1
@outer
def withdraw():
    path = os.path.join(parent_path, 'db', 'user', LOGIN_USER['user_id'], 'record', 'user_info.json')
    # print(path)
    fp = open(path, 'r')
    temp = json.load(fp)

    logging.basicConfig(filename=os.path.join(parent_path, 'db', 'user', LOGIN_USER['user_id'], 'log', 'user.log'),
                        level=logging.INFO,
                        format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    while True:
        print("您当前余额是%d"%temp['balance'])
        withdraw_money=input("请输入你需要取钱的金额\n>>>>>")
        if withdraw_money.isdigit():
            withdraw_money=int(withdraw_money)
            break
        else:
            print("请输入合法的数字")
            continue


    if withdraw_money>temp['balance']:
        print("超过余额限制，请重新输入！\n")
    else:
        new_balance=temp['balance']-withdraw_money
        print("剩余金额{}".format(new_balance))
        temp['balance']=new_balance

        fp = open(path, 'w+')
        json.dump(temp,fp)
        print("取钱成功！")
        logging.info("Account {} withdrawl {}, current balance is {}".format(temp['id'],withdraw_money,temp['balance']))


#转账
@outer1
@outer
def transfer():
    path = os.path.join(parent_path, 'db', 'user', LOGIN_USER['user_id'], 'record', 'user_info.json')
    receive_id=input("请输入对方的账号信息\n>>>>>")
    receiver_profile = os.path.join(parent_path, 'db', 'user', receive_id)
    if not os.path.isdir(receiver_profile):
        print("对方账户不存在！")
        return False
    if receive_id==LOGIN_USER['user_id']:
        print("不可以转钱给当前登录账户")
        return False

    re_fp=open(os.path.join(receiver_profile,'record','user_info.json'),'r')
    se_fp=open(path,'r')
    temp1=json.load(re_fp) #收款人
    temp2=json.load(se_fp) #当前用户

    while True:
        tran_money=input("请输入转账的金额\n>>>>>")
        if tran_money.isdigit():
            tran_money=int(tran_money)
            break
        else:
            print("请输入合法的数字")
            continue

    if tran_money>temp2['balance']:
        print("超过余额限制，请重新输入！\n")
    else:
        #当前账户减去金钱
        new_balance=temp2['balance']-tran_money
        print("当前账户剩余金额{}".format(new_balance))
        temp2['balance']=new_balance

        se_fp = open(path, 'w+')
        json.dump(temp2,se_fp)

        #对方账户添加金钱
        new_balance2=temp1['balance']+tran_money
        temp1['balance']=new_balance2
        re_fp = open(os.path.join(receiver_profile, 'record', 'user_info.json'), 'w')
        json.dump(temp1,re_fp)

        print("转钱成功！")

        #在本地账户和对方账户的日志中分别添加记录，注意需要去掉handler才可以更改日志文件
        logging.basicConfig(filename=os.path.join(parent_path, 'db', 'user', LOGIN_USER['user_id'], 'log', 'user.log'),
                            level=logging.INFO,
                            format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logging.info("Account {} transfered {} to {}".format(temp2['id'],tran_money,temp1['id']))

        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        logging.basicConfig(filename=os.path.join(parent_path, 'db', 'user', temp1['id'], 'log', 'user.log'),
                            level=logging.INFO,
                            format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logging.info("Account {} received {} from {}".format(temp1['id'],tran_money,temp2['id']))


#该账户所有的历史操作记录
@outer
def report(user_id=LOGIN_USER['user_id']):
    print("账号{}历史记录".format(LOGIN_USER['user_id']))
    log_path=os.path.join(parent_path, 'db', 'user', LOGIN_USER['user_id'], 'log', 'user.log')

    if not os.path.isfile(log_path):
        print("目前没有任何交易记录")
        return False
    fp=open(log_path,'r')
    for line in fp:
        print(line.strip())


#设置自动充值的金额，然后deposit.py会根据设定的值进行存钱操作
@outer1
@outer
def autosave():

    while True:
        auto_money = input("请输入你每月自动充值的金额数目\n>>>>>>")
        if auto_money.isdigit():
            auto_money=int(auto_money)
            break
        else:
            print("请输入一个合法的金额数量")

    path = os.path.join(parent_path, 'db', 'user', LOGIN_USER['user_id'], 'record', 'user_info.json')
    # print(path)
    fp = open(path, 'r')
    temp = json.load(fp)
    logging.basicConfig(filename=os.path.join(parent_path, 'db', 'user', LOGIN_USER['user_id'], 'log', 'user.log'),
                        level=logging.INFO,
                        format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


    temp['auto_deposit']=auto_money
    fp=open(path,'w')
    json.dump(temp,fp)

    logging.info("User {} setup auto deposite {} per month".format(temp['name'],auto_money))

#初始化界面
def init():

    parent_path = os.path.abspath(os.path.pardir)
    if not os.path.isfile(os.path.join(parent_path, "config", 'atm.config')):
        exit("配置文件不存在！")

    fp = open(os.path.join(parent_path, "config", 'atm.config'), 'r', encoding="utf-8")
    for line in fp:
        temp = line.split("=")
        if temp[0].strip() == "ADMIN_FILEPATH":
            ADMIN_FILEPATH = os.path.abspath(temp[1].strip())
        if temp[0].strip() == 'ADMIN_LOG':
            ADMIN_LOG = os.path.abspath(temp[1].strip())
        if temp[0].strip() == "Client_Path":
            # Client_Path=parent_path+"\\"+temp[1].strip()
            Client_Path = os.path.abspath(temp[1].strip())


    msg="""
    1.登录
    2.充值
    3.取钱
    4.转账
    5.历史记录
    6.设置自动充值
    7.退出
    """

    schedule.every()

    print("欢迎使用ATM用户系统")
    while True:
        print(msg)
        choice=input("请输入选项：\n>>>>>")

        if choice=='1':login()
        elif choice=='2':save()
        elif choice=='3':withdraw()
        elif choice=='4':transfer()
        elif choice=='5':report()
        elif choice=='6':autosave()
        elif choice=='7':exit()



def run():
    init()

# run()