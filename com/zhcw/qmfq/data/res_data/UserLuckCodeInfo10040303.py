#2.3.3 认购记录明细(10040303)
from com.zhcw.qmfq.data.res_data.ResponseBaseData import ResponseBaseData


class UserLuckCodeInfo(ResponseBaseData):
    def setLuckCode(self,*luckCode):
        self.luckCode = luckCode
    def getLuckCode(self):
        return self.luckCode
