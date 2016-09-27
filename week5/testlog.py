#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li
import logging

logging.basicConfig(filename='log1',
                    level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

logging.info("log1")

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(filename='log2',
                    level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

logging.info("log2")