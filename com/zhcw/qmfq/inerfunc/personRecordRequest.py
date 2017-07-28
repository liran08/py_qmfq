#个人记录 接口实现

from com.zhcw import qmfq
from com.zhcw.qmfq.execTestCase import execRequest
from com.zhcw.qmfq.tools import ResponseDataAnayls
from com.zhcw.qmfq.tools.BaseParamTools import BaseParamTools
from com.zhcw.qmfq.data.res_data.UserProduceRecod10040304 import UserRecod
from com.zhcw.qmfq.tools.FileOperator import FileOperator


class UserRecorde:
    __res__ = ""
    def setParam(self,userId,cookie,name):
        fpn = FileOperator().getFileConfigName()
        bp = BaseParamTools.getParam(fpn,name)
        if bp is None :
            raise Exception("没有找到测试的参数名")
            return  False

        param =bp.getBodyParam().replace("{userId}", userId)
        pm = qmfq.req_param.replace("*", bp.gettransactionType()).replace("#", bp.getSrc()).replace("%", param)
        if bp.getreqType()=="get":
            UserRecorde.__res__ = execRequest.request_get(qmfq.url,pm,cookie)
        else:
            UserRecorde.__res__ = execRequest.request_post(qmfq.url, pm,cookie)

        if UserRecorde.__res__.status_code != 200:
            raise Exception("请求接口异常：{:d}".format(UserRecorde.__res__.status_code))
            return False
        return  True

    def request_zhengchang(self,userId,cookie,name):
        if UserRecorde().setParam(userId,cookie,name):
            return UserRecorde().setPersonRecord(name,userId)
        else :
            return None

    def setPersonRecord(self,name,userId):
        body = ResponseDataAnayls.getBodyDatafromResponseData(UserRecorde.__res__)
        userRecord = UserRecod()
        if "list" in body:
            userRecord.setList(body["list"])
            userRecord.setTotalNum(body["totalNum"])
        userRecord.setResCode(body["resCode"])
        userRecord.setMessage(body["message"])
        userRecord.setMethonName(name)
        userRecord.setTestCaseName("UserBuyNumber--个人记录")
        if userRecord.getResCode() != "000000":
            raise Exception("请求接口失败：message = {:s},resCode = {}".format(body["message"],body["resCode"]))
        userRecord(userId)
        return userRecord
