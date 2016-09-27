#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author Yuan Li

def sendmail():
    try:
        import smtplib
        from email.mime.text import MIMEText
        from email.utils import formataddr
        msg = MIMEText('邮件内容', 'plain', 'utf-8')
        msg['From'] = formataddr(["liyuan",'yuan.li@syd.ddb.com'])
        msg['To'] = formataddr(["走人",'38144205@qq.com'])
        msg['Subject'] = "主题"

        server = smtplib.SMTP("outlook.office365.com", 587)
        server.login("yli@syd.ddb.com", "Goat201510")
        server.sendmail('yli@syd.ddb.com', ['yuan.li@live.com','38144205@qq.com'], msg.as_string())
        server.quit()
        print("done")
    except:
        # 发送失败
        return "失败"
    else:
        # 发送成功
        return "cc"

ret = sendmail()


print(ret)
if ret == "cc":
    print('发送成功')
else:
    print("发送失败")