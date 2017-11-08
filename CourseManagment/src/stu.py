
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li


import pickle
import hashlib
import logging
import os
from admin import student,teacher,training

#获取相对位置的文件路径
parent_path=os.path.abspath(os.path.pardir)
# ttt=os.path.join(parent_path,"config",'atm.config')
teachpath = os.path.join(parent_path, 'db', 'teacher')
courepath=os.path.join(parent_path,'db','training')
stupath=os.path.join(parent_path,'db','student')
logpath=os.path.join(parent_path,'db','log1')

def run():
    #自定义filehandler，以便修改编码为utf-8，支持中文
    logging.basicConfig(handlers=[logging.FileHandler(logpath, 'a', 'utf-8')],
                        level=logging.INFO,
                        format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    f=pickle.load(open(stupath,'rb'))

    INDEX=0
    flag=False
    while flag is False:
        print("欢迎来到学生选课系统，请登录")
        name=input("请输入学生账号")
        pwd=input("请输入密码")
        ss=hashlib.md5()
        ss.update(bytes(pwd,encoding='utf8'))
        pwd1=ss.hexdigest()
        # print(pwd1)

        #登录
        for item in f:
            if name==item.name and pwd1==item.password:
                print("登录成功!")
                print(item.name,item.courselist)
                INDEX=f.index(item)
                flag=True

                break

        if flag==False:
            print("登录失败，请重试!")

    #获取学生的课程对象列表
    clist=f[INDEX].courselist
    if flag:
        msg="""
        0.退出
        1.选课
        2.上课
        3.历史记录

        """

        while True:

            print(msg)

            choice=input("请输入你的选项")

            if choice.isdigit():
                choice=int(choice)
            #退出
            if choice==0:
                exit()

            #选择课程，添加到列表
            elif choice==1:
                fp=pickle.load(open(courepath,'rb'))

                while True:
                    print("目前有以下课程可供选择")

                    for item in enumerate(fp):
                        index = item[0]
                        print(index,item[1].name,item[1].rate,item[1].teacherobj.name)

                    option=input("请输入你需要的课程编号")
                    if option.isdigit():
                        option=int(option)

                    else:
                        print("非法字符输入")
                        continue
                    # print(clist)

                    if option>len(fp):
                        print("超出范围！")
                        continue

                    clist_flag=False

                    #如果列表不为空，判断是否已经包括了当前新选择的内容
                    if clist:
                        for item in clist:
                            if item.name == fp[option].name:


                                print("该课程已经在你的课程表中,提交不会做任何改变")
                                clist_flag=True
                                break


                    else:
                        print("直接添加课程")



                    if clist_flag==False:
                        clist.append(fp[option])

                    #提交整个列表
                    ok=input("是否提交?(y/n)")
                    if ok=='y':
                        f[INDEX].courselist=clist
                        pickle.dump(f,open(stupath,'wb'))
                        break
                    elif ok=='n':
                        pass

            #进行课程的学习

            elif choice==2:
                print("以下内容是您购买的课程")
                # fp=pickle.load(open('student','rb'))
                stu_course_obj=f[INDEX].courselist
                if not stu_course_obj:
                    print("你没有任何选课记录")
                    continue
                else:

                    for item in enumerate(stu_course_obj):
                        index=item[0]
                        print(index,item[1].name,item[1].rate,item[1].teacherobj.name)

                    ipt=input("请选择一门课程编号开始学习")

                    if ipt.isdigit():
                        ipt=int(ipt)
                    else:
                        print("非法输入")

                    ret=stu_course_obj[ipt].train()

                    print(ret)

                    review_flag=False
                    while review_flag is False:
                        review=input("请评价课程质量 (good/bad)")

                        #获取所有的老师对象和课程的任课老师进行匹配
                        ff=pickle.load(open(teachpath,'rb'))

                        tech_flag=False
                        for item in ff:
                            if stu_course_obj[ipt].teacherobj.name==item.name:
                                # 匹配成功
                                tech_flag=True

                                #如果是好评就根据rate发钱给老师，差评就扣钱
                                indexnu=ff.index(item)
                                if review=='good':
                                    ff[indexnu].gain(stu_course_obj[ipt].rate)
                                    print("谢谢好评！")
                                    review_flag=True
                                    logging.info("Student %s Study course %s, teacher %s, review %s"%(name,stu_course_obj[ipt].name,item.name,review))

                                elif review=='bad':
                                    ff[indexnu].disaster(10)

                                    print("请提供差评的强力证件，不然校方会找你麻烦！")
                                    review_flag=True
                                    logging.info("Student %s study course %s, teacher %s, review %s" % (
                                    name, stu_course_obj[ipt].name, item.name, review))

                                else:
                                    print("非法字符，请重新输入(good/bad)")

                                pickle.dump(ff,open(teachpath,'wb'))

                if tech_flag is False:
                    print("错误！找不到相关文件")
            #根据学生的名字搜索关键字
            elif choice==3:
                print("输出学生 %s 的学习记录"%name)
                if not os.path.isfile(logpath):
                    print("没有找到日子文件！")
                else:
                    fp=open(logpath,'r',encoding='utf8')
                    for line in fp:
                        if name in line:
                            print(line.strip())

if __name__ == '__main__':
    run()