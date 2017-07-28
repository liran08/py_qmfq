#获取开期状态(10040204)

from com.zhcw.qmfq.data.res_data.ResponseBaseData import ResponseBaseData


class QiCiStatus(ResponseBaseData):

    def setIssueState(self,issueState):
        self.issueState = issueState
    def getIssueState(self):
        return self.issueState

    def setItemPeoTimes(self,itemPeoTimes):
        self.itemPeoTimes = itemPeoTimes
    def getItemPeoTimes(self):
         return self.itemPeoTimes

    def setItemBought(self,itemBought):
        self.itemBought = itemBought
    def getItemBought(self):
        return self.itemBought