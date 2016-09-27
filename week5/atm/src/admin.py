#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li

LOGIN_USER={"is_login":False,"user_id":"0"}

import os,json
import logging


parent_path=os.path.abspath(os.path.pardir)
# ttt=os.path.join(parent_path,"config",'atm.config')

#通过配置文件获取管理员和用户文件的路径

if not os.path.isfile(os.path.join(parent_path,"config",'atm.config')):
    exit("配置文件不存在！")


fp=open(os.path.join(parent_path,"config",'atm.config'),'r',encoding="utf-8")
for line in fp:
    temp=line.split("=")
    if temp[0].strip()=="ADMIN_FILEPATH":
        ADMIN_FILEPATH=os.path.abspath(temp[1].strip())
    if temp[0].strip()=='ADMIN_LOG':
        ADMIN_LOG=os.path.abspath(temp[1].strip())
    if temp[0].strip()=="Client_Path":
        # Client_Path=parent_path+"\\"+temp[1].strip()
        Client_Path=os.path.abspath(temp[1].strip())


#定义一个装饰器判断是否登录
def outer(func):
    def inner(*args, **kwargs):
        if LOGIN_USER['is_login']:
            r = func(*args,**kwargs)
            return r
        else:
            print("警告：管理员请登录\n")
            login()

    return inner

#新建一个账户
@outer
def create_user():
    """
    输入用户的账户，姓名，密码，预存款值
    :return:
    """
    import os,json
    print("请根据提示输入用户资料\n")
    account_id=input("请输入账号")
    account_name=input("请输入姓名")
    account_pwd=input("请输入密码")

    while True:
        balance=input("请输入预存额度")

        if balance.isdigit():
            balance=int(balance)
            break
        else:
            print("请输入合法的数字")


#创建账户对应的文件夹和日志记录
    userprofile=os.path.join(Client_Path,account_id,'record')
    userlog=os.path.join(Client_Path,account_id,'log')

    fp=open(os.path.join(parent_path,'config','loglocation.conf'),'a')
    fp.write(os.path.join(userlog,'user.log')+"\n")

    fp=open(os.path.join(parent_path,'config','userfilelocation.conf'),'a')
    fp.write(os.path.join(userprofile,'user_info.json')+"\n")

    if os.path.isdir(userprofile):
        print("该用户已经存在！")
        return 0

    #makedirs可以递归的创建文件夹,mkdir只有一个文件夹
    os.makedirs(userprofile)
    os.makedirs(userlog)

#用户的基本信息，包括姓名，密码，账号，余额，状态和自动存款
    information={
    'name':account_name,
    'pwd':account_pwd,
    'id':account_id,
    'balance':balance,
    'status':'active',
    'auto_deposit':0
    }

    fp=open(os.path.join(Client_Path,account_id,'record','user_info.json'),'w')
    json.dump(information,fp)

#删除账户，需要删除对应的文件夹和日志中的路径
@outer
def delete_user():
    import os,json,shutil
    account_id=input("请输入要删除用户的账户\n>>>>")

    if not os.path.isdir(os.path.join(Client_Path,account_id)):
        print("该用户账户不存在！")
        return False

    while True:
        Confirm=input("请确认删除（y/n)!\n>>>>")
        if Confirm=='y':
            profile=os.path.join(Client_Path,account_id)
            shutil.rmtree(profile)
            logging.basicConfig(filename=ADMIN_LOG, level=logging.INFO,
                                format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

            logging.warning('Administrator Deleted account %s' %account_id)
            print("账户%s已经删除"%account_id)

#下面的操作是通过重新写一个新的文件，来删除旧文件中的用户路径记录
            with open(os.path.join(parent_path,'config','userfilelocation.conf'),'r') as old,open(os.path.join(parent_path,'config','temp'),'w') as new:

                for line in old:

                    pathname=line.strip()
                    if os.path.isfile(pathname):
                        new.write(line)
                    else:
                        print("%s not found"%pathname)


            #删除原先的记录，重命名新的
            os.remove(os.path.join(parent_path,'config','userfilelocation.conf'))
            os.rename(os.path.join(parent_path,'config','temp'),os.path.join(parent_path,'config','userfilelocation.conf'))

            return True

        elif Confirm=='n':
            return False
        else:
            print("请输入合法字符！\n")



    print("该账户档案已经删除！")


#输入账户，查询相关信息
@outer
def query_user():
    import os, json
    # 输入关键字查询相关人员的信息
    logging.basicConfig(filename=ADMIN_LOG, level=logging.INFO,
                        format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    account_id=input("请输入用户的账号信息")
    if not os.path.isdir(os.path.join(Client_Path,account_id)):
        print("该用户账户不存在！")

    else:
        fp=open(os.path.join(Client_Path,account_id,'record','user_info.json'),'r')
        temp=json.load(fp)
        logging.warning('Administrator query info of account %s' %temp['name'])
        print("姓名{name},账户ID{id},余额{balance},状态{status}".format(name=temp['name'],id=temp['id'],balance=temp['balance'],status=temp['status']))





#锁住账户，这样该账户登录之后无法进行任何金钱相关的操作
@outer
def lockuot_user():

    import os, json
    # 输入关键字查询相关人员的信息
    account_id=input("请输入用户的账号信息")
    if not os.path.isdir(os.path.join(Client_Path,account_id)):
        print("该用户账户不存在！")

    else:
        fp = open(os.path.join(Client_Path, account_id, 'record', 'user_info.json'), 'r')
        temp = json.load(fp)

        while True:
            choice=input("请确认冻结该账户(Y/N)")
            if choice=="Y" or choice=='y':
                logging.warning('Administrator Changed account %s status to inactive' % (temp['name'] ))
                temp['status']='inactive'
                fp = open(os.path.join(Client_Path, account_id, 'record', 'user_info.json'), 'w')
                json.dump(temp,fp)
                return True
            elif choice=='N' or choice=='n':
                return False
            else:
                print("请输入合法字符\n")


#更改用户的余额
@outer
def updateCredit_user():

    import os, json
    # 输入关键字查询相关人员的信息
    account_id=input("请输入用户的账号信息")
    if not os.path.isdir(os.path.join(Client_Path,account_id)):
        print("该用户账户不存在！")

    else:
        fp = open(os.path.join(Client_Path, account_id, 'record', 'user_info.json'), 'r')
        temp = json.load(fp)

        print("用户%s当前余额%d"%(temp['name'],temp['balance']))
        while True:
            new_balance=input("请输入新的余额数目\n>>>>>")
            if new_balance.isdigit():
                new_balance=int(new_balance)
                break

            else:
                print("请输入合法的数字！\n")

        logging.basicConfig(filename=ADMIN_LOG, level=logging.INFO,
                            format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        while True:
            choice=input("请确认更新该用户余额(Y/N)")
            if choice=="Y" or choice=='y':
                logging.warning('Administrator Changed account %s balance from %d to %d ' % (temp['name'], temp['balance'],new_balance))
                temp['balance']=new_balance
                fp = open(os.path.join(Client_Path, account_id, 'record', 'user_info.json'), 'w')
                json.dump(temp,fp)

                return True

            elif choice=='N' or choice=='n':
                return False
            else:
                print("请输入合法字符\n")


#管理员登录
def login():
    import os,json
    logging.basicConfig(filename=ADMIN_LOG, level=logging.INFO,
                        format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    if not os.path.isfile(ADMIN_FILEPATH):
        print("错误！用户文件不存在，请创建新用户！")
        return False
    userIndex = ''

    fp = open(ADMIN_FILEPATH, 'r+')
    userinfo = json.load(fp)

    info = userinfo.values()

    login_flag = False

    counter = 0
    while login_flag is False:
        usr = input("请输入用户名:")
        pwd = input("请输入密码:")
        global LOGIN_USER
        for user in info:

            if user['name'] == usr and user['password'] == pwd:
                print("登录成功!".center(40, '-'))
                print("\n")

                login_flag = True

                LOGIN_USER['is_login']=True
                break
            else:

                continue


        if login_flag==False:
            print("登录失败\n")

                # logging.info('So should this')
            logging.warning('Administrator Login Failed')

        else:
            logging.info('Administrator Login Successfully')
                # break


#初始化界面
def init():
    msg="""
    1.登录
    2.注册新用户
    3.删除用户
    4.冻结用户
    5.更改用户信用额度
    6.查看用户信息
    7.退出
    """


    flag=True
    while True:
        print('欢迎使用ATM管理系统'.center(40, '-'))
        print(msg)
        choice=input("请输入选项\n>>>>")
        if choice=='1':login()
        elif choice=='2':create_user()
        elif choice=='3':delete_user()
        elif choice=='4':lockuot_user()
        elif choice=='5':updateCredit_user()
        elif choice=='6':query_user()
        elif choice=='7':exit("谢谢使用ATM管理系统")



def run():
    init()

# run()