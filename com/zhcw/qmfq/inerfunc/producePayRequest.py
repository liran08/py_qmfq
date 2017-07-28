#订单支付(10040306)

from com.zhcw import qmfq
from com.zhcw.qmfq.data.res_data.OrderPay10040306 import OrderPay
from com.zhcw.qmfq.execTestCase import execRequest

from com.zhcw.qmfq.tools import  ResponseDataAnayls
from com.zhcw.qmfq.tools.BaseParamTools import BaseParamTools
from com.zhcw.qmfq.tools.FileOperator import FileOperator


class ProducePay:
    __r__=''
    def setParam(self,item,name,userId,cookie):
        fpn = FileOperator().getFileConfigName()

        bp = BaseParamTools.getParam(fpn,name)
        if bp is None :
            # print("没有找到测试的参数名")
            raise Exception("没有找到测试的参数名")
            return  False

        param = bp.getBodyParam().replace("{itemId}",item.getItemId()).replace("{issueName}",item.getIssueName())
        param =param.replace("{userId}", userId)
        pm = qmfq.req_param.replace("*", bp.gettransactionType()).replace("#", bp.getSrc()).replace("%", param)
        # print("pm:", pm)
        if bp.getreqType()=="get":
            ProducePay.__r__ = execRequest.request_get(qmfq.url,pm,cookie)
        else:
            ProducePay.__r__ = execRequest.request_post(qmfq.url, pm,cookie)

        if ProducePay.__r__.status_code != 200:
            raise Exception("请求接口异常：{:d}".format(ProducePay.__r__.status_code))
            return False

        return True

    def request_zhengchang(self,item,name,userId,cookie):
        if ProducePay().setParam(item,"producePayzhengchangzhifu",userId,cookie):
            return ProducePay().setProducData(name)
        else:
            return None

    def setProducData(self, name):
        body = ResponseDataAnayls.getBodyDatafromResponseData(ProducePay.__r__)
        pld = OrderPay()
        pld.setResCode(body["resCode"])
        pld.setMessage(body["message"])
        pld.setMethonName(name)
        pld.setTestCaseName("request_zhengchang -- 商品支付")
        if "issueId" in body :
            pld.setIssueId(body['issueId'])
            pld.setMaAccount(body['maAccount'])
            pld.setAccount(body['account'])
        if pld.getResCode() != "000000":
            raise Exception("请求接口失败：message = {:s},resCode = {}".format(body["message"],body["resCode"]))
        return pld
