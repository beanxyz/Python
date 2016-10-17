#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li

def f1():
    print("f1")


print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')


def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30, 38):
            s1 = ''
            for bg in range(10, 48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')


print_format_table()

print('\x1b[7;32;10m' + 'Success!' + '\x1b[0m')

print('\x1b[7;31;10m' + 'Failed!' + '\x1b[0m')
