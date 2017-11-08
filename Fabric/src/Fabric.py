#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li


"""

 本程序模拟Fabric，远程的批量进行SSH连接，可以执行下载，上传和shell命令执行。
 远程命令的执行，使用了线程池的技术，因为执行的时间比较少，而线程本身执行的时间占的比重比较大；
 对于下载和上传，因为本身就是比较消耗时间的操作，因此每个连接单独使用了线程创建和销毁，因为时间比较久，线程的时间可以忽略了

"""

import threading
import queue
import time
import paramiko
import os

#找到相对路径
parent_path = os.path.abspath(os.pardir)
db_path=os.path.join(parent_path,'db')

#一个管理类，基本思路是把任务和相关的参数填充到队列（任务池）中，然后创建一个进程池，里面的进程循环地读取任务池里面的内容，任何执行其中的内容，直到所有任务全部实现。
class workmanager(object):

    #构造函数
    def __init__(self,cmd,username,password,work_num=1000,thread_num=2,):
        """

        :param cmd:远程命令
        :param username: 用户名
        :param password: 密码
        :param work_num: 任务池（队列大小）
        :param thread_num: 线程池大小
        """
        self.cmd=cmd
        self.work_num=work_num
        self.thread_num=thread_num
        self.queue=queue.Queue()
        self.threads=[]
        self.init_task(work_num,cmd,username,password)
        self.init_threadpool(thread_num)

    #初始化任务池
    def init_task(self,num,inp,username,password):
        for i in range(num):
            self.add_job(do_job,i,inp,username,password)

    #添加任务到任务池
    def add_job(self,job,*args):
        #填充任务到任务池，每一个任务是一个元祖（任务，参数列表）
        self.queue.put((job,list(args)))

    #初始化线程池
    def init_threadpool(self,num):
        for i in range(num):
            self.threads.append(work(self.queue))

    #等待挂起主线程
    def wait_allcomplete(self):
        for item in self.threads:
            if item.isAlive():
                item.join()

#线程类，每个线程循环地去任务池取任务
class work(threading.Thread):
    def __init__(self,que):
        super(work, self).__init__()
        self.queue=que
        self.start()


    def run(self):
        while True:
            try:
                #当任务池为空的时候，强制报错，退出
                do,args=self.queue.get(block=False)
                # print(do,args)
                do(args[0],args[1],args[2],args[3])
                #确保队列里面的任务都完成了
                self.queue.task_done()
            except:
                break

#初始化的一个主机组，测试用的
hosts=['anoble-ise','bberry-ise','blackbr-ise','jlau-ise','kwood-ise','marwa-ise','smaroo-ise','psekarwin-ise','spare2-ise']


#远程连接SSH并且执行命令
def do_job(args,inp,username,password):
    """

    :param args: hosts列表的索引
    :param inp: 远程命令
    :param username: 用户名
    :param password: 密码
    :return:
    """
    # time.sleep(0.1)

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hosts[args], 22, username, password)

    # 执行命令测试

    stdin, stdout, stderr = ssh.exec_command(inp)
    for line in stdout.readlines():
        print(line.strip())
    print(("\x1b[5;19;32m  %s \x1b[0m" % hosts[args]).center(40,'*'))
    print("\n")

#下载测试
def download(args,user,pwd,remote,local):
    """

    :param args: hosts列表的索引
    :param inp: 远程命令
    :param username: 用户名
    :param password: 密码
    :return:
    """

    try:
        # print(hosts[args])
        t = paramiko.Transport((hosts[args],22))
        t.connect(username=user, password=pwd)
        sftp = paramiko.SFTPClient.from_transport(t)
        # remotepath='/tmp/test2'

        if not os.path.isdir(local):
            os.makedirs(local)

        remotepath=remote
        localpath=os.path.join(local,hosts[args])

        sftp.get(remotepath, localpath)
        print("下载文件从%s成功" % hosts[args])
    except Exception as ex:
        print("下载文件从%s失败"%hosts[args])


# 上传测试
def upload(args,user,pwd,remote,local):

    try:
        # print(hosts[args])
        t = paramiko.Transport((hosts[args], 22))
        t.connect(username=user, password=pwd)
        sftp = paramiko.SFTPClient.from_transport(t)
        # remotepath='/tmp/test2'
        remotepath=remote
        localpath=local
        # localpath='c:/temp/aaa.txt'
        sftp.put(localpath, remotepath)
        print('上传文件到%s成功' % hosts[args])
        t.close()
    except Exception as ex:
        print('上传文件到%s失败'%hosts[args])

#选择主机组
def hostinfo():
    global hosts
    print("可供选择的主机组包括：")
    from os import listdir
    from os.path import isfile, join
    # mypath=os.getcwd()
    onlyfiles = [f for f in listdir(db_path) if isfile(join(db_path, f))]
    print(onlyfiles)
    for file in onlyfiles:
        file_path=os.path.join(db_path,file)
        with open(file_path,'r') as fp:
           print(("\x1b[5;19;32m %s 主机列表 \x1b[0m" %file).center(40, '*'))
           for line in fp:
               print(line.strip())


    name=input("请选择你要操作的主机组名称（hostgroup1,hostgroup2,hostgroup3..)")
    if name in onlyfiles:
        hosts=[]
        file_path=os.path.join(db_path,name)
        with open(file_path,'r') as fp:
            for line in fp:

                hosts.append(line.strip())

    else:
        print("该主机组不存在")

username=""
password=""

#入口文件
def display():
    global hosts,username,password


    msg="""
    欢迎使用Fabric模拟程序，您可以执行以下操作
    1.显示主机组
    2.批量执行远程命令
    3.批量上传
    4.批量下载
    5.输入管理员账号
    6.退出

    """

    msg2 = """
    1.选择主机组
    2.列出当前主机列表
    3.返回上一级目录

     """

    while True:
        print(msg)
        inpt=input("请输入选项")

        #输出主机组的相关信息
        if inpt=='1':
            while True:
                print(msg2)

                opt=input("请输入选项")
                if opt=='1':
                    hostinfo()

                elif opt=='2':
                    for item in hosts:
                        print(item)

                elif opt=='3':break
                else:print("非法输入")



        #远程批量操作
        elif inpt=='2':
            # username=input("用户名")
            # password=input("密码")
            if not username:
                print("请先配置登录账号信息")


            else:
                while True:
                    inp = input("输入指令(q返回上级目录）\n>>>")
                    if inp =='q':break
                    if not inp:
                        print("不能输入空命令")

                    else:
                        start = time.time()
                        #指定命令，用户名，密码，任务池（队列）的大小，和线程的个数）
                        work_manager = workmanager(inp,username,password, len(hosts), 2)
                        work_manager.wait_allcomplete()
                        end = time.time()
                        print("Cost time is %s" % (end - start))

        #创建批量上传的多线程
        elif inpt=='3':

            if not username:
                print("请先配置登录账号信息")
            else:
                remote_path=input("远程路径")
                local_path=input("当前路径")
                threads = []
                for item in range(len(hosts)):
                    t = threading.Thread(target=upload, args=(item,username,password,remote_path,local_path))
                    t.start()
                    threads.append(t)
                for t in threads:
                    t.join()

        #创建批量下载的多线程
        elif inpt=='4':

            if not username:
                print("请先配置登录账号信息")


            else:
                remote_path = input("远程文件路径")
                local_path = input("当前文件夹路径")
                threads=[]
                for item in range(len(hosts)):
                    t = threading.Thread(target=download, args=(item,username,password,remote_path,local_path))
                    t.start()
                    threads.append(t)
                for t in threads:
                    t.join()

        elif inpt=='5':
            username = input("用户名")
            password = input("密码")


        elif inpt=='6':
            exit("退出程序")

        else:
            print("无效输入，请重试")



if __name__ == '__main__':

    display()
