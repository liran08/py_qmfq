import requests
import json

from com.zhcw.qmfq.tools.FileOperator import FileOperator

def responseDataLog(*resp):
    for o in resp:
        m = o.getMessage()
        if m.find("\r\n") :
            m = m.replace("\r\n",",")
        errmessage = "testCaseName={:s},method = {:s},message = {:s},resCode = {:s}".format(o.getTestCaseName(),o.getMethonName(),m, o.getResCode())
        FileOperator().writeResultLog(errmessage)


