#!/usr/bin/env python
#! _*_ coding:utf-8 _*_
# @TIME   : 2018/11/14  22:58
# @Author : Noob
# @File   : send_email.py

import os
import smtplib
from email.mime.text import MIMEText
# from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.header import Header
import cases

def sendEmail(file_html):
    # 打开文件
    f = open(file_html, 'rb')
    # 读取文件内容
    mail_body = f.read()
    # 关闭文件
    f.close()

    # 发送邮箱用户名/密码（授权码）
    user = 'xxx@qq.com'
    password = 'xxx'
    # 发送邮箱
    sender = user
    # 多个接收邮箱，单个收件人的话，直接是receiver='XXX@163.com'
    receiver = [user]
    # 发送邮件主题
    subject = '自动化测试报告'

    # 邮件类型为"multipart/mixed"的邮件包含附件。向上兼容，如果一个邮件有纯文本正文，超文本正文，内嵌资源，附件，则选择mixed类型。
    # MIMEMultipart对象代表邮件本身
    msg = MIMEMultipart('mixed')

    # 附件
    msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msg_html1)
    msg_html1['Content-Disposition'] = 'attachment;filename="TestReport.html"'

    # 邮件正文
    msg_html = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msg_html)

    # 使用三个引号来设置邮件信息，标准邮件需要三个头部信息： From, To, 和 Subject ，每个信息直接使用空行分割
    msg['From'] = user
    msg['To'] = ';'.join(receiver)
    msg['Subject'] = Header(subject, 'utf-8')
    try:
        # 发送邮箱服务器，这里使用第三方服务商smtp——qq邮箱
        smtpserver = 'smtp.qq.com'

        # 实例化 smtplib 模块的 SMTP 对象 smtpObj 来连接到 SMTP 访问，并使用 sendmail 方法来发送信息

        # 第一种发送成功的方式
        # smtp = smtplib.SMTP()
        # smtp.connect(smtpserver, 25)

        # 第二种发送成功的方式
        smtp = smtplib.SMTP_SSL(smtpserver, 465)

        # 第三方发送邮件需要connect或SSL和login
        # login(发送邮件账号, 发送邮件的密码)
        smtp.login(user, password)

        # sendmail(from_addr,to_addrs,msg,...)
        # 1. from_addr:邮件发送者地址
        # 2. to_addrs:邮件接收者地址。字符串列表['接收地址1','接收地址2','接收地址3',...]或'接收地址'
        # 3. msg：发送消息：邮件内容。一般是msg.as_string():as_string()是将msg(MIMEText对象或者MIMEMultipart对象)变为str。
        smtp.sendmail(sender, receiver, msg.as_string())

        # 用于结束SMTP会话
        smtp.quit()
        print('邮件发送成功')
    except smtplib.SMTPException:
        print('error：无法发送邮件')

if __name__ == '__main__':
    example_html = os.getcwd() + '\example.html'
    # 调用模块cases.py的runcases方法
    cases.runcases(example_html)
    sendEmail(example_html)

    print('end')
