
# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li
# !/usr/bin/env python
import pika
import os
#部门标签，当前主机属于的部门
tags=[]
#生成的随机队列名称
queue_name=""
parent_path = os.path.abspath(os.pardir)
config_path=os.path.join(parent_path,"config",'db.config')
config_path2=os.path.join(parent_path,"config",'RabbitMQ.config')

#从数据库获取当前主机的部门，通过部门名称来绑定队列
def severty():
    global tags
    import pymysql

    #判断数据库配置文件是否存在，不在的话创建
    if not os.path.isfile(config_path):
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


    #读取配置文件内容
    ss=""
    fp = open(config_path, 'r', encoding='utf-8')
    for line in fp:
        if line.strip().startswith('host'):
            host = line.strip().split("=")[1].strip()
        if line.strip().startswith('port'):
            port = line.strip().split("=")[1].strip()
        if line.strip().startswith('user'):
            user = line.strip().split("=")[1].strip()
        if line.strip().startswith('passwd'):
            passwd = line.strip().split("=")[1].strip()
        if line.strip().startswith('db'):
            db = line.strip().split("=")[1].strip()

    # print(host, port, user, passwd, db)

    #查询数据库，获取信息
    conn = pymysql.connect(host=host, port=int(port), user=user, passwd=passwd, db=db)
    # conn = pymysql.connect(host='sydnagios', port=3306, user='yli', passwd='yli', log='mydb')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select * from Hosts INNER JOIN Department on Hosts.department_id=Department.dep_id")
    rows = cursor.fetchall()

    name=os.popen('hostname').read()
    # print(name)

    #根据主机名进行匹配
    for row in rows:
        # print(row['host_name'])
        if row['host_name'].lower().strip()==name.lower().strip():
            tags.append(row['dep_name'])


    # return tags


def execute():

    global queue_name
    if not os.path.isfile(config_path2):
        print("没有找到RabitMQ服务器的信息，请配置！")
        server_name = input("RabbitMQ服务器")
        msg = 'server=%s' % server_name
        fp = open(config_path2, 'w', encoding='utf-8')
        fp.write(msg)
        fp.close()


    #读取RabbitMQ的配置文件
    ft = open(config_path2, 'r', encoding='utf-8')
    for line in ft:
        if line.strip().startswith('server'):
            server_name = line.split("=")[1]

    # print(server_name)
    # 绑定broker，创建一个队列
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=server_name))
    channel = connection.channel()
    # 设定Exchange类型为Direct
    channel.exchange_declare(exchange='direct_logs_test_1',
                             type='direct')
    tt = [ 'Creative', ]

    # 随机创建队列，exclusive=True表示当我们断开和消费者的连接，这个queue会自动删除
    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue

    print("创建随机队列%s"%queue_name)
    print("读取数据库...")
    severty()
    print("本机属于以下部门%s"%tags)
    for t in tags:
        # print(t)
        channel.queue_bind(exchange='direct_logs_test_1',
                           queue=queue_name,
                           routing_key=t)
        # channel.queue_bind(exchange='logs_fanout',
        #                queue=queue_name)

    print("队列绑定到 Exchange")

    # 负载平衡
    channel.basic_qos(prefetch_count=1)

    # 接受请求之后，自动调用on_request,内部执行函数，然后发回结果
    channel.basic_consume(on_request, queue=queue_name)
    print(" [x] 等待 RPC 请求")
    #死循环读取信息
    channel.start_consuming()

# 定义一个回调函数给basic_consume使用
def on_request(ch, method, props, body):
    n = body.decode()
    print(" [.] 收到请求命令(%s)" % n)
    # response = fib(n)

    response=os.popen(n).read()
    # 把结果发布回去
    print(response)

    hostname=os.popen('hostname').read()
    msg="queue: "+queue_name+"\n"+"host: "+hostname+"\n"+response+"\n---------------------------"

    #发回结果和correlation_id
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id= \
                                                         props.correlation_id),
                     body=msg)

    ch.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == '__main__':
    execute()