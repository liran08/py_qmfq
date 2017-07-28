#订单支付(10040306)
from com.zhcw.qmfq.data.res_data.ResponseBaseData import ResponseBaseData


class OrderPay(ResponseBaseData):
    def setOutTradeId(self,outTradeId):
        self.outTradeId = outTradeId
    def getOutTradeId(self):
        return self.outTradeId

    def setMaAccount(self,maAccount):
        self.maAccount =maAccount
    def getMaAccount(self):
        return self.maAccount

    def setAccount(self,account):
        self.account =account
    def getAccount(self):
        return self.account

    def setIssueId(self,issueId):
        self.issueId =issueId
    def getIssueId(self):
        return self.issueId