# -*- coding: cp936 -*-
'''
���ʹ������ʼ�
С���壺http://www.cnblogs.com/xiaowuyi
'''

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

class SendMailTestReport:
    #����һ����������ʵ��

    def __init__(self):
        SendMailTestReport.msg = MIMEMultipart()
        # ���ʼ�ͷ
        SendMailTestReport.msg['to'] = 'liran@zhcw.com'
        SendMailTestReport.msg['from'] = 'liran@zhcw.com'
        SendMailTestReport.msg['subject'] = '���Ա���'


    def sendMail(self,tcNameFile):
        #���츽��1
        f = tcNameFile.split("\\")
        n =len(f)

        fn = open(tcNameFile, 'rb')
        att1 = MIMEText(fn.read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename='+ f[n-1]#�����filename��������д��дʲô���֣��ʼ�����ʾʲô����
        SendMailTestReport.msg.attach(att1)
        fn.close()
        #�����ʼ�
        try:
            # server = smtplib.SMTP('smtp.163.com')
            server=smtplib.SMTP('mail.zhcw.com')
            # server.login('lixu_03@163.com','19820402.')#XXXΪ�û�����XXXXXΪ����
            server.login('liran@zhcw.com','lr_zhcw1212')#XXXΪ�û�����XXXXXΪ����
            server.sendmail(SendMailTestReport.msg['from'], SendMailTestReport.msg['to'],SendMailTestReport.msg.as_string())
            server.quit()
            print ('���ͳɹ�')
        except Exception as e:
            print (str(e))