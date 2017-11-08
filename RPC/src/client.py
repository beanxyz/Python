#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li
# !/usr/bin/env python
import pika
import uuid
import os
import pymysql
import logging

class RpcClient(object):
    def __init__(self):


        # print(config_path2)
        #创建配置文件
        if not os.path.isfile(config_path2):
            logging.info("Create RabbitMQ config file")

            print("没有找到RabitMQ服务器的信息，请配置！")
            server_name=input("RabbitMQ服务器")
            msg='server=%s'%server_name
            fp=open(config_path2,'w',encoding='utf-8')
            fp.write(msg)
            fp.close()

        # 读取配置文件

        ft=open(config_path2,'r',encoding='utf-8')
        for line in ft:
            if line.strip().startswith('server'):
                server_name=line.split("=")[1]

        #绑定RabbitMQ
        # print(server_name)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=server_name))
        self.channel = self.connection.channel()
        # self.channel.exchange_declare(exchange='logs_fanout',
                                 # type='fanout')

        self.channel.exchange_declare(exchange='direct_logs_test_1',
                                 type='direct')

        logging.info("Binding to RabbitMQ server %s"%server_name)

        import pymysql
        #配置数据库文件信息
        # print(config_path)
        if not os.path.isfile(config_path):
            logging.info("Create DB config file")

            print("数据库配置文件不存在，请创建！")

            # temp_list=[]
            host = input("MySQL服务器IP或者域名")
            port = input("MySQL服务器端口号（3306）")
            user = input("用户名")
            passwd = input("密码")
            db = input("数据库名称")

            msg = "host=%s\nport=%s\nuser=%s\npasswd=%s\nlog=%s" % (host, port, user, passwd, db)

            # 生成初始化的配置文件

            fp = open(config_path, 'w', encoding='utf-8')
            fp.write(msg)
            fp.close()
        #读取数据库文件信息
        ss = ""
        count = 0
        fp = open(config_path, 'r', encoding='utf-8')

        for line in fp:
            if line.strip().startswith('host'):
                self.host = line.strip().split("=")[1].strip()
            if line.strip().startswith('port'):
                self.port = line.strip().split("=")[1].strip()
            if line.strip().startswith('user'):
                self.user = line.strip().split("=")[1].strip()
            if line.strip().startswith('passwd'):
                self.passwd = line.strip().split("=")[1].strip()
            if line.strip().startswith('db'):
                self.db = line.strip().split("=")[1].strip()

        # print(self.host)
        # print(self.host, self.port, self.user, self.passwd, self.db)

        temp=self.tag()
        # print(temp)
        self.severity = temp['label']
        self.num=temp['num']

        # 生成随机队列
        self.result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = self.result.method.queue
        print("生成返回队列%s"%self.callback_queue)


        # 指定on_response从callback_queue读取信息，阻塞状态
        self.channel.basic_consume(self.on_response, no_ack=True,
                                   queue=self.callback_queue)

    # 接受返回的信息
    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body
            print( (self.response).decode())

    # 发送请求
    def call(self, n):
        self.response = None

        # 生成一个随机值
        self.corr_id = str(uuid.uuid4())

        # 发送两个参数 reply_to和 correlation_id
        self.channel.basic_publish(exchange='direct_logs_test_1',
                                   routing_key=self.severity,
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id,
                                   ),
                                   body=n)

        # 等待接受返回结果
        # while self.response is None:
        #     self.connection.process_data_events()

        # self.count()
        # return str(self.response)

    #选择主机组
    def tag(self):
        print("查询数据库...")
        logging.info("Query from DB %s"%self.db)
        #查询数据库
        conn = pymysql.connect(host=self.host, port=int(self.port), user=self.user, passwd=self.passwd, db=self.db)
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute("select * from Hosts INNER JOIN Department on Hosts.department_id=Department.dep_id")
        rows = cursor.fetchall()

        IT_hosts = []
        Creative_hosts = []
        Dev_hosts = []

        for row in rows:
            if row['dep_name'] == 'IT':
                IT_hosts.append(row)
            elif row['dep_name'] == 'Creative':
                Creative_hosts.append(row)
            elif row['dep_name'] == 'Develop':
                Dev_hosts.append(row)

        print("主机组如下所示")

        print("IT部门主机:".center(40, '*'))
        for item in IT_hosts:
            print(item)

        print("Creative部门主机:".center(40, '*'))
        for item in Creative_hosts:
            print(item)

        print("Develope部门主机:".center(40, '*'))
        for item in Dev_hosts:
            print(item)

        option = input("请选择主机组编号\n>>>")

        if option == '1':
            ss = 'IT'
            num=len(IT_hosts)
        elif option == '2':
            ss = 'Creative'
            num=len(Creative_hosts)
        elif option == '3':
            ss = 'Develop'
            num=len(Dev_hosts)

        value={'label':ss,'num':num}
        return value

    # def count(self):
    #     print(self.result.method.message_count)

#找到绝对路径
parent_path = os.path.abspath(os.pardir)
# print(parent_path)
config_path=os.path.join(parent_path,"config",'db.config')
config_path2=os.path.join(parent_path,"config","RabbitMQ.config")
log_path=os.path.join(parent_path,"log","client.log")
logging.basicConfig(filename=log_path, level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def run():
# 实例化对象
    request_rpc = RpcClient()
    print(" [x] 准备发送RPC请求 ")
    while True:
        ipt=input("请输入远程命令:\n>>>")
        # 调用call，发送数据
        # ipt=int(ipt)
        response = request_rpc.call(ipt)
        logging.info('RPC request: %s' % ipt)

        # fibonacci_rpc.channel.start_consuming()
        #根据每个部门的主机个数判断应该取多少次数据,延时为1秒
        print("[x] 等待读取结果...")
        for i in range(request_rpc.num):
            request_rpc.connection.process_data_events(time_limit=1)


if __name__ == '__main__':
    run()