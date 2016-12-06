#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://yli:yli@sydnagios:3306/mydb", max_overflow=5)

Base = declarative_base()

class Department(Base):
    __tablename__ = 'Department'
    dep_id = Column(Integer, primary_key=True,autoincrement=True)
    dep_name = Column(String(32), index=True, nullable=True)

class Hosts(Base):
    __tablename__ = 'Hosts'
    host_id = Column(Integer, primary_key=True,autoincrement=True)
    host_name=Column(String(32))
    host_ip=Column(String(32))
    department_id = Column(Integer,ForeignKey(Department.dep_id))

#
Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

list1=["IT","Creative","Devlop"]
for item in list1:
    obj = Department(dep_name=item)
    session.add(obj)
session.commit()

q = session.query(Department)
print(q)
ret = q.all()
print(ret)
print(ret[0].dep_name)

list2=[{'host_name':'sydnagios','host_ip':'10.2.1.107','department_id':1},{'host_name':'localhost','host_ip':'127.0.0.1','department_id':2}]

for item in list2:
    obj=Hosts(host_name=item['host_name'],host_ip=item['host_ip'],department_id=item['department_id'])
    print(obj)
    session.add(obj)
session.commit()


q=session.query(Department)
