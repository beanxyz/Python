#!/usr/bin/env python
# -*- coding:utf-8 -*-

class person:
    # 构造函数，初始化人物
    def __init__(self, name, sex, age, money):
        self.name = name
        self.sex = sex
        self.age = age
        self.money = money
        self.relationship = dict()
        self.spouse = ''

    # 工作经历
    def work_experience(self):
        self.dict = {0: {'value': 150000, 'Event': '中三等奖!'},
                     1: {'value': 100000, 'Event': '股票大涨'},
                     2: {'value': -200000, 'Event': '赌博输了'},
                     3: {'value': -100000, 'Event': '住院吃药'},
                     4: {'value': 100000, 'Event': '创业基金投资'},
                     5: {'value': 100000, 'Event': '炒房赚翻了'}
                     }
        import random
        num = random.randint(0, 4)
        v = self.dict[num]

        self.money += v['value']

        if v['value'] > 0:
            print("\x1b[5;19;32m%s %s,资产变成%d \x1b[0m" % (self.name, v['Event'], self.money))

        else:
            print("\x1b[56;16;31m%s %s,资产变成%d \x1b[0m" % (self.name, v['Event'], self.money))




            # 初次邂逅

    def first_meet(self, obj):
        # 好感度随机在50上下波动
        import random
        self.relationship[obj.name] = 50 + random.randint(-10, 10)
        obj.relationship[self.name] = self.relationship[obj.name]

        print("%s和%s认识，关系为%s" % (self.name, obj.name, self.relationship[obj.name]))

    # 结婚
    def marraige(self, obj):
        # 如果你未婚，她未嫁，那么喜结良缘
        if not self.spouse and not obj.spouse:
            self.spouse = obj.name
            obj.spouse = self.name
            print("\x1b[7;32;40m%s和%s牵手成功\x1b[0m" % (self.name, obj.name))
        # 如果已经有了牵挂，而且那个他还不是你，那么只能相逢恨晚
        elif not self.spouse == obj.name:
            print('\x1b[3;19;33m%s和%s相逢恨晚，已经有了牵挂的人了，就别想太多了！\x1b[0m' % (self.name, obj.name))

            # 婚姻的坟墓

    def divore(self, obj):
        if self.spouse == obj.name:
            self.spouse = ''
            obj.spouse = ''
            print("\x1b[6;30;41m%s和%s关系破裂!\x1b[0m" % (self.name, obj.name))

            # 爱情经历

    def love_experience(self, obj):
        # 一些随机事件会改变彼此的好感度
        self.dict2 = {0: {'value': 10, 'Event': '一起看电影!'},
                      1: {'value': 20, 'Event': '调情'},
                      2: {'value': -20, 'Event': '吵架'},
                      3: {'value': -20, 'Event': '抠门'},
                      4: {'value': 30, 'Event': '亲热'},
                      5: {'value': -50, 'Event': '外遇！'}
                      }

        import random
        num = random.randint(0, 4)
        v = self.dict2[num]
        if v['value'] > 0:
            print("\x1b[5;19;32m %s和%s%s \x1b[0m" % (self.name, obj.name, v['Event']))
        else:
            print("\x1b[56;16;31m %s和%s%s \x1b[0m" % (self.name, obj.name, v['Event']))

        self.relationship[obj.name] += int(v['value'])
        obj.relationship[self.name] += int(v['value'])

        # 好感度最多不能超过100
        if self.relationship[obj.name] > 100:
            self.relationship[obj.name] = 100
            obj.relationship[self.name] = 100

        print("当前%s和%s的亲密度是%d" % (self.name, obj.name, self.relationship[obj.name]))

    # 高富帅装逼
    def show_money(self, obj):
        self.relationship[obj.name] += int(self.money / 10000)
        obj.relationship[self.name] += int(self.money / 10000)
        if self.relationship[obj.name] > 100:
            self.relationship[obj.name] = 100
            obj.relationship[self.name] = 100

        print("%s 展示了他的资产%s" % (self.name, self.money))

    def purchase_hosue(self, houseobj):

        balance = self.money - int(houseobj.value)
        if balance > 0:
            self.money = balance
            houseobj.owner = self.name
            print(
                "\x1b[7;32;40m%s 买了一栋房子%s，位于%s,价值$%d\x1b[0m" % (self.name, houseobj.name, houseobj.add, houseobj.value))
            return True
        else:
            print("\x1b[6;30;41m%s想买房子，但是买不起,仍然是个穷屌丝！\x1b[0m" % self.name)
            return False


class house:
    def __init__(self, name, add, value):
        self.name = name
        self.add = add
        self.value = value
        self.owner = ''


# John
John = person('John', 'male', 30, 20)
# liz
Liz = person('Liz', 'female', 22, 30)
# peter
Peter = person('Peter', 'male', 25, 50)

# 2个男人和1个女人的初次见面

print("故事的开端是这样子滴，大学新生见面会上，John,Peter和Liz互相认识了")
John.first_meet(Liz)
Peter.first_meet(Liz)

# 大学4年，20次爱情事件
for i in range(20):
    if John.relationship[Liz.name] > 80:
        John.marraige(Liz)

    if John.relationship[Liz.name] < 30:
        John.divore(Liz)

    if Peter.relationship[Liz.name] > 80:
        Peter.marraige(Liz)

    if Peter.relationship[Liz.name] < 30:
        Peter.divore(Liz)

    John.love_experience(Liz)
    Peter.love_experience(Liz)

if John.spouse != '':
    print("一晃大学4年就过去了~John觉得自己找到了真爱，毕业的时候，%s和%s的亲密度是%d,%s的对象是%s" % (
        John.name, Liz.name, John.relationship['Liz'], John.name, John.spouse))

else:
    print("一晃4年过去了，John和Liz的感情起起伏伏，关系一直不稳定，他们的亲密度是%d" % John.relationship['Liz'])

print("而这个时候，Peter和Liz的亲密度是%d" % Peter.relationship['Liz'])
# ipt=input("输入回车键继续故事".center(40,'-'))

print("这个时候，Peter表示其实他是一个高富帅")
Peter.money += 1000000

Peter.first_meet(Liz)
Peter.show_money(Liz)
print("Liz 和 Peter的亲密度成为%d" % Liz.relationship[Peter.name])
if Liz.spouse == 'John':
    Liz.divore(John)
    print("Liz 决定和John分手")
else:
    print("Liz 决定和Peter好了")

Liz.marraige(Peter)

print("屌丝狗John收到刺激 决定奋发图强")
import random

for i in range(10):
    John.work_experience()

print("经过多年努力，John的资产达到了%d" % John.money)

print("这个时候，John打算买个房子")

houseobj = house('锦绣花园', '人民路4号', 200000)

John.purchase_hosue(houseobj)

print("转眼间10年过去了...")
John.age += 10
Liz.age += 10
Peter.age += 10

print("这个时候，Liz的关系和Peter逐渐恶化，Peter开始在外面找女人")

Liz.divore(Peter)

print("Liz 在同学会上再次碰见了John,这个时候John已经%d岁了，而Liz已经%d岁了" % (John.age, Liz.age))

print("大结局".center(40, '*'))
if houseobj.owner == 'John':

    print("两人相见，唏嘘不已，John的翩（有）翩（大）风（房）度（子）再次吸引了Liz，而John也希望有机会重温旧梦？！")

    John.first_meet(Liz)
    for i in range(20):
        John.love_experience(Liz)

    if John.relationship[Liz.name] > 90:
        print("两个人终于破镜重圆")
    elif John.relationship[Liz.name] < 30:
        print("事实证明，两个性格差异的人最终还是很难走到一起")
    else:
        print("经过一段时间的尝试，John和Liz觉得还是做个普通朋友就好了")

else:
    print('Liz表示过了这么多年 John连个房子都没有，幸好当年没找他！')

print("剧终".center(40, '*'))
