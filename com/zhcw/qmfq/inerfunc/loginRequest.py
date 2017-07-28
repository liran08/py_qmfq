import os

from com.zhcw import qmfq
from com.zhcw.qmfq.execTestCase import execRequest
from com.zhcw.qmfq.tools import ResponseDataAnayls
from com.zhcw.qmfq.tools.FileOperator import FileOperator
from com.zhcw.qmfq.tools.BaseParamTools import BaseParamTools
from com.zhcw.qmfq.data.res_data import Login10020102

class LoginRequest:
    __r__ = ""
    def setParam(self,name):
        fop = FileOperator()
        filePath = fop.getFileConfigName()

        bp = BaseParamTools.getParam(filePath, name)
        if bp is None:
            raise Exception("没有找到测试的参数名")
            return  False

        pm = qmfq.req_param_u.replace("*", bp.gettransactionType()).replace("#", bp.getSrc()).replace("%",
                                                                                                      bp.getBodyParam())
        if bp.getreqType() == "get":
            LoginRequest.__r__ = execRequest.request_get(qmfq.url, pm, "")
        else:
            LoginRequest.__r__ = execRequest.request_post(qmfq.url, pm)

        if LoginRequest.__r__.status_code != 200:
            raise Exception("请求接口异常：{:d}".format(LoginRequest.__r__.status_code))
            return False
        return True

    def login(self,name):
        if LoginRequest().setParam(name):
            return LoginRequest().setLogin(name)
        else :
            return None

    def setLogin(self,name):
        body = ResponseDataAnayls.getBodyDatafromResponseData(LoginRequest.__r__)
        login = Login10020102.Login()
        if "userId" in body:
            login.setUserId(body["userId"])
            login.setCookies(LoginRequest.__r__.cookies)
        login.setTestCaseName("loginTestCase--登录用例")
        login.setMethonName(name)
        login.setMessage(body["message"])
        login.setResCode(body["resCode"])
        if login.getResCode() != "000000":
            raise Exception("请求接口失败：message = {:s},resCode = {}".format(body["message"], body["resCode"]))
        return login