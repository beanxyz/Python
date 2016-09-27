# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# # Author Yuan Li
#
# 直接import 标准库
# 第三方库 pip install pandas
#
# windows也工作
# >>> import os
# >>> os.system("ipconfig")
#
# Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import os
# >>> r=os.popen("ipconfig").read()
# >>> print(r)
#
#
# pyc 文件，编译-》 字节码文件， 有python虚拟机执行
# 手动执行的时候不会生成pyc文件，频率不高，没必要保存了，导入的话才会生成
#
# 数据类型：type()
#
# int 3.0以后没区别了
# bool 真/假 0 == False, 1==True
# 字符串
# name="yuan li"
# print("My name is "+ name+" and You?")
# print("My name is %s and You?" %name)
# My name is yuan li and You?
#
# 列表：（数组）
#
# >>> name=["zhangsan","lisi","wangwu"]
# >>> name[0]
# 'zhangsan'
# >>> name[-1]
# 'wangwu'
# >>> name[0:1]  可以省略前面或者后面
# ['zhangsan']
# >>> name[-2:-1]
# ['lisi']
#
# 步长
# >>> name[::2]
# ['zhangsan', 'wangwu']
#
# 切片
# >>> name=["h","sjdkf",23,232,["22","33",234]]
# >>> name[4][2]
# 234
#
# 插入
# >>> name.insert(3,"hhhh")
# >>> name
# ['h', 'sjdkf', 23, 'hhhh', 232, ['22', '33', 234]]
#
# 判断是否存在元素
# >>> name
# ['jkjjljlj', 'sjdkf', ['22', '33', 234], 'end']
# >>> 22 in name
# False
# >>> '22' in name
# False
# >>> 'end' in name
# True
# >>> '22' in name[2]
# True
#
#
# 追加
# >>> name.insert(3,"hhhh")
# >>> name
# ['h', 'sjdkf', 23, 'hhhh', 232, ['22', '33', 234]]
#
# 删除 一次只删除一个
# >>> name.remove(23)
# >>> name
# ['h', 'sjdkf', 'hhhh', 232, ['22', '33', 234], 'end']
#
# 一次性删除
# >>> del name[2:4]
# >>> name
# ['h', 'sjdkf', ['22', '33', 234], 'end']
#
# 修改
# >>> name[0]='jkjjljlj'
# >>> name
# ['jkjjljlj', 'sjdkf', ['22', '33', 234], 'end']
#
# 多少个元素
#
# name.count('22')
#
#
# name=[2,2,3,9,23,9,22,21,9]
# for i in range(name.count(9)):
#     index=name.index(9)
#     name[index]=999
# print(name)
#
# 合并
#
# name2=['klk','sdf']
# name.extend(name2)
# print(name)
#
# 排序 混杂字符串和数字在3里面不行，2里面安装anscii排序
# print(name.sort())
#
# 根据索引号删除
# name.pop(2)
# print(name)
#
#
# name=['al','jksf','sdf',[2,3,5],'234']
# name3=name.copy()
# name[0]='AA'
# name[3][1]=99
# print(name)
# print(name3)
#
# import copy
# name=['al','jksf','sdf',[2,3,5],'234']
# name4=copy.deepcopy(name)
# name[3]='22222'
# print(name4)
# print(name)

#tuple

#
# r=(1,3,4,5)
# print(type(r))
#
# print("count of 1:",r.count(1))
# print("index of 3:",r.index(3))
# #string
#
# user = " Yuan Li is a handsome man "
# print(user.strip()) # remove space in the front and end
#
# names="zhangsan, lisi, wanger"
# name2=names.split(",")  #become list
# print(name2)
# print("|".join(name2))
#
# print(names[0])
#
# print('' in names)
#
# print(names.capitalize())
#
# msg="hello,{name}, it's been a long {time}"
# msg2=msg.format(name='Yuan',time= 'period')
# msg3="hhh{0},dddd{1}"
# print(msg2)
# print(msg3.format('Yuuu','222'))
#
# name="abcedefgh"
# print(names[2:5])
#
# print(name.center(40,'-'))
#
# name="abcedefgh"
# print(name.find('e'))
# print(name.find('dddd'))
#
# age=input("your age:")
# if age.isdigit():
#     age=int(age)
# else:
#     print("invalid data type")
#
#
# name="abcedefgh"
# print(name.endswith("fgh"))
#
# print(name.upper())

Flag=False
counter=0
while Flag is not True:
    counter+=1
    if counter>50 and counter <60:
        continue
    elif counter>100:Flag=True
    else:
        print(counter)




