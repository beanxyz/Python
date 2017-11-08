#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li

import os, hashlib, json

parent_path = os.path.abspath(os.pardir)
print(parent_path)

login_path = os.path.join(parent_path, "db", "logon.json")
logs_path=os.path.join(parent_path,'db','log')

def create_user():
    name = input("账号名")
    user_pwd = input("密码")
    obj = hashlib.md5()
    obj.update(bytes(user_pwd, encoding='utf8'))
    pwd = obj.hexdigest()
    while True:
        quote = input("配额(G)")
        if quote.isdigit():
            quote = int(quote)
            break
        else:
            print("请输入一个整数")

    user_path = os.path.join(parent_path, "ftproot", name)
    if not os.path.isdir(user_path):
        os.mkdir(user_path)
    else:
        print("该用户文件夹已经存在！")

    user_info = {name: {"pwd": pwd, "quote": quote}}

    if os.path.isfile(login_path) and os.stat(login_path).st_size != 0:
        # print(len(login_path))
        fp = open(login_path, 'r+')

        temp = json.load(fp)
        print(temp)
        temp[name] = {"pwd": pwd, "quote": quote}
        fp = open(login_path, 'w', encoding='utf-8')
        json.dump(temp, fp)
        fp.close()
    else:
        fp = open(login_path, 'w')
        json.dump(user_info, fp)


def change_user():
    try:
        inpt = input("请输入用户名")
        if os.path.isfile(login_path):
            fp = open(login_path, 'r', encoding='utf-8')
            temp = json.load(fp)
            value = temp.get(inpt)
            print(value)
            new_pwd = input("请输入新的密码")
            obj = hashlib.md5()
            obj.update(bytes(new_pwd, encoding='utf8'))
            new_pwd = obj.hexdigest()
            value["pwd"] = new_pwd
            while True:
                new_quote = input("请输入新的配额")
                if new_quote.isdigit():
                    new_quote = int(new_quote)
                    break
                else:
                    print("请重新输入合法的配额")
            value["quote"] = new_quote

            print(temp)
            fp = open(login_path, 'w', encoding='utf-8')
            json.dump(temp, fp)
        else:
            print("错误：用户配置文件不存在！")
    except Exception as ex:
        print(ex)


def delete_user():
    inpt = input("请输入用户名")
    if os.path.isfile(login_path):
        fp = open(login_path, 'r+', encoding='utf-8')
        temp = json.load(fp)
        value = temp.get(inpt)
        print(temp)
        if not value:
            print("该用户不存在！")

        else:
            temp.pop(inpt, None)

            print(temp)
            fp = open(login_path, 'w')
            json.dump(temp, fp)

            user_path = os.path.join(parent_path, "ftproot", inpt)
            os.rmdir(user_path)

    else:
        print("错误：用户配置文件不存在！")


def display_user():
    if os.path.isfile(login_path) and os.stat(login_path).st_size != 0:
        fp = open(login_path, 'r', encoding='utf-8')
        temp = json.load(fp)
        print(temp)
        for item in temp:
            print("账户%s, 资料%s" % (item, temp[item]))

    elif os.stat(login_path).st_size == 0:
        print("文件内容为空，没有任何用户数据")

    else:
        print("错误：用户配置文件不存在！")



def display_log():
    if os.path.isfile(logs_path):
        with open(logs_path,'r',encoding='utf-8') as fp:
            for line in fp:
                print(line.strip())
    else:
        print("Not Log file")



def run():
    msg = """
    1.创建用户
    2.修改用户
    3.删除用户
    4.打印用户
    5.打印日志
    6.退出
    """
    while True:
        print(msg)
        inpt = input("请输入选项")
        if inpt == '1':
            create_user()
        elif inpt == '2':
            change_user()
        elif inpt == '3':
            delete_user()
        elif inpt == '4':
            display_user()
        elif inpt == '5':
            display_log()
        elif inpt=='6':
            exit()
        else:
            print("非法输入")
            continue


if __name__ == '__main__':
    run()
