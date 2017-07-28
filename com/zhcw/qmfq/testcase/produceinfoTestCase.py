#基本信息(10040101)

from com.zhcw.qmfq.inerfunc.produceinfoRequest import ProduceInfo
from com.zhcw.qmfq.tools import ResponseLog


class ProduceInfoTC:
    def produceInfo(self):
        pi = ProduceInfo().request_zhengchang("produceInfozhengchang")
        if pi is not None:
            ResponseLog.responseDataLog(pi)
