#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li

#需要遵循一个日志格式
import logging
# # 默认是root用户输出的日志
# logging.warning("Warning information")
# logging.critical("server is down")
#
# #所有比info高级的才会记录，debug不会被记录
# logging.basicConfig(filename='ex.log',level=logging.INFO, format='%(asctime)s %(message)s',datefmt='%m/%d%/Y %I:%M:%S %p')
# logging.debug('this message should go to log file')
# logging.info("info message")
# logging.warning('hhh')


#同时打印到屏幕和文件里面
'''
logger: 给用户显示日志
handler:把日志发送到不同的地方
filter:日志过滤
formatter:格式化输出


局部的级别只能比全局的级别高
'''

logger=logging.getLogger('test-log')#先获取logger
logger.setLevel(logging.DEBUG) #全局的日志级别

# 创建console handler
ch=logging.StreamHandler() #日志打印到屏幕
ch.setLevel(logging.DEBUG) #文件输出的日志的级别

#创建file handler
fh=logging.FileHandler("access.log")
fh.setLevel(logging.WARNING)

#创建formatter
#注意不同格式具有哪些意义
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)')

ch.setFormatter(formatter)
fh.setFormater(formatter)

#注册handler到logger
logger.addHandler()

logger.warning("this is a warning")
logger.debug("this is a debug")