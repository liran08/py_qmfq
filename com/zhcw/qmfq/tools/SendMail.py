# -*- coding: cp936 -*-
'''
发送带附件邮件
小五义：http://www.cnblogs.com/xiaowuyi
'''

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

class SendMailTestReport:
    #创建一个带附件的实例

    def __init__(self):
        SendMailTestReport.msg = MIMEMultipart()
        # 加邮件头
        SendMailTestReport.msg['to'] = 'liran@zhcw.com'
        SendMailTestReport.msg['from'] = 'liran@zhcw.com'
        SendMailTestReport.msg['subject'] = '测试报告'


    def sendMail(self,tcNameFile):
        #构造附件1
        f = tcNameFile.split("\\")
        n =len(f)

        fn = open(tcNameFile, 'rb')
        att1 = MIMEText(fn.read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename='+ f[n-1]#这里的filename可以任意写，写什么名字，邮件中显示什么名字
        SendMailTestReport.msg.attach(att1)
        fn.close()
        #发送邮件
        try:
            # server = smtplib.SMTP('smtp.163.com')
            server=smtplib.SMTP('mail.zhcw.com')
            # server.login('lixu_03@163.com','19820402.')#XXX为用户名，XXXXX为密码
            server.login('liran@zhcw.com','lr_zhcw1212')#XXX为用户名，XXXXX为密码
            server.sendmail(SendMailTestReport.msg['from'], SendMailTestReport.msg['to'],SendMailTestReport.msg.as_string())
            server.quit()
            print ('发送成功')
        except Exception as e:
            print (str(e))