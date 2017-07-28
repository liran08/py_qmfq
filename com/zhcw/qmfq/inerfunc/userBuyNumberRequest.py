#认购人次数(10040301)

from com.zhcw import qmfq
from com.zhcw.qmfq.data.res_data.UserBuyNumber10040301 import UserBuyNumber
from com.zhcw.qmfq.execTestCase import execRequest
from com.zhcw.qmfq.tools import  ResponseDataAnayls
from com.zhcw.qmfq.tools.BaseParamTools import BaseParamTools
from com.zhcw.qmfq.tools.FileOperator import FileOperator


class UserBuyNumRequest:
    __res__ =""
    def my_request(self,userId,name,cookie):

        fpn = FileOperator().getFileConfigName()
        bp = BaseParamTools.getParam(fpn,name)
        if bp is None:
            raise Exception("没有找到测试的参数名")
            return False

        param = bp.getBodyParam().replace("{userId}", userId)
        pm = qmfq.req_param.replace("*", bp.gettransactionType()).replace("#", bp.getSrc()).replace("%", param)
        if bp.getreqType()=="get":
            UserBuyNumRequest.__res__ = execRequest.request_get(qmfq.url,pm,cookie)
        else:
            UserBuyNumRequest.__res__ = execRequest.request_post(qmfq.url, pm,cookie)

        if UserBuyNumRequest.__res__.status_code != 200:
            raise Exception("请求接口异常：{:d}".format(UserBuyNumRequest.__res__.status_code))
            return None

        return UserBuyNumRequest().setUserBugData(name)

    def setUserBugData(self,name):
        body = ResponseDataAnayls.getBodyDatafromResponseData(UserBuyNumRequest.__res__)
        userNum = UserBuyNumber()
        if "list" in body:
            userNum.setEncashNum(body["list"])
            userNum.setEncashTotal(body["encashTotal"])
        userNum.setResCode(body["resCode"])
        userNum.setMessage(body["message"])
        userNum.setMethonName(name)
        userNum.setTestCaseName("UserBuyNumber--认购人次数")
        if userNum.getResCode() != "000000":
            raise Exception("请求接口失败：message = {:s},resCode = {}".format(body["message"],body["resCode"]))
        return userNum
