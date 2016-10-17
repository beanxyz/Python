#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li
import os

s = "c:\\temp\junos.msi.zip"

print(len(s))
print(os.stat(s).st_size)
