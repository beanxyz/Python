#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li
class Foo:
    abc = 'aaa'

    # 私有的静态字段，私有字段（只能通过类自己调用）
    __abc = 'bbb'

    def __init__(self, name):
        self.name = name
        # 私有的普通字段
        self.__fullname = name

    def show(self):
        print(self.name)
        print(self.__fullname)

    @staticmethod
    def show2():
        print(Foo.abc)

    @staticmethod
    def show3():
        print(Foo.__abc)


ob = Foo('yes')
# print(ob.__name) #因为是私有类型，所以通过对象去调用会报错
print(ob.show())  # 私有类型的普通字段，可以通过类里面的普通方法去间接调用


class Bar(Foo):
    def show3(self):
        print(self.name)


oo = Bar('bar')
print(oo.name)
print(Bar.abc)  # 私有类型的静态字段，如果通过类直接调用，需要使用类的静态方法去间接调用
# Foo.__abc

Foo.show3()

# print(Bar.__abc)

#
# #普通方法
# obj=Foo('hhh')
# obj.show()
#
# #静态方法
# Foo.show2()
#
#
# #普通字段
# print(obj.name)
# #静态字段
# print(Foo.abc)
