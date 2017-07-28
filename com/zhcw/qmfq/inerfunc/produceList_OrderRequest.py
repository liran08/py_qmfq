
from com.zhcw import qmfq
from com.zhcw.qmfq.data.res_data.ProduceListData10040201 import ProduceListData
from com.zhcw.qmfq.execTestCase import execRequest
from com.zhcw.qmfq.tools import  ResponseDataAnayls
from com.zhcw.qmfq.tools.BaseParamTools import BaseParamTools
from com.zhcw.qmfq.tools.FileOperator import FileOperator


class ProduceListOrder:
    __r__ =""
    def getProduceList(self,name):
        fpn = FileOperator().getFileConfigName()
        bp = BaseParamTools.getParam(fpn,name)
        if bp is None :
            # print("没有找到测试的参数名")
            raise Exception("没有找到测试的参数名")
            return  False

        pm = qmfq.req_param.replace("*", bp.gettransactionType()).replace("#", bp.getSrc()).replace("%", bp.getBodyParam())
        if bp.getreqType()=="get":
            ProduceListOrder.__r__ = execRequest.request_get(qmfq.url,pm,'')
        else:
            ProduceListOrder.__r__ = execRequest.request_post(qmfq.url, pm,'')

        if ProduceListOrder.__r__.status_code != 200:
            raise Exception("请求接口异常：{:d}".format(ProduceListOrder.__r__.status_code))
            return None

        return ProduceListOrder().setProduceListOrder(name)

    def setProduceListOrder(self,name):
        body = ResponseDataAnayls.getBodyDatafromResponseData(ProduceListOrder.__r__)
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
            pld.setTestCaseName("request_zhengchang -- 商品列表按进度排序")
            ll = pld.getItemList()
        if pld.getResCode() != "000000":
            raise Exception("请求接口失败：message = {:s},resCode = {}".format(body["message"], body["resCode"]))
        return pld

# if __name__ == "__main__":
#     ProduceListOrder().getProduceList()