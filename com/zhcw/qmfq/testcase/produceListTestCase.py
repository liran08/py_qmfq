#商品列表(10040201)
from com.zhcw.qmfq.inerfunc.produceListRequest import ProduceList
from com.zhcw.qmfq.tools import ResponseLog

class ProduceListTC:

    def checkProduceList(self):
        pld = ProduceList().my_request("produceListzhengchang")
        if pld is not None:
            ResponseLog.responseDataLog(pld)
