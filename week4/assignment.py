
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan L

"""
作业要求
普通用户：登录，注册，修改密码，查看本用户信息；
管理员：登录，注册，修改密码，查看本用户信息；
        修改，添加普通用户
        修改普通用户密码
        查看普通用户
        提供普通用户权限

---------------------------
基本思路：

读取用户的json文件，获取姓名，密码，邮件，权限
该文件如果不存在，自动创建默认存在的用户为管理员admin，admin，admin@localhost, privilege:admin

基本格式：
{
1:{user:alex,password:123,email:alex@gmail.com, privilege:standard},
2:{user:James,password:222,email:james@163.com,privilege:admin},
...
}

1. 后台管理
    -更改密码和邮箱地址
    -查看本用户信息
    -更改权限 （管理员）
    -查询用户 （管理员）
    -创建新用户(管理员）
    -删除旧用户（管理员）
2. 登录
3. 注册

"""


# 伪代码

import json

LOGIN_USER={"is_login":False,"user_type":"standard","user_id":"0","user_name":"anonyoumous"}


#装饰器-用户登录判断
def outer(func):
    def inner(*args, **kwargs):
        if LOGIN_USER['is_login']:
            r = func(*args,**kwargs)
            return r
        else:
            print("请登录".center(40,'-'))

    return inner


#装饰器-管理员登录判断
def outer1(func):
    def inner(*args, **kwargs):
        if LOGIN_USER['is_login'] and LOGIN_USER['user_type'] == "admin":
            r = func(*args,**kwargs)
            return r
        else:
            print("请登录,或者权限不够".center(40,'-'))
    return inner

#第一个默认的管理员账户
def testfile():
    userinfo={
        1:{
            'name':'admin',
            'password':'admin',
            'email':'admin@localhost',
            'privilege':'admin'

        },
    }
    import json
    import os
    with open('users.json', 'w') as fp:
         json.dump(userinfo, fp)


#输出当前用户的信息
@outer
def Infos():
    print("欢迎%s" % LOGIN_USER["user_name"])
    userid = LOGIN_USER["user_id"]
    fp = open('users.json', 'r')
    info = json.load(fp)
    print("你的个人信息如下所示：")
    print("用户名%s 密码%s 邮件%s 访问权限%s\n"%(info[userid]['name'],info[userid]['password'],info[userid]['email'],info[userid]['privilege']))
    return True

#修改当前用户密码和邮件
@outer
def ChangePwd():
    import json
    #判断读取Json文件，通过useId获取用户的value
    """
    """
    print("欢迎%s"%LOGIN_USER["user_name"])
    newpwd=input("请输入你的新密码")
    userid=LOGIN_USER["user_id"]
    newemail = input("请输入你的新邮件")
    #     userid = LOGIN_USER["user_id"]

    fp=open('users.json','r')
    info=json.load(fp)
    info[userid]["password"]=newpwd
    info[userid]["email"] = newemail

    fp=open('users.json','w')
    json.dump(info,fp)
    print("修改成功！".center(40,'-'))


#更改指定用户的权限
@outer1
def ChangePrivilege():

    print("欢迎%s" % LOGIN_USER["user_name"])
    username=input("请输入用户的账户")
    user_index=0

    if not QueryUser(username):
        print("该用户不存在！")
        return False


    fp=open('users.json','r')
    temp=json.load(fp)
    userinfo=temp.values()
    for k, v in temp.items():
        if v['name']==username:
            user_index=k
            # print(user_index,type(user_index))

    while True:
        pri=input("请输入权限（standard/admin)")
        if not pri in ["standard","admin"]:
            print("错误指令，请重新输入")
        else:
            break

    fp.close()
    fp=open('users.json','w')
    temp[user_index]["privilege"]=pri
    json.dump(temp,fp)
    return True


#关键字查询用户信息
@outer1
def QueryUser(user_keywords):
    import os,json
    #输入关键字查询相关人员的信息

    # user_keywords=input("请输入关键字查询")
    # LOGIN_USER = {"is_login": False, "user_type": "standard", "user_id": "0", "user_name": "anonyoumous"}

    if not os.path.isfile('users.json'): return False
    fp=open('users.json')
    info=json.load(fp)
    values=info.values()
    query_flag=False
    for users in values:

        try:
            if (user_keywords in users['name']) or (user_keywords in users['email']) or (user_keywords in users['privilege']):
                print("匹配到相关信息:账户%s 邮箱%s 权限%s"%(users['name'],users['email'],users['privilege']))
                query_flag=True


        except:
            print("错误信息，无法找到")

    if query_flag==False:
        print("没有找到搜索的信息")
        return False
    else:
        return True

#删除指定用户
def deluser():
    print("欢迎%s" % LOGIN_USER["user_name"])
    username = input("请输入用户的账户")
    user_index = 0
    if not QueryUser(username):
        print("该用户不存在！")
        return False

    fp = open('users.json', 'r')
    temp = json.load(fp)
    userinfo = temp.values()
    for k, v in temp.items():
        if v['name'] == username:
            user_index = k
            # print(user_index, type(user_index))

    if user_index==0:
        print("用户不存在")
        return False
    del temp[user_index]


    fp=open('users.json','w')
    json.dump(temp,fp)
    print("删除%s成功"%username)
    return True


#注册新用户
def register():
    #判断文件是否存在，不存在，创建一个新的；存在的话，判断用户是否存在；

    import json,os


    if not os.path.isfile("users.json"):
        print("用户文件不存在，创建第一个默认的管理员账户admin")
        testfile()
        return True

    else:

        username = input("请创建用户名:")
        fp=open('users.json','r+')
        userinfo=json.load(fp)
        value=userinfo.values()
        fp.close()
        user_flag=False
        for user in value:
            if username == user["name"]:
                # print("This account is already in use. Please create a new account!")
                user_flag=True
            else:
                continue

        if user_flag:
            print("该账户已经被使用，请重新创建新账号!")

        else:

            pwd=input("请创建密码:")
            email=input("请输入邮箱地址")

            new_userinfo="{'name':'%s','password':'%s','email':'%s','privilege':'standard'}"%(username,pwd,email)
            #把字符串转换为字典
            dicformat=eval(new_userinfo)
            #添加信息
            #获取用户index
            maxid=max(userinfo.keys())
            # print("There are %s users in the system"%maxid)
            userinfo[str(int(maxid)+1)]=dicformat
            # print(userinfo)

            fp=open('users.json','w+')
            json.dump(userinfo,fp)
            return True


#登录
def login():


    import os
    if not os.path.isfile('users.json'):
        print("错误！用户文件不存在，请创建新用户！")
        return False
    userIndex = ''

    fp = open('users.json', 'r+')
    userinfo = json.load(fp)

    info = userinfo.values()

    login_flag = False

    counter=0
    while login_flag is False:
        usr = input("请输入用户名:")
        pwd = input("请输入密码:")
        global LOGIN_USER
        for user in info:
            counter+=1
            # print(user['name'],user['password'])
            # balance = user['balance']
            if user['name'] == usr and user['password'] == pwd:
                print("登录成功!".center(40,'-'))
                # print("Your privilege is ", balance)
                login_flag = True
                # LOGIN_USER = {"is_login": False, "user_type": 1, "user_id": 0, "user_name": "anonyoumous"}

                break
            else:
                continue

        if login_flag is True:
            for k, v in userinfo.items():
                # print(k, v)
                if usr in v['name'] and pwd in v['password']:
                    # print("User %s key is "%usr, k)

                    LOGIN_USER["is_login"] = True
                    LOGIN_USER["user_id"] = k
                    LOGIN_USER["user_name"]=usr
                    LOGIN_USER["user_type"]=v['privilege']
                    userIndex = k
        else:
            print("登录失败\n")
            break

#main函数
def main():


    while True:
        print("欢迎使用账户管理系统".center(40, '-'))
        choice=input ("请输入选项\n1.后台管理\n2.登录\n3.注册\n4.显示当前用户信息\n5.退出程序\n")

        Mgmt_Flag=False
        if choice == '1':
            while Mgmt_Flag is False:
                mgm_choice=input("请输入管理选项\n1.修改密码和邮箱\n2.修改权限\n3.查询用户信息\n4.添加新用户\n5.删除用户\n6.退出管理界面\n")

                if mgm_choice=='1': ChangePwd()
                elif mgm_choice=='2':
                    r=ChangePrivilege()
                    if r: print("权限修改成功\n")
                    else: print("权限修改失败\n")
                elif mgm_choice=='3':
                    name=input("输入关键字查询:")
                    QueryUser(name)
                elif mgm_choice=='4':
                    r=register()
                    if r: print("新用户注册成功\n")
                    else: print("新用户注册失败\n")
                elif mgm_choice=='5':
                    r=deluser()
                    if r:
                        print("删除用户成功\n")
                    else:
                        print("删除用户失败\n")
                elif mgm_choice=='6':Mgmt_Flag=True
                else:print("错误选项，请重新输入\n")

        elif choice=='2':
            r=login()


        elif choice=='3':
            res=register()
            name="成功" if res else "失败"
            print("注册 %s"%name)
        elif choice=='4':
            Infos()

        elif choice=='5':
            exit()



# testfile()
main()


