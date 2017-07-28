import unittest
import os
import re
import time

import sys

from com.zhcw.qmfq.tools import SendMail
from com.zhcw.qmfq.tools.HTMLTestRunner import HTMLTestRunner


class QMFQ_TestSuit(unittest.TestCase):
    
    def createTestSuiteMap(self):
        path = os.getcwd()
        files = os.listdir(path)
        
        test = re.compile("^test")
        csf = filter(test.search, files)   
        filenameToModuleName = lambda f: os.path.splitext(f)[0]  
        moduleNames = map(filenameToModuleName, csf)           
        modules = map(__import__, moduleNames)     
                        
        load = unittest.defaultTestLoader.loadTestsFromModule    
        t_suites = unittest.TestSuite(map(load, modules))
        t = time.strftime('%Y-%m-%d%H:%M:%S')
        t = t.replace("-","").replace(":","")
        filename = path  + '\\result-'+t+'.html'
        fp = open(filename, 'wb')
        HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况：').run(t_suites)
        fp.close()

        SendMail.SendMailTestReport().sendMail(filename)

if __name__ == '__main__':
    print(sys.path)
    qd = QMFQ_TestSuit()
    qd.createTestSuiteMap()
