#基本信息(10040101)

from com.zhcw import qmfq
from com.zhcw.qmfq.data.res_data.ProduceInfoData10040101 import ProduceInfoData
from com.zhcw.qmfq.execTestCase import execRequest
from com.zhcw.qmfq.tools import  ResponseDataAnayls
from com.zhcw.qmfq.tools.BaseParamTools import BaseParamTools
from com.zhcw.qmfq.tools.FileOperator import FileOperator


class ProduceInfo:
    __res__ =""
    def setParam(self,name):
        # filePath = os.path.abspath(os.path.dirname(sys.argv[0]))
        # fpn = filePath.__add__("\param.conf")
        fpn = FileOperator().getFileConfigName()
        bp = BaseParamTools.getParam(fpn,name)
        if bp is None:
            raise Exception("没有找到测试的参数名")
            return False

        pm = qmfq.req_param.replace("*", bp.gettransactionType()).replace("#", bp.getSrc()).replace("%", bp.getBodyParam())

        if bp.getreqType()=="get":
            ProduceInfo.__res__ = execRequest.request_get(qmfq.url,pm,"")
        else:
            ProduceInfo.__res__ = execRequest.request_post(qmfq.url, pm,"")
        if ProduceInfo.__res__.status_code != 200:
            raise Exception("请求接口异常：{:d}".format(ProduceInfo.__res__.status_code))
            return False
        return True

    def request_zhengchang(self,name):
        if ProduceInfo().setParam(name):
            return ProduceInfo().setProduceInfoData(name)

    def setProduceInfoData(self,name):

        body = ResponseDataAnayls.getBodyDatafromResponseData(ProduceInfo.__res__)
        pid = ProduceInfoData()
        pid.setResCode(body["resCode"])
        pid.setMessage(body["message"])
        pid.setMethonName(name)
        pid.setTestCaseName("request_canshu_zhengque --商品信息详情")
        if pid.getResCode() != "000000":
            raise Exception("请求接口失败：message = {:s},resCode = {}".format(body["message"], body["resCode"]))
        return pid

# if __name__ == "__main__":
#     Request().request_zhengchang()