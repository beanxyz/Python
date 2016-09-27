#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li
import re
a=re.findall('al.*x','jskldflsalx')
#. 匹配除换行符以外的任何1个字符
# * 匹配0或者多次任意字符
#.* 任意0个或者多个字符
#+ 匹配1到多次
#？0或者1次
# {X,y} x到y次

print(a)


# []里面元字符没有意义了，-表示范围
#^在【】里面表示非的意思了，\d数字

b=re.findall('a[bc]d','abd')
b=re.findall('a[bc]d','acd')
b=re.findall('a[a-z]d','azd')
b=re.findall('a[a-z]+d','azdd')

b=re.findall('a[a*]d','aad')
b=re.findall('a[^2]d','a2d')

"""
finall，找到所有匹配结果  finditer（）
match, 只有起始位置,返回一个match对象，group(1)返回第一个
search,可以从半截找，返回一个对象，但是也只有第一个结果的信息

sub 替换
res.sub('g.t','have','get, got, gut',2)  最大替换次数

subn还多显示一个替换的次数

split

re.split（'\d+','on23k2kl2ikll2')
import re
text='dksljklsdjklfjsldf cool jkljl l ; '
regex=re.compile(r'\w*oo\w*')
print regex.findall(text)

re.search('\\com','ksjdfl\com')
re.search(r'\\com','kllkkl\com')  r表示原生字符
re.search('\\\\','\kldfls') python需要2个转移，re还需要两个转移
注意有的特殊符号\b在python和正则里面都有不同意义，所以尽量用r原生字符或者\转移

re.search('\\bbolg','bolg')

"""

print(b)