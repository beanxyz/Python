#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li


def fetch(backend):
    """
    参数传入backend的域名
    :param backend:
    :return:

    基本思路：
    读取文件1，如果发现匹配的backend域名，那么设置falg为True；如果是下一个backend，那么flag设置为False
    如果flag为真，而且是以server开头的节点内容，那么放入列表
    """

    with open('config','r',encoding="utf-8") as file:
        flag=False  #Flag用来标识是否找到了对应的backend
        result=[]   #空列表用来存放找到的节点数据
        for line in file:
            if line.strip().startswith("backend") and line.strip()=="backend "+backend:
                flag=True
                continue  #如果找到了backend，那么设置flag，同时进入下一层循环（节点）
            if flag is True and line.strip().startswith("backend"):
                flag=False#如果离开了匹配的backend范围，那么flag设置为假
                break
            elif flag is True and line.strip().startswith("server"):
                result.append(line.strip()) #如果在匹配的范围内，把节点放入列表
    return  result


def add(bk,rd):

    """
    传入参数backend和record
    :param bk:
    :param rd:
    :return:
    思路：
    获取指定backend的所有节点记录
    如果backend不存在，那么直接复制文件1到文件2，然后把新记录写入文件2末尾
    如果backend存在，而且record也存在，那么直接复制文件1到文件2即可；
    如果backend存在，而且record不存在，那么把数据更新到列表中，然后把列表和除了这个backend范围以外的所有数据写入文件2
    """
    r=fetch(bk)
    if not r:
        #backend 不存在

        with open('config','r') as old, open('new','w') as new:
            for line in old:
                new.write(line)

        new=open('new','a')
        new.write("\n\nbackend "+bk+"\n")
        new.write(" "*8+rd+"\n")
        new.close()

    else:
        #backend 存在
        if rd in r:
            #record 存在
            import shutil
            print("该信息已经存在于源文件中！\n")
            shutil.copy("config","new")
            # return False

        else:
            #record 不存在
            #把新信息添加打列表中
            r.append(rd)


            with open('config', 'r') as old, open('new', 'w') as new:
                flag=False
                for line in old:
                    if line.strip().startswith("backend") and line.strip() == "backend " + bk:
                        flag=True
                        # print("found the backend "+line.strip())
                        new.write(line)  #写入backend这一行
                        for new_line in r:
                            # print(new_line+" is added")
                            new.write(" "*8+new_line+"\n")
                    #如果离开了匹配的backend范围，那么直接写入数据到文件2，并把flag设置为假
                    if flag and line.strip().startswith("backend"):
                        flag=False
                        new.write(line)
                        continue

                    #其他行直接写入文件2
                    if not flag and line.strip():
                        new.write(line)

        return True

def delete(bk,rd):
    #基本思路：找到BackEnd,然后寻找record；没有找到，返回错误
    #找到BackEnd的话，如果这个是唯一的匹配记录，那么Backend和他所属的record都不写入文件2（删除）
    #如果不是唯一的记录，那么Backend 写入文件2，这个我要删的record不写入，其他照旧写入
    #如果BackEnd匹配，但是record不匹配，返回错误

    record=fetch(bk)

    #backend不存在
    if not record:
        # print("BackEnd doesn't exist")
        return False

    #backend存在
    else:
    #如果Backend存在，但是record不匹配，直接返回报错
        matchflag = False
        for item in record:
            if item == rd:
                matchflag = True

        if matchflag == False:
            print("Backend存在，但是对应的节点不存在！")
            return False

        if len(record)>1:
            with open('config','r') as old, open('new','w') as new:
                for line in old:
                    if line.strip()==rd:
                        continue
                    else:
                        new.write(line)

        elif len(record)==1:
            with open('config', 'r') as old, open('new', 'w') as new:
                for line in old:
                    if line.strip()=="backend "+bk:
                        continue
                    elif line.strip()==rd:
                        continue
                    else:
                        new.write(line)



    return True


def update(bk,rd):
    #基本思路：搜索Backend，如果该IP地址的记录不存在，返回错误；
    #如果BackEnd和该IP地址的记录都存在，那么原先的line不写入，写入更改之后的newline

    record = fetch(bk)

    # backend不存在
    if not record:
        # print("BackEnd doesn't exist")
        return False

    # backend存在
    else:

        flag=False
        for item in record:
            if str(item).split("weight")[0]==rd.split("weight")[0]:
                # print("IP match!")
                flag=True
            else:
                continue

        if flag is False:
            return False

        with open('config', 'r') as old, open('new', 'w') as new:
            for line in old:
                if line.strip().startswith("server") and line.strip().split("weight")[0]==rd.split("weight")[0]:
                    new.write(" "*8+rd)
                    new.write("\n")
                else:
                    new.write(line)

        return True


import json

flag=False
while flag is False:
    choice=input("请输入你的选项\n1.查询节点\n2.添加节点\n3.删除节点\n4.修改节点\n5.退出程序\n")

    if choice.isdigit():
        choice=int(choice)
        if choice==1:
            bk= input("请输入backend的域名进行查询")
            result=fetch(bk)
            if result:
                for item in result:
                    print(item)
            else:
                print("查询失败！请确认域名是否正确\n")
            continue
        if choice in [2,3,4]:

            string = input("请以Json格式输入backend和站点信息")
            try:
                dic = json.loads(string)
                bk = dic["backend"]
                # rd=dic["record"]
                server = dic["record"]['server']
                weight = dic["record"]["weight"]
                maxconn = dic["record"]["maxconn"]
                rd = "server %s weight %d maxconn %d" % (server, weight, maxconn)

            except:
                print("非法格式\n")
                continue
            if choice==2:
                res=add(bk,rd)
                name = "成功" if res is True else "失败"
                print("添加%s\n"%name)

                continue
            elif choice==3:
                res=delete(bk,rd)
                name="成功" if res is True else "失败"
                print("删除%s\n"%name)
                continue
            else:
                res=update(bk,rd)
                name="成功" if res is True else "失败"
                print("更改%s\n"%name)

        elif choice==5:
            flag=True


        else:
            print("请输入1-4的选项")
    else:
        print("非法输入!\n")


# bk = "www.oldboy.org"
# rd = "server 100.1.7.9 100.1.7.239 weight 20 maxconn 3000"
# {"backend": "www.oldboy.org","record":{"server": "100.1.7.9 100.1.7.9","weight": 20,"maxconn": 3000}}
# fetch(bk)




