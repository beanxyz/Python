#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li

'''
#Windows is not working
import getpass
username=input("Username:")
password=getpass.getpass("Password:")
print(username,password)


'''

import os
os.system("df -h")
os.mkdir("dir")

res=os.system("df -h")
print(res)  # return 0

res2=os.popen("df -h").read()
print(res2)


'''
复制代码
 1 #!/usr/bin/env python
 2 # python startup file
 3 import sys
 4 import readline
 5 import rlcompleter
 6 import atexit
 7 import os
 8 # tab completion
 9 readline.parse_and_bind('tab: complete')
10 # history file
11 histfile = os.path.join(os.environ['HOME'], '.pythonhistory')
12 try:
13     readline.read_history_file(histfile)
14 except IOError:
15     pass
16 atexit.register(readline.write_history_file, histfile)
17 del os, histfile, readline, rlcompleter
'''



import sys
print(sys.path)