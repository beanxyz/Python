#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy import create_engine, and_, or_, func, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, DateTime
from  sqlalchemy.orm import sessionmaker, relationship
import os

Base = declarative_base()  # 生成一个SqlORM 基类
parent_path = os.path.abspath(os.pardir)
config_path=os.path.join(parent_path,'config','db.log')


# print(config_path)
#创建6张表，host和hostuser是多对多关系；hostuser和userprofile是多对多关系，auditlog是日志记录


class Host2HostUser(Base):
    __tablename__ = 'host2hostuser'
    id=Column(Integer,primary_key=True,autoincrement=True)
    host_id = Column(Integer,ForeignKey('host.id'),nullable=False)
    hostuser_id = Column(Integer,ForeignKey('host_user.id'),nullable=False)

class Host(Base):
    __tablename__ = 'host'
    id = Column(Integer, primary_key=True, autoincrement=True)
    hostname = Column(String(64), unique=True, nullable=False)
    ip_addr = Column(String(128), unique=True, nullable=False)
    port = Column(Integer, default=22)

    host_users=relationship('HostUser',secondary=Host2HostUser.__table__,backref='host')


class HostUser(Base):
    __tablename__ = 'host_user'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False)
    password = Column(String(255))


class UserProfile2HostUser(Base):
    __tablename__='userprofile_2_hostuser'
    id=Column(Integer,primary_key=True,autoincrement=True)
    userprofile_id=Column(Integer,ForeignKey('user_profile.id'),nullable=False)
    hostuser_id=Column(Integer,ForeignKey('host_user.id'),nullable=False)

class UserProfile(Base):
    __tablename__ = 'user_profile'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    host_list = relationship('HostUser', secondary=UserProfile2HostUser.__table__, backref='userprofiles')



class AuditLog(Base):
    __tablename__ = 'audit_log'
    id = Column(Integer, primary_key=True)
    userprofile_id = Column(Integer, ForeignKey('user_profile.id'))
    hostuser_id = Column(Integer, ForeignKey('host_user.id'))
    host_id=Column(Integer,ForeignKey('host.id'))
    cmd = Column(String(255))
    date = Column(DateTime)




engine=''


#读取数据库配置文件信息
if not os.path.isfile(config_path):
    print("错误！请配置数据库文件")
    exit()
else:
    fp=open(config_path,'r')
    for line in fp:
        if line.strip().startswith('username'):
            username=line.split('=')[1].strip()
        if line.strip().startswith('password'):
            password=line.split('=')[1].strip()
        if line.strip().startswith('dbserver'):
            dbserver=line.split('=')[1].strip()
        if line.strip().startswith('db'):
            db=line.split('=')[1].strip()
        if line.strip().startswith('port'):
            port=line.split('=')[1].strip()

    url="mysql+pymysql://%s:%s@%s:%s/%s"%(username,password,dbserver,port,db)
    print(url)
    engine = create_engine(url, max_overflow=5)

    fp.close()



# engine = create_engine("mysql+pymysql://yli:yli@sydnagios:3306/mydb", max_overflow=5)

#创建表
def init_db():
    Base.metadata.create_all(engine)


# 删除表
def drop_db():
    Base.metadata.drop_all(engine)


Session=sessionmaker(bind=engine)
session = Session()



# #插入测试数据，初始化列表
# def insert_data1():
#     session.add(Host(hostname='sydnagios',ip_addr='10.2.1.107', port=22))
#     session.add(Host(hostname='sydapp01',ip_addr='10.2.1.247', port=22))
#     session.add(Host(hostname='jwood-ise',ip_addr='10.2.2.39', port=22))
#
#     session.commit()
#
#
#     session.add(HostUser(username='root',password='Goaaa111'))
#     session.add(HostUser(username='yli',password='Goat333'))
#     session.add(HostUser(username='administrator',password='D11dd0ntGsue55'))
#     session.add(HostUser(username='administrator',password='N11t33t2atfs'))
#     session.commit()
#
#     session.add(Host2HostUser(host_id=1,hostuser_id=1))
#     session.add(Host2HostUser(host_id=1,hostuser_id=2))
#     session.add(Host2HostUser(host_id=2,hostuser_id=4))
#     session.add(Host2HostUser(host_id=3,hostuser_id=3))
#     session.commit()
#
#     session.add(UserProfile(username='yli',password='yli'))
#     session.add(UserProfile(username='alex',password='alex'))
#     session.commit()
#
#     session.add(UserProfile2HostUser(userprofile_id=1,hostuser_id=1))
#     session.add(UserProfile2HostUser(userprofile_id=1,hostuser_id=2))
#     session.add(UserProfile2HostUser(userprofile_id=1,hostuser_id=3))
#     session.add(UserProfile2HostUser(userprofile_id=1,hostuser_id=4))
#     session.add(UserProfile2HostUser(userprofile_id=2,hostuser_id=1))
#     session.add(UserProfile2HostUser(userprofile_id=2,hostuser_id=3))
#     session.commit()

#

def insertHost(hostname,ip,port):
    session.add(Host(hostname=hostname, ip_addr=ip, port=port))
    session.commit()

def insertHostUser(username, password):
    session.add(HostUser(username=username, password=password))
    session.commit()

def insertHost2HostUser(hostid,hostuser):
    session.add(Host2HostUser(host_id=hostid, hostuser_id=hostuser))
    session.commit()

def insertUserProfile(username, password):
    session.add(UserProfile(username=username, password=password))
    session.commit()

def insertUserProfile2HostUser(userprofile_id,hostuser_id):
    session.add(UserProfile2HostUser(userprofile_id=userprofile_id, hostuser_id=hostuser_id))
    session.commit()



def ManageData():
    msg="""
    1.添加主机
    2.添加主机账户
    3.绑定主机和主机账户
    4.添加堡垒机用户
    5.绑定堡垒机用户和主机账户
    6.查看日志
    7.退出
    """

    while True:

        print(msg)

        choice=input('请输入选项')
        if choice=='1':
            hostname=input('请输入主机名 ')
            ip=input("请输入IP ")
            port=input("请输入端口 ")
            try:
                insertHost(hostname,ip,port)
                print("数据添加成功！")

            except Exception as ex:
                print(ex)
        elif choice=='2':
            user=input("请输入主机账户名 ")
            pwd=input("请输入账户密码 ")
            try:
                insertHostUser(user,pwd)
                print("数据添加成功")
            except Exception as ex:
                print(ex)

        elif choice=='3':
            hostname=input("请输入主机名")
            username=input("请输入主机账户")
            pwd = input("请输入账户密码 ")
            try:
                hostid=session.query(Host.id).filter(Host.hostname==hostname).first()
                userid=session.query(HostUser.id).filter(and_(HostUser.username==username , HostUser.password==pwd)).first()
                # print(hostid[0],userid[0])
                insertHost2HostUser(hostid[0],userid[0])
                print("数据添加成功")
            except Exception as ex:
                print(ex)

        elif choice=='4':
            username=input("请输入堡垒机用户名")
            pwd=input("请输入用户密码")
            try:
                insertUserProfile(username,pwd)
                print("数据添加成功")
            except Exception as ex:
                print(ex)

        elif choice=='5':
            username = input("请输入堡垒机用户名")
            user = input("请输入主机账户名 ")
            pwd = input("请输入账户密码 ")
            try:
                huserid=session.query(UserProfile.id).filter(UserProfile.username==username).first()
                userid = session.query(HostUser.id).filter( and_(HostUser.username == user , HostUser.password == pwd)).first()

            # print(huserid,userid)
                insertUserProfile2HostUser(huserid[0],userid[0])
                print("数据添加成功")

            except Exception as ex:
                print(ex)


        elif choice=='6':
            ret=session.query(AuditLog).all()
            for item in ret:
                print("时间%s 堡垒机用户id:%s 主机用户id:%s 主机id:%s 命令:%s"%( item.date,item.userprofile_id, item.hostuser_id,item.host_id,item.cmd))

        elif choice=='7':
            break
        else:
            print("无效输入！")



def run():
    usrname=input("Name: ")
    pwd=input("Pwd: ")

    host_list=[]

    #查询堡垒机用户信息
    obj =session.query(UserProfile).filter(UserProfile.username==usrname,UserProfile.password==pwd).first()

    if obj ==None:
        print("该用户不存在")
        return None
    else:
        #堡垒机用户的ID
        userprofile_id=obj.id
        #host_list通过关联找到主机用户的信息
        for item in obj.host_list:
        #host通过item关联找到主机信息
            for j in item.host:

                temp={'host':j.ip_addr,'hostname':j.hostname,'username':item.username,'pwd':item.password,'userprofileid':userprofile_id,'hostuserid':item.id,'hostid':j.id}
                host_list.append(temp)



    return host_list



if __name__ == '__main__':
    # init_db()
    run()