#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li


# !/usr/bin/env python
# -*- coding:utf-8 -*-
# import SocketServer
import socketserver, json, os, subprocess, hashlib

parent_path = os.path.abspath(os.pardir)
login_path = os.path.join(parent_path, "db", "logon.json")
print(login_path)


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        # print self.request,self.client_address,self.server
        # self.request 相当于单线程的conn

        while True:

            self.request.sendall(bytes('欢迎使用FTP简易模拟系统，请输入用户名和密码登录.', encoding="utf-8"))
            data = self.request.recv(1024)
            user_data = json.loads(data.decode())
            self.user_name = user_data.get("name")
            self.user_password = user_data.get("pwd")

            print(self.user_name, self.user_password)
            try:
                if os.path.isfile(login_path) and os.stat(login_path).st_size != 0:
                    fp = open(login_path, 'r', encoding='utf-8')
                    temp = json.load(fp)
                    print(temp)
                    value = temp.get(self.user_name)
                    if self.user_password == value.get("pwd"):
                        print("%s 成功登录" % self.user_name)

                        user_dir = os.path.join(parent_path, 'ftproot', self.user_name)
                        # 输出总共配额，和使用的空间，以及剩余空间
                        self.total_quote = value.get("quote")
                        self.used_space = MyServer.get_size(user_dir)
                        self.free_space = self.total_quote * 1024 * 1024 * 1024 - self.used_space
                        # print("total:$dG,used:%d,free:%d"%(total_quote,used_space,free_space))
                        size_info = {"total": self.total_quote * 1024 * 1024 * 1024, "used": self.used_space,
                                     "free": self.free_space,
                                     "status": "Login Succesful"}
                        print(size_info)

                        # 切换到用户的主目录
                        os.chdir(user_dir)  # uncomment to actually change directory
                        self.currentdir = os.getcwd()  # 获取当前目录
                        print("准备发送资料到客户端")
                        self.request.sendall(bytes(json.dumps(size_info), encoding='utf8'))

                        data = self.request.recv(2048)
                        if data.decode() == 'LOGIN|ACK':
                            break
                    else:
                        print("Failed")
                        msg_data = {"status": "Login Failed"}
                        self.request.sendall(bytes(json.dumps(msg_data), encoding='utf8'))
                        continue

                else:

                    print("文件内容为空或者不存在！")

            except Exception:
                msg_data = {"status": "Login Failed"}
                self.request.sendall(bytes(json.dumps(msg_data), encoding='utf8'))

        while True:

            try:
                # 首先接受客户端发送的一个Json格式的字符串，包括文件操作，文件名称和大小
                data = self.request.recv(1024)
                # 如果客户端断开，发送一个空包过来
                if len(data) == 0: break
                print("data", data)
                print("[%s] says:%s" % (self.client_address, data.decode()))
                # decode（）相当于str(bytes文件)，转化bytes为str，然后读取字典内容
                task_data = json.loads(data.decode())
                # get()通过key获取value
                task_action = task_data.get("action")
                # 反射，第一个参数表示对象，比如模块，这里是self自己；第二个是要搜找的函数名
                if hasattr(self, "task_%s" % task_action):
                    func = getattr(self, "task_%s" % task_action)
                    func(task_data)
                else:
                    print("task action is not supported", task_action)
            except Exception:

                break

    def task_put(self, *args, **kwargs):
        print("---put", args, kwargs)
        # 这里就输入了一个参数，一个字典
        filename = args[0].get('filename')
        filesize = args[0].get('file_size')
        md5_value = args[0].get('md5_value')

        print("已使用空间", self.used_space)
        self.free_space = self.total_quote * 1024 * 1024 * 1024 - self.used_space
        print("剩余空间%d,上传文件%d" % (self.free_space, filesize))

        if self.free_space > filesize:

            filename = os.path.join(os.getcwd(), filename)
            print(filename)
            # 判断是否已经存在了

            if os.path.isfile(filename):
                if os.stat(filename).st_size < filesize:
                    print("文件已经存在了,而且内容不全")
                    server_response = {"status": 300}
                    self.request.send(bytes(json.dumps(server_response), encoding='utf-8'))
                    confirm = self.request.recv(1024)
                    if confirm.decode() == 'GO':
                        size = os.stat(filename).st_size
                        self.request.sendall(bytes(str(size), encoding='utf8'))
                        f = open(filename, 'ab')
                        recv_size = size
                        # 不断地读取客户端的内容，防止粘包
                        while recv_size < filesize:
                            # 一次接受4096个字节
                            data = self.request.recv(4096)
                            f.write(data)
                            recv_size += len(data)
                            # print('filesize: %s  recvsize:%s' % (filesize,recv_size))

                        md5_2 = MyServer.md5(os.path.join(os.getcwd(), filename))
                        if md5_value == md5_2:
                            print("file recv success")
                        else:
                            print("MD5不匹配！")

                        f.close()


                elif os.stat(filename).st_size == filesize:
                    print("文件已经存在，无需再次上传")
                    server_response = {"status": 100}
                    self.request.send(bytes(json.dumps(server_response), encoding='utf-8'))

            elif not os.path.isfile(filename):
                server_response = {"status": 200}
                # 把一个字典序列化为字符串之后，编码utf-8发回给客户端
                self.request.send(bytes(json.dumps(server_response), encoding='utf-8'))
                # 打开一个文件，准备写

                filename = os.path.join(os.getcwd(), filename)
                # print(filename)
                f = open(filename, 'wb')
                recv_size = 0
                # 不断地读取客户端的内容，防止粘包
                while recv_size < filesize:
                    # 一次接受4096个字节
                    data = self.request.recv(4096)
                    f.write(data)
                    recv_size += len(data)
                    # print('filesize: %s  recvsize:%s' % (filesize,recv_size))
                # abspath=os.path.join(os.getcwd(), filename)
                # print(abspath)
                f.seek(0)
                md5_2 = MyServer.md5(filename)
                print(md5_2)
                if md5_value == md5_2:
                    print("file recv success")
                    self.request.sendall(bytes("MD5:OK", encoding='utf-8'))
                    print("回复MD5")
                else:
                    print("MD5不匹配！")

                    self.request.sendall(bytes("MD5:bad", encoding='utf-8'))
                    print("回复MD5")
                f.close()
        else:

            print("超过配额！")
            response = {"status": 400}

            self.request.sendall(bytes(json.dumps(response), encoding='utf-8'))
            print("send")

    def task_pwd(self, *args, **kwargs):
        print("---pwd", args, kwargs)
        #
        # user_dir=os.path.join(parent_path,'ftproot',self.user_name)
        #
        # #切换到用户的主目录
        # os.chdir(user_dir) # uncomment to actually change directory
        cwd = os.getcwd().split(os.path.join(parent_path, 'ftproot'))[1]  # 获取当前目录
        # 发送长度

        print("目录%s,长度%d" % (cwd, len(cwd)))
        self.request.send(bytes(str(len(cwd)), encoding='utf-8'))
        # print("准备接受确认信息")
        confirm = self.request.recv(1024)
        # print(confirm)
        if confirm.decode() == 'ok':
            self.request.send(bytes(cwd, encoding='utf8'))

    def task_mkdir(self, *args, **kwargs):

        print("--mkdir")
        dir_name = args[0].get("folder")
        print(self.currentdir)
        print(dir_name)
        if not os.path.isdir(dir_name):
            os.mkdir(dir_name)
            self.request.sendall(bytes("SUCCESS", encoding='utf-8'))
        else:
            self.request.sendall(bytes("EXIST", encoding='utf-8'))

    def task_cd(self, *args, **kwargs):

        print("--cd")
        dest = args[0].get("dest")
        print(dest)

        if os.getcwd() == os.path.join(parent_path, 'ftproot', self.user_name) and dest == '..':
            self.request.sendall(bytes("TOP", encoding='utf-8'))

        elif os.path.isdir(dest):
            self.currentdir = os.chdir(dest)
            self.request.sendall(bytes("SUCCESS", encoding='utf-8'))
        else:
            print("该目录不存在")
            self.request.sendall(bytes("FAILURE", encoding='utf-8'))

    def task_dir(self, *args, **kwargs):

        print("--dir")
        content = os.listdir(os.getcwd())
        folder_size = MyServer.get_size(start_path=os.getcwd())

        # 直接发送
        msg_data = {"content": content, 'size': folder_size}
        # print(msg_data)
        self.request.sendall(bytes(json.dumps(msg_data), encoding='utf8'))

    # 下载文件
    def task_get(self, *args, **kwargs):

        print("--get")
        print(args[0])
        file_name = args[0].get("filename")
        print(file_name)

        file_path = os.path.join(os.getcwd(), file_name)
        if os.path.isfile(file_path):
            print("找到文件，准备下载")
            self.request.sendall(bytes("Ready", encoding='utf-8'))
            md5_value = MyServer.md5(file_path)
            confirm = self.request.recv(2048)
            if confirm.decode() == 'Go':
                file_size = os.stat(file_name).st_size
                # filename = abs_filepath.split("\\")[-1]
                print('file:%s size:%s' % (file_name, file_size))
                msg_data = {"action": "get",
                            "filename": file_name,
                            "file_size": file_size,
                            "md5_value": md5_value}

                # 发送大小给客户端 避免粘包
                self.request.sendall(bytes(json.dumps(msg_data), encoding='utf-8'))

                print("已经发送大小给客户端")
                d = self.request.recv(2048)
                if json.loads(d.decode()).get("status") == 200:
                    # 准备传输
                    print("start sending file ", file_name)
                    f = open(file_name, 'rb')
                    temp = 0.0
                    for line in f:
                        self.request.send(line)
                        temp += len(line)
                        # update_progress(temp / file_size)

                    print("send file done ")

                    # 断点续传
                elif json.loads(d.decode()).get("status") == 300:
                    f = open(file_name, 'rb')
                    size = json.loads(d.decode()).get("size")
                    print("size", size)
                    f.seek(int(size))
                    temp = size
                    for line in f:
                        self.request.sendall(line)



                else:
                    print("Error!")


        else:
            print("该文件不存在")
            self.request.sendall(bytes("NotExist", encoding='utf-8'))

    # 计算指定目录的大小
    @staticmethod
    def get_size(start_path):

        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size

    @staticmethod
    def md5(fname):
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()


def run():
    server = socketserver.ThreadingTCPServer(('0.0.0.0', 8009), MyServer)
    server.serve_forever()


if __name__ == '__main__':
    run()
