#商品列表(10040201)

from com.zhcw import qmfq
from com.zhcw.qmfq.data.res_data.ProduceListData10040201 import ProduceListData
from com.zhcw.qmfq.execTestCase import execRequest
from com.zhcw.qmfq.tools import ResponseDataAnayls
from com.zhcw.qmfq.tools.BaseParamTools import BaseParamTools
from com.zhcw.qmfq.tools.FileOperator import FileOperator


class ProduceList:

    __r__=''
    def setParam(self,name):
        fpn = FileOperator().getFileConfigName()

        bp = BaseParamTools.getParam(fpn,name)
        if bp is None :
            # print("没有找到测试的参数名")
            raise Exception("没有找到测试的参数名")
            return  False

        param = bp.getBodyParam()
        # print(param)
        pm = qmfq.req_param.replace("*", bp.gettransactionType()).replace("#", bp.getSrc()).replace("%", param)
        # print("pm:", pm)
        if bp.getreqType()=="get":
            ProduceList.__r__ = execRequest.request_get(qmfq.url,pm,'')
        else:
            ProduceList.__r__ = execRequest.request_post(qmfq.url, pm,'')

        if ProduceList.__r__.status_code != 200:
            raise Exception("请求接口异常：{:d}".format(ProduceList.__r__.status_code))
            return False

        return  True

    def my_request(self,name):

        if ProduceList().setParam(name):
            return ProduceList().setProduceListData(name)
        else :
            return  None

    def setProduceListData(self,name):

        body = ResponseDataAnayls.getBodyDatafromResponseData(ProduceList.__r__)
        pld = ProduceListData()
        pld.setResCode(body["resCode"])
        pld.setMessage(body["message"])
        if "itemList" in body :
            iList = body["itemList"]
            list = []
            for l in iList:
                item = ProduceListData().ItemList()
                item.setIssueId(l["issueId"])
                item.setIssueName(l["issueName"])
                item.setItemId(l["itemId"])
                list.append(item)
            pld.setItemList(list)
            pld.setMethonName(name)
            pld.setTestCaseName("request_canshu_zhengque --商品列表")
            ll = pld.getItemList()
        if pld.getResCode() != "000000":
            raise Exception("请求接口失败：message = {:s},resCode = {}".format(body["message"], body["resCode"]))
        return pld

# if __name__ == "__main__":
#     Request().my_request()