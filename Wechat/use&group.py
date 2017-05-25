import itchat

itchat.auto_login(hotReload=True)
#
# # 获取自己的用户信息
# a=itchat.search_friends()
# print(a)
# #输出其他好友的信息
# b=itchat.search_friends(nickName='Kai')
# print(b)
#
#输出群聊的成员信息
import re

c=itchat.search_chatrooms(name='专注土澳搬砖几十年')[0]['HeadImgUrl']

# username=c.split('=@')[1].split('&')[0]
username=re.search('@\w+&',c).group()[:-1]
# print(username)
# print(username2 )
member=itchat.update_chatroom(username)
for name in member['MemberList']:
   print("用户 %s"%(name['NickName']))

#输出群聊的记录

# import itchat
#
# newInstance = itchat.new_instance()
# newInstance.auto_login(hotReload=True, statusStorageDir='newInstance.pkl')
#
# @newInstance.msg_register(itchat.content.TEXT,isGroupChat=True)
# def reply(msg):
#     print(msg['ActualNickName'] + ":" + msg['Content'])
#
# newInstance.run()
#
# def input_msg():
#     msg=input('Message:')
#     itchat.send(msg,toUserName=username)
#
# while 1:
#     input_msg()

import threading,time


#
# def input_msg():
#
#     msg=input('Message:')
#     itchat.send(msg,toUserName=username)
#     time.sleep(2)

@itchat.msg_register(itchat.content.TEXT,isGroupChat=True)
def get_msg(msg):
    # print(msg)
    print(msg['ActualNickName']+":"+msg['Content'])
    time.sleep(2)

    #
    # t1=threading.Thread(input_msg(),)
    # # t1.setDaemon(True)
    # t1.start()
    # t1.join()

itchat.run()
