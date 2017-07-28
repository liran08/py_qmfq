#订单支付(10040306)
from com.zhcw.qmfq.inerfunc.loginRequest import LoginRequest
from com.zhcw.qmfq.inerfunc.produceList_OrderRequest import ProduceListOrder
from com.zhcw.qmfq.inerfunc.producePayRequest import ProducePay
from com.zhcw.qmfq.tools import ResponseLog


class ProducePayTC:
    def checkProducePay(self):
        login = LoginRequest().login("loginTC_success")
        plo = ProduceListOrder().getProduceList("produceList_Order")
        if login is not  None and plo is not None:
            itemList = plo.getItemList()
            item = itemList[0]
            pp =ProducePay().request_zhengchang(item,"producePayzhengchangzhifu",login.getUserId(),login.getCookie())
            if pp is not None:
                ResponseLog.responseDataLog(login, plo, pp)

