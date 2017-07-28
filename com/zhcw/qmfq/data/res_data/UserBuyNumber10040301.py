#认购人次数(10040301)
from com.zhcw.qmfq.data.res_data.ResponseBaseData import ResponseBaseData


class UserBuyNumber(ResponseBaseData):
    def setEncashTotal(self,encashTotal):
        self.encashTotal = encashTotal
    def getEncashTotal(self):
        return self.encashTotal

    def setEncashNum(self,*encashNum):
        self.encashNum = encashNum
    def getEncashNum(self):
        return self.encashNum
