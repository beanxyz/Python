#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li

import socket
import os, json, sys
import hashlib


# 显示进度条
def update_progress(progress):
    barLength = 10  # Modify this to change the length of the progress bar
    status = ""
    # 如果传入的是整数，转换为浮点数
    if isinstance(progress, int):
        progress = float(progress)
    # 如果是其他类型的，报错
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    # 如果传入的是个负数，中止
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    # 如果传入的是正数，okay啦
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength * progress))
    # 根据百分比输出#的块
    text = "\rPercent: [{0}] {1}% {2}".format("#" * block + "-" * (barLength - block), "%.2f" % (progress * 100),
                                              status)
    sys.stdout.write(text)
    sys.stdout.flush()


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


# 发送消息
# 首先接受一个欢迎信息

def run():
    ip_port = ('127.0.0.1', 8009)

    s = socket.socket()

    s.connect(ip_port)
    while True:
        welcome_msg = s.recv(1024)
        print(welcome_msg.decode())
        name = input("输入用户名")
        pwd = input("输入密码")

        obj = hashlib.md5()
        obj.update(bytes(pwd, encoding='utf8'))
        pwd = obj.hexdigest()
        user_info = {"name": name, "pwd": pwd}
        # 发送用户名和密码到服务器
        s.sendall(bytes(json.dumps(user_info), encoding='utf8'))

        data = s.recv(1024)
        # print(data)
        # print(json.loads(data.decode()))
        if json.loads(data.decode()).get("status") == 'Login Succesful':
            flag = True
            print("用户成功登录")
            data = json.loads(data.decode())
            print("总空间%.4fG,使用空间%.4fG,剩余空间%.4fG" % (
                data.get("total") / (1024 * 1024 * 1024), data.get("used") / (1024 * 1024 * 1024),
                data.get("free") / (1024 * 1024 * 1024)))

            # 回复一个确认信息

            s.send(bytes("LOGIN|ACK", encoding='utf8'))

            break
        elif json.loads(data.decode()).get("status") == 'Login Failed':
            print("用户名或密码不正确")
            continue

    # 循环发送
    while True:
        send_data = input(">>: ").strip()
        # 不能发送空数据，不然对方会堵塞
        if len(send_data) == 0: continue
        # 发送的格式为put c:\temp\a.txt, 用空格分开，转化为列表
        cmd_list = send_data.split()
        # 列表长度小于2，无效
        # if len(cmd_list) <2:continue
        task_type = cmd_list[0]
        # 上传文件
        if task_type == 'put':
            if len(cmd_list) < 2: continue
            # 第一个列表元素是操作；第二个列表元素是路径
            abs_filepath = cmd_list[1]
            if os.path.isfile(abs_filepath):
                # 获取长度
                file_size = os.stat(abs_filepath).st_size
                filename = abs_filepath.split("\\")[-1]

                md5_value = md5(abs_filepath)
                print('file:%s size:%s' % (abs_filepath, file_size))
                msg_data = {"action": "put",
                            "filename": filename,
                            "file_size": file_size,
                            "md5_value": md5_value}
                # 发送一个字典给服务器
                s.sendall(bytes(json.dumps(msg_data), encoding="utf-8"))
                # 获取一个确认信息；这是因为send()函数每次发送的大小不一定，所以需要确定全部发送成功，避免和后面的数据连在一起
                server_confirmation_msg = s.recv(2048)
                print(server_confirmation_msg)
                confirm_data = json.loads(server_confirmation_msg.decode())
                if confirm_data['status'] == 200:

                    print("start sending file ", filename)
                    f = open(abs_filepath, 'rb')
                    temp = 0.0
                    for line in f:
                        s.send(line)
                        temp += len(line)
                        update_progress(temp / file_size)

                    print("send file done ")

                    md5_confirm = s.recv(2048)

                    if md5_confirm.decode() == 'MD5:OK':
                        print("MD5 验证匹配通过！成功上传文件")
                    else:
                        print("MD5 验证匹配失败，上传文件不完整或被修改")
                    continue

                elif confirm_data['status'] == 300:
                    print("该文件已经存在！准备断点续传..")

                    s.sendall(bytes('GO', encoding='utf-8'))
                    size = s.recv(2048)
                    # print(size)
                    # print(size.decode())


                    f = open(abs_filepath, 'rb')
                    temp = int(size.decode())
                    print("existing size", size)
                    f.seek(int(size.decode()))
                    for line in f:
                        s.sendall(line)
                        temp += len(line)
                        update_progress(temp / file_size)
                    continue

                elif confirm_data['status'] == 100:
                    print("已经存在完整版本，无需上传")
                    continue

                elif confirm_data['status'] == 400:
                    print("剩余空间不足，无法上传")
                    continue

            else:
                print("\033[31;1mfile [%s] is not exist\033[0m" % abs_filepath)
                continue
        # 显示当前路径
        elif task_type == 'pwd':
            msg_data = {"action": "pwd"}
            s.send(bytes(json.dumps(msg_data), encoding="utf-8"))
            # 接受长度
            raw_data = s.recv(1024)
            data_size = int(raw_data.decode())

            # print("长度：",data_size)
            s.send(bytes('ok', encoding='utf-8'))
            # print("发送ok")
            recv_size = 0
            dir_info = b''
            # 不断地读取客户端的内容，防止粘包
            while recv_size < data_size:
                # 一次接受4096个字节
                data = s.recv(1024)
                dir_info += data
                recv_size += len(data)
            # print("direcotry info recv success")

            print(dir_info.decode())
            continue
        # 创建目录
        elif task_type == 'mkdir':

            if len(cmd_list) < 2: continue

            new_dir = cmd_list[1]
            msg_data = {"action": "mkdir",
                        "folder": cmd_list[1]}

            # 发送指令
            s.send(bytes(json.dumps(msg_data), encoding='utf-8'))
            # 接受创建成功的回复
            data = s.recv(2048)
            if data.decode() == 'SUCCESS':
                print("新目录创建成功！")
            else:
                print("该目录已经存在！")

            continue
        # 切换目录
        elif task_type == 'cd':

            if len(cmd_list) < 2: continue

            dest = cmd_list[1]
            msg_data = {"action": "cd", "dest": dest}

            s.send(bytes(json.dumps(msg_data), encoding='utf-8'))
            data = s.recv(2048)
            if data.decode() == 'SUCCESS':
                print("目录切换成功！")
            elif data.decode() == 'TOP':
                print("已经是用户根目录了！")
            else:
                print("目录不存在")
            continue
        # 显示当前目录内容
        elif task_type == 'dir':
            msg_data = {"action": "dir"}
            s.send(bytes(json.dumps(msg_data), encoding='utf-8'))
            content = s.recv(4096)
            print(content)
            data = json.loads(content.decode())
            print("当前目录包括以下内容")
            for item in data.get("content"):
                print(item)

            print("总计%d字节" % data.get("size"))
            continue
        # 下载文件
        elif task_type == 'get':
            if len(cmd_list) < 2: continue
            # 第一个列表元素是操作；第二个列表元素是文件名
            filename = cmd_list[1]
            msg_data = {"action": "get", "filename": filename}
            # 发送命令
            s.sendall(bytes(json.dumps(msg_data), encoding='utf-8'))
            # 接受反馈信息，看看是否文件存在于服务器端
            confirm = s.recv(2048)
            if confirm.decode() == 'Ready':
                s.sendall(bytes("Go", encoding='utf8'))
                content = s.recv(4096)
                file_get_size = json.loads(content.decode()).get("file_size")
                md5_get_value = json.loads(content.decode()).get("md5_value")
                print("文件大小", file_get_size)

                # 判断当前文件是否已经存在
                # 如果不存在，那么直接下载
                if not os.path.isfile(filename):

                    server_response = {"status": 200}
                    # 告诉服务器我准备好了
                    s.send(bytes(json.dumps(server_response), encoding='utf-8'))

                    # print(filename)
                    print("准备接收")
                    f = open(filename, 'wb')
                    recv_size = 0
                    # 不断地读取客户端的内容，防止粘包
                    while recv_size < file_get_size:
                        # 一次接受4096个字节
                        data = s.recv(4096)
                        f.write(data)
                        recv_size += len(data)
                        update_progress(recv_size / file_get_size)
                        # print('filesize: %s  recvsize:%s' % (file_get_size,recv_size))

                    f.seek(0)
                    md5_2 = md5(filename)
                    if md5_2 == md5_get_value:

                        print("MD5匹配通过，文件成功下载！")
                    else:
                        print("MD5匹配失败，文件下载不完整或者被修改")
                    f.close()
                    continue

                elif os.path.isfile(filename) and os.stat(filename).st_size < file_get_size:
                    print("文件已经存在，准备断点续传")
                    msg_data = {"size": os.stat(filename).st_size, "status": 300}
                    # 告诉服务器准备断点续传
                    s.sendall(bytes(json.dumps(msg_data), encoding='utf-8'))

                    print("准备继续接收")
                    f = open(filename, 'ab')
                    recv_size = os.stat(filename).st_size
                    while recv_size < file_get_size:
                        data = s.recv(4096)
                        f.write(data)
                        recv_size += len(data)
                        update_progress(recv_size / file_get_size)
                    print("文件成功下载")
                    f.close()
                    continue
                else:
                    print("文件已经成功下载，无需再次下载")
                    continue


            else:
                print("用户指定的文件在服务器上不存在！")
                continue



        else:
            print("doesn't support task type", task_type)
            continue
        # s.send(bytes(send_data,encoding='utf8'))
        # 收消息
        recv_data = s.recv(1024)
        print(str(recv_data, encoding='utf8'))
        # 挂电话
    s.close()


if __name__ == '__main__':
    run()
