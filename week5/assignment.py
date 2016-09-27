
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li
"""
"
http://t.51cto.com/exam/view?id=1019
ATM：
1. 指定最大透支额度
2. 可取款
3. 定期还款（每月指定日期还款，如15号）
4. 可存款
5. 定期出账单
6. 支持多用户登陆，用户间转帐
7. 支持多用户
8. 管理员可添加账户、指定用户额度、冻结用户等"

bin 入口代码
config 配置文件，
db  日志等等  admin folder （管理员文件）
             userinfo （卡号文件） -- record folder
                                 -- 基本信息 （ 卡号，用户名，密码，credit, balance, saving, enroll-date, expire-date, status, debt)
lib  所有通用代码
src  业务逻辑代码





管理员
    1. 创建用户
           卡号
            记录文件夹
                2016-5-22 每月信息
            基本信息



普通用户



"""