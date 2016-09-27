
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li

# http://t.51cto.com/exam/view?id=1021
# 选课系统：
# 管理员：
# 创建老师：姓名、性别、年龄、资产
# 创建课程：课程名称、上课时间、课时费、关联老师
# 学生：用户名、密码、性别、年龄、选课列表[]、上课记录{课程1：【di,a,】}
#
# 1. 管理员设置课程信息和老师信息
# 2. 老师上课获得课时费
# 3. 学生上课，学到“上课内容”
# 4. 学生可自选课程
# 5. 学生可查看已选课程和上课记录
# 6. 学生可评价老师，差评老师要扣款
# 7. 使用pickel



#测试版本，创建老师，创建课程，互相关联
import pickle
import hashlib,os

class teacher:
    def __init__(self,name,age,sex,money):
        self.name=name
        self.age=age
        self.sex=sex
        self.money=int(money)

    def gain(self,value):
        self.money+=int(value)

    def disaster(self,value):
        self.money-=value

class training:
    def __init__(self,name,rate,teacherobj):
        self.name=name
        self.rate=rate
        self.teacherobj=teacherobj

    def train(self):
        # self.teacherobj.gain(self.rate)
        result=self.name+" exp +10"
        return result

class student:
    def __init__(self,name,password,sex,age,courselist=list()):
        self.name=name
        self.password=password
        self.sex=sex
        self.age=age
        self.courselist=courselist


parent_path=os.path.abspath(os.path.pardir)
# ttt=os.path.join(parent_path,"config",'atm.config')
teachpath = os.path.join(parent_path, 'db', 'teacher')
courepath=os.path.join(parent_path,'db','training')
stupath=os.path.join(parent_path,'db','student')


print(parent_path)
#通过配置文件获取管理员和用户文件的路径

# if not os.path.isfile(os.path.join(parent_path,"config",'atm.config')):
#     exit("配置文件不存在！")

def run():
    print("欢迎来到管理界面")
    msg="""
    0.退出
    ------教师系统-------------
    1.创建教师档案
    2.保存教师档案
    3.读取教师档案
    ------课程系统-------------
    4.创建课程档案
    5.保存课程档案
    6.读取课程档案
    ------学生系统-------------
    7.创建学生档案
    8.保存学生档案
    9.读取学生档案
    """




    #初始化教师列表,如果有记录，读取记录，否则创建一个空列表

    if os.path.isfile(teachpath):
        a=pickle.load(open(teachpath,'rb'))
    else:
        a=list()


    #初始化课程列表

    if os.path.isfile(courepath):
        b=pickle.load(open(courepath,'rb'))
    else:
        b=list() #course


    #初始化学生列表
    if os.path.isfile(stupath):
        c=pickle.load(open(stupath,'rb'))
    else:
        c=list()
    while True:
        print(msg)

        choice=input("请输入选项 ")

        if choice.isdigit()==True:
            choice=int(choice)

        if choice==1:
            print("您将设置教师档案")
            name=input("姓名 ")
            age=input("年龄 ")
            sex=input("性别 ")
            money=input("资产 ")
            obj=teacher(name,age,sex,money)
            a.append(obj)

        elif choice==2:
            print("保存您刚刚设置教师档案")

            pickle.dump(a,open(teachpath,'wb'))


        elif choice==3:
            print("读取教师档案记录")
            if not os.path.isfile(teachpath):
                print("教师档案不存在！")
            else:

                fp=pickle.load(open(teachpath,'rb'))
                # print(fp)
                print("教师姓名-年龄-性别-资产".center(40,'-'))
                for item in fp:
                    print("%s-%s-%s-%d"%(item.name,item.age,item.sex,item.money))
                print("-".center(50,'-'))

        elif choice==4:
            print("您将设置课程档案")
            classname=input("课程名称")
            classrate=input("课时费")
            classteacher=input("教师名称")
            fp = pickle.load(open(teachpath, 'rb'))
            # print(fp)
            flag=False
            for item in fp:
                if item.name==classteacher:
                    obj_training=training(classname,classrate,item)
                    b.append(obj_training)
                    flag=True
            if flag==False:
                print("错误:该教师不存在！")


        elif choice==5:
            print("保存您刚刚课程档案")
            pickle.dump(b,open(courepath,'wb'))


        elif choice==6:
            print("读取课程档案")
            if not os.path.isfile(courepath):
                print("课程档案不存在！")
            else:
                fp=pickle.load(open(courepath,'rb'))
                # print(fp,type(fp))
                print("课程名称-课时费-教师姓名".center(40,'-'))
                for item in fp:
                    print("%s-%s-%s"%(item.name,item.rate,item.teacherobj.name))
                print("-".center(50,'-'))

        elif choice==7:
            print("创建学生档案")
            stu_name=input("学生姓名")

            obj=hashlib.md5()
            stu_password=input("学生密码")#We can use hashlib
            obj.update(bytes(stu_password,encoding='utf8'))
            pwd=obj.hexdigest()
            stu_sex=input("性别")
            stu_age=input("年龄")
            s=student(stu_name,pwd,stu_sex,stu_age)




            c.append(s)

        elif choice==8:
            print("保存学生档案")
            pickle.dump(c,open(stupath,'wb'))

        elif choice==9:
            print("读取学生档案")
            if not os.path.isfile(stupath):
                print("错误！学生文档不存在！")
            else:
                f=pickle.load(open(stupath,'rb'))
                print("学生姓名-密码-学生年龄-学生课程表".center(40,'-'))
                for item in f:
                    print(item.name,item.password,item.age,item.courselist)
                print('-'.center(50,'-'))
        elif choice==0:
            exit()


        else:
            print("非法字符输入")


if __name__ == '__main__':
    run()