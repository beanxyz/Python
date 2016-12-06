#!/usr/bin/env python
# -*- coding:utf-8 -*-

import paramiko
import sys
import os
import socket
import datetime
import getpass

from paramiko.py3compat import u

import databaseControl

parent_path = os.path.abspath(os.pardir)
log_path=os.path.join(parent_path,'log','handle.log')


# windows does not have termios...
try:
    import termios
    import tty

    has_termios = True
except ImportError:
    has_termios = False

#通过termios判断是windows还是Linux/OSX

def interactive_shell(chan,pid,hid,hsid):
    if has_termios:
        posix_shell(chan,pid,hid,hsid)
    else:
        windows_shell(chan,pid,hid,hsid)

#Shell环境的操作，
def posix_shell(chan,pid,hid,hsid):
    """

    :param chan: 通道，用于接收服务器返回信息
    :param pid: userprofileid
    :param hid: hostuserid
    :param hsid: hostid
    :return:
    """


    import select

    #获取tty的属性

    oldtty = termios.tcgetattr(sys.stdin)
    try:
        #设置tty的属性
        tty.setraw(sys.stdin.fileno())
        tty.setcbreak(sys.stdin.fileno())
        chan.settimeout(0.0)
        log = open(log_path, 'a+', encoding='utf-8')
        #flag用来判断是否输入了tap
        flag = False
        temp_list = []
        while True:

            #监测输入和返回值（socket）
            r, w, e = select.select([chan, sys.stdin], [], [])

            #监测返回值
            if chan in r:
                try:
                    x = u(chan.recv(1024))
                    if len(x) == 0:
                        sys.stdout.write('\r\n*** EOF\r\n')
                        break


                    if flag:
                        if x.startswith('\r\n'):
                            pass
                        else:
                            temp_list.append(x)
                        flag = False

                    sys.stdout.write(x)
                    sys.stdout.flush()



                except socket.timeout:
                    pass

            #监测输入内容
            if sys.stdin in r:
                x = sys.stdin.read(1)
                import json

                if len(x) == 0:
                    break

                #如果输入tab
                if x == '\t':
                    flag = True

                else:
                    temp_list.append(x)

                #如果回车发送命令了，记录日志到本地和数据库
                if x == '\r':
                    # print(temp_list)

                    currenttime = datetime.datetime.now()
                    str="\n操作时间%s  堡垒机账号代码%d 主机账号代码%d 主机代码%d 执行代码%s"%(currenttime,pid,hid,hsid,''.join(temp_list).strip())
                    log.write(str)

                    databaseControl.session.add(databaseControl.AuditLog(userprofile_id=pid, hostuser_id=hid, cmd=''.join(temp_list), host_id=hsid,date=currenttime))
                    databaseControl.session.commit()
                    log.flush()
                    temp_list.clear()

                #发送命令
                chan.send(x)




    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)


#windows没有tty终端，因此用多线程实现
def windows_shell(chan,pid,hid,hsid):
    import threading

    sys.stdout.write("Line-buffered terminal emulation. Press F6 or ^Z to send EOF.\r\n\r\n")
    log = open(log_path, 'a+', encoding='utf-8')


    #接收数据
    def writeall(sock):
        while True:
            data = sock.recv(256)
            # print(data)
            if not data:
                sys.stdout.write('\r\n*** EOF ***\r\n\r\n')
                sys.stdout.flush()
                break


            sys.stdout.write(data.decode())
            sys.stdout.flush()

    writer = threading.Thread(target=writeall, args=(chan,))
    writer.start()
    temp_list=[]
    #发送数据
    try:
        while True:
            d = sys.stdin.read(1)
            if not d:
                break


            #如果输入tab
            
            temp_list.append(d)

            #如果回车发送命令了，记录日志到本地和数据库
            if d=='\n':
                # print("Ready")


                log.flush()
                currenttime=datetime.datetime.now()
                str = "\n操作时间%s  堡垒机账号代码%d 主机账号代码%d 主机代码%d 执行代码%s" % (
                currenttime, pid, hid, hsid, ''.join(temp_list).strip())
                log.write(str)
                databaseControl.session.add(
                    databaseControl.AuditLog(userprofile_id=pid, hostuser_id=hid, cmd=''.join(temp_list), host_id=hsid,
                                             date=currenttime))
                databaseControl.session.commit()
                temp_list.clear()
            chan.send(d)
    except EOFError:
        # user hit ^Z or F6
        pass


def run():
    # # 获取当前登录用户

    #读取数据库，获取相关信息
    host_list=databaseControl.run()

    if host_list ==None:
        return

    flag=True

    num=0

    while flag:
        for item in enumerate(host_list, 1):
            print(item)
        num = input('输入序号：')

        if not num.isdigit():
            print("非法输入")
            continue
        else:
            num=int(num)

        if num<=0 or num> len(host_list):
            print("超出范围")
            continue
        else:
            flag=False



    sel_host = host_list[int(num) - 1]
    hostname = sel_host['host']
    username = sel_host['username']
    pwd = sel_host['pwd']
    pid=sel_host['userprofileid']
    hid=sel_host['hostuserid']
    hsid=sel_host['hostid']
    print(hostname, username, pwd)

    tran = paramiko.Transport((hostname, 22,))
    tran.start_client()
    tran.auth_password(username, pwd)

    # 打开一个通道
    chan = tran.open_session()
    # 获取一个终端
    chan.get_pty()
    # 激活器
    chan.invoke_shell()

    interactive_shell(chan,pid,hid,hsid)

    chan.close()
    tran.close()


if __name__ == '__main__':
    run()
