#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li

import random
import sys
import time
import json, os, sys
import property
from property import house

from career import careers, public_servant, farmer

parent_path = os.path.abspath(os.pardir)

lovepath = os.path.join(parent_path, 'db', 'love.json')
workpath = os.path.join(parent_path, 'db', 'work.json')


class person:
    # 构造函数，初始化人物
    def __init__(self, name, sex, age, money, title):
        self.name = name
        self.sex = sex
        self.age = age
        self.money = money
        self.relationship = dict()
        self.spouse = ''
        self.title = title
        self.credit = 0
        self.ownlist = []

    def first_meet(self, obj):
        # 好感度随机在50上下波动
        import random
        self.relationship[obj.name] = 50 + random.randint(-10, 10)
        obj.relationship[self.name] = self.relationship[obj.name]

        print("%s和%s认识，关系为%s" % (self.name, obj.name, self.relationship[obj.name]))

    def love_experience(self, obj):
        # 一些随机事件会改变彼此的好感度
        fp = open(lovepath, 'r')

        self.dict2 = json.load(fp)
        import random
        num = random.randint(0, 4)
        v = self.dict2[str(num)]
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
        # 结婚

    def marraige(self, obj):
        # 如果你未婚，她未嫁，那么喜结良缘
        if not self.spouse and not obj.spouse:
            self.spouse = obj.name
            obj.spouse = self.name
            print("\x1b[7;32;40m%s和%s牵手成功\x1b[0m" % (self.name, obj.name))
        # 如果已经有了牵挂，而且那个他还不是你，那么只能相逢恨晚
        elif not self.spouse == obj.name:
            print('\x1b[3;19;33m%s和%s相逢恨晚，如果别个还没分手，就别想太多了！\x1b[0m' % (self.name, obj.name))

            # 婚姻的坟墓

    def divore(self, obj):
        if self.spouse == obj.name:
            self.spouse = ''
            obj.spouse = ''
            print("\x1b[6;30;41m%s和%s关系破裂!\x1b[0m" % (self.name, obj.name))

            # 爱情经历

    def show_money(self, obj):
        self.relationship[obj.name] += int(self.money / 10000)
        obj.relationship[self.name] += int(self.money / 10000)
        if self.relationship[obj.name] > 100:
            self.relationship[obj.name] = 100
            obj.relationship[self.name] = 100

        print("%s 展示了他的资产%s" % (self.name, self.money))

    def purchase(self, itemobj):

        balance = self.money - int(itemobj.value)
        if balance > 0:
            self.money = balance
            itemobj.owner = self.name
            self.ownlist.append(itemobj)
            print("\x1b[7;32;40m%s 买了一个%s，价值$%d\x1b[0m" % (self.name, itemobj.name, itemobj.value))
            return True
        else:
            print("\x1b[6;30;41m%s想买%s，但是买不起,仍然是个穷屌丝！\x1b[0m" % self.name, itemobj.name)
            return False


class poor(person):
    def study(self):
        self.credit += 20
        print("%s的学分+20" % self.name)

    def work(self):

        fp = open(workpath, 'r', encoding='utf')
        self.dict = json.load(fp)

        import random
        num = random.randint(0, 4)
        v = self.dict[str(num)]

        self.money += v['value']

        if v['value'] > 0:
            print("\x1b[5;19;32m%s %s,资产变成%d \x1b[0m" % (self.name, v['Event'], self.money))

        else:
            print("\x1b[56;16;31m%s %s,资产变成%d \x1b[0m" % (self.name, v['Event'], self.money))

    def graduate(self):
        if self.credit >= 80:
            print("%s学到了足够的学分，可以毕业了,他的头衔变成了毕业生" % self.name)
            self.title = "Graduate"
            return True
        else:
            print("%s学分不够，必须继续学习" % self.name)
            return False


class rich(person):
    # 钻石礼物
    def diamond_gift(self, obj):
        print("%s给%s送了一个奢侈的礼物" % (self.name, obj.name))

        self.money -= 1000
        self.relationship[obj.name] += 20
        obj.relationship[self.name] += 20

    # 游轮
    def boat(self, obj):
        print("%s带%s去有游艇玩了一个晚上" % (self.name, obj.name))
        self.money -= 50000
        self.relationship[obj.name] += 50
        obj.relationship[self.name] += 50

    # 股票分红
    def dividend(self):
        print("%s取点钱花花" % self.name)
        self.money += 50000


class girl(person):
    def shopping(self):
        pass


# class house:
#     def __init__(self, name, add, value):
#         self.name = name
#         self.add = add
#         self.value = value
#         self.owner = ''


# 初始化人物


JOHN = poor('John', 'male', 20, 1000, 'student')
LIZ = girl('Liz', 'female', 18, 5000, 'student')
PETER = rich('Peter', 'male', 25, 1000000000, 'boss')


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()  # defeat buffering
        time.sleep(0.01)


# 大学生活
def Uni_life():
    msg = """故事即将开始，John经过努力，成功的考入了本市的一所大学。在大学的新生晚会上，John意外邂逅了一个美丽的女孩Liz.现在，我们将镜头切换到John

    """

    slowprint(msg)
    # print(msg)
    slowprint("John（心理活动）:好靓的妞儿，我要去认识一下！")

    while True:
        option = input('1.去认识一下MM\n2.不，还是算了\n>>>')
        if option == '1':
            JOHN.first_meet(LIZ)
            break
        elif option == '2':
            slowprint("John(心理活动）：不行， 鼓起勇气还是得认识一下！")
        else:
            print("不能胡思乱想了！！")

    slowprint("经过一番洽谈，两人很快熟悉了起来，成为了朋友。再接下来的日子里，John不断地向Liz发出邀请，两人的关系发生了变化，同时John也面临着经济和学习的压力，镜头再次切换都John")

    for i in range(10):

        option = input('1.谈恋爱\n2.想办法弄点钱\n3.学习\n4.毕业\n >>>')
        if option == '1':
            JOHN.love_experience(LIZ)
            if JOHN.relationship[LIZ.name] >= 90:
                JOHN.marraige(LIZ)
            elif JOHN.relationship[LIZ.name] <= 40:
                JOHN.divore(LIZ)
            continue
        elif option == '2':
            JOHN.work()
            continue
        elif option == '3':
            JOHN.study()
            continue
        elif option == '4':
            ret = JOHN.graduate()
            if ret:
                slowprint("John成功滴地大学毕业了，这个时候他和Liz的关系是%d" % JOHN.relationship[LIZ.name])
                break

    if not JOHN.graduate():
        slowprint("很遗憾 4年过去了，John没有能够成功毕业，被强制离校成为社会闲散人员")
        JOHN.title = 'Loser'


# 进入社会,高富帅横刀夺爱
def Career_life():
    slowprint("这个时候，一个大腹便便的男子出现了，他的名字叫做Peter，是本市一家上市公司的大少爷")
    slowprint("Peter(心理活动）：哟西！这个妞不错，她归我了！")
    slowprint("Peter开着跑车到Liz面前，做了自我介绍")
    PETER.first_meet(LIZ)
    slowprint("镜头切换到Peter")

    for i in range(10):
        print("Peter".center(40, '*'))
        option = input("1.妞你就跟我混吧\n2.送钻石礼物\n3.去游艇玩\n4.展示资产\n5.股票分红")
        if option == '1':
            if LIZ.relationship[PETER.name] > LIZ.relationship[JOHN.name]:
                print("Liz被Peter的金弹攻势打动了，决定抛弃John了")

                if LIZ.spouse == 'John':
                    LIZ.divore(JOHN)

                LIZ.marraige(PETER)
                break
            else:
                print("Liz对John还存有好感，拒绝了Peter的邀请")
        elif option == '2':
            PETER.diamond_gift(LIZ)
        elif option == '3':
            PETER.boat(LIZ)
        elif option == '4':
            PETER.show_money(LIZ)
        elif option == '5':
            PETER.dividend()


def fight():
    slowprint("John很伤心，也很愤怒LIZ的背叛，他决定奋发图强。")
    if JOHN.title == 'Graduate':
        slowprint("幸好John以优异的成绩毕业了，因此他成功考入了公务员系统")
        p1 = public_servant('公务员', JOHN)
        slowprint("就在Liz享受着上流社会的纸醉金迷时，John在社会上努力拼搏着")


    else:
        print("John只能回家种田去了")
        p1 = farmer('农民', JOHN)

    for i in range(50):
        print('John'.center(40, '*'))
        opt = input("1.上班\n2.随机事件\n3.买房子\n4.自我感觉不错了去参加同学会显摆一下")
        if opt == '1':
            p1.work()
            print("John的现有资金积攒到%d" % JOHN.money)
        elif opt == '2':
            JOHN.work()
        elif opt == '3':
            print("当前可以购买的房子如下所示\n")
            key = ''
            for item in enumerate(property.houselist):
                index = item[0]
                key = index
                # print(item[1])
                name = item[1].name
                add = item[1].add
                price = item[1].value
                print(index, name, price)

            while True:
                opt = input("输入你希望购买的房屋编号")
                if opt.isdigit():
                    opt = int(opt)
                    if opt < len(property.houselist):
                        break
                    else:
                        print("超出边界！请重新输入")
                else:
                    print("错误输入！请重新输入")
            if JOHN.money > property.houselist[opt].value:
                print("购买成功！")
                JOHN.purchase(property.houselist[opt])
            else:
                print("对不起，您的钱不够请稍后再来！")

        elif opt == '4':
            slowprint("JOHN打算去参加同学会，去看看当年的老同学都怎么样了")
            break

        else:
            print("别胡思乱想混日子了，赶快行动起来")


def change():
    slowprint("随着时间的推移，Peter逐渐厌烦了Liz...")
    for i in range(10):
        print("Peter".center(40, '*'))
        opt = input("1.殴打Liz\n2.吵架\n3.大保健\n4.给Liz道歉")
        if opt == '1':
            LIZ.relationship[PETER.name] -= 30
            PETER.relationship[LIZ.name] -= 30
        elif opt == '2':

            LIZ.relationship[PETER.name] -= 20
            PETER.relationship[LIZ.name] -= 20
        elif opt == '3':

            LIZ.relationship[PETER.name] -= 30
            PETER.relationship[LIZ.name] -= 30
        elif opt == '4':
            LIZ.relationship[PETER.name] += 10
            PETER.relationship[LIZ.name] += 10
        else:
            print("我当年为啥会去找这个傻妞？！")
        if PETER.relationship[LIZ.name] < 30:
            PETER.divore(LIZ)
            break
    if PETER.relationship[LIZ.name] < 30:
        PETER.divore(LIZ)
    else:
        print("这不科学，剧本不是这样的")


def oldmate():
    slowprint("John回到校园，这是他当年伤心也快乐过的地方，意外的，他竟然看见了Liz，Liz的容貌仍然和当初相似...")
    if LIZ.spouse != "Peter":
        slowprint("经过交谈，John发现Liz已经因为家暴和PETER分手了，Liz痛哭地说，我错了，我当初不应该抛弃你，我们还可以重新开始吗")

        print("John:".center(40, '*'))
        opt = input("1.往事如烟，我们已经覆水难收了！\n2.我也很想念你，昔日的旧船票是否还能登上你的小船\n>>>")

        if opt == '1':
            slowprint("John 拒绝了Liz的示爱，转身离去，留下一个深深地背影")
        elif opt == '2':
            slowprint("John 决定再给Liz一次机会，看看相处如何")
            for i in range(10):
                JOHN.love_experience(LIZ)
            if JOHN.relationship[LIZ.name] > 90:
                slowprint("John 决定和LiZ再系前缘")
                JOHN.marraige(LIZ)
            elif JOHN.relationship[LIZ.name] > 50:
                slowprint("John 决定两人不适合 还是做个普通朋友吧")
            else:
                slowprint("果然是个大错误！John和Liz的性格南辕北辙，格格不入，最后只能劳燕分飞")

    else:
        slowprint("经过交谈，John发现Liz现在和Peter过的很好，只能衷心地祝福，然后默默离去")


def run():
    # 大学的美好生活
    Uni_life()
    # 残酷的社会，土豪横刀多爱
    Career_life()
    # 屌丝逆袭的奋斗
    fight()
    # 分手了！
    change()
    # 重逢
    oldmate()
    slowprint("The End".center(40, '*'))


if __name__ == '__main__':
    run()
