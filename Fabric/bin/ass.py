#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li
import os, sys

parent_path = os.path.abspath(os.pardir)

path = parent_path + "\src"

sys.path.append(path)

import Fabric

if __name__ == '__main__':
    Fabric.display()

