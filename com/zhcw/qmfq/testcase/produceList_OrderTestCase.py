from com.zhcw.qmfq.inerfunc.produceList_OrderRequest import ProduceListOrder
from com.zhcw.qmfq.tools import ResponseLog


class ProduceListOrderTC:

    def produceListOrder(self):
        plo = ProduceListOrder().getProduceList("produceList_Order")
        if plo is not None:
            ResponseLog.responseDataLog(plo)
