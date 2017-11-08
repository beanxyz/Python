#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li
import os, sys

parent_path = os.path.abspath(os.pardir)

path = parent_path + "\src"

sys.path.append(path)

import story, property, career
from story import person, poor, rich, girl

print("欢迎使用我爱讲故事系统，下面请进入模拟人生的故事")
story.run()
