#基本信息(10040101)

from com.zhcw.qmfq.data.res_data.ResponseBaseData import ResponseBaseData

class ProduceInfoData(ResponseBaseData):

    def setItemPeoTimes(self,itemPeoTimes):
        self.itemPeoTimes = itemPeoTimes
    def getItemPeoTimes(self):
        return  self.itemPeoTimes

    def setItemBought(self,itemBought):
        self.itemBought= itemBought
    def getItemBought(self):
        return self.itemBought

    def setItemRemainTimes(self,itemRemainTimes):
        self.itemRemainTimes = itemRemainTimes
    def getItemRemainTimes(self):
        return self.itemRemainTimes

    def setissueId(self,issueId):
        self.issueId = issueId
    def getissueId(self):
        return self.issueId

    def setCurrIssueId(self,currIssueId):
        self.currIssueId = currIssueId
    def getCurrIssueId(self):
        return self.currIssueId

    def setIssueName(self,issueName):
        self.issueName = issueName
    def getIssueName(self):
        return  self.issueName

    def setIssueState(self,issueState):
        self.issueState = issueState
    def getIssueState(self):
        return self.issueState

    def setEndTime(self,endTime):
        self.endTime = endTime
    def getEndTime(self):
        return self.endTime

    def setTtimeDown(self,timeDown):
        self.timeDown = timeDown
    def getTtimeDown(self):
        return self.timeDown

    def setIitemId(self,itemId):
        self.itemId = itemId
    def getIitemId(self):
        return self.itemId

    def setIitemName(self,itemName):
        self.itemName = itemName
    def getIitemName(self):
        return self.itemName

    def setUuserIssueLimit(self,userIssueLimit):
        self.userIssueLimit = userIssueLimit
    def getUuserIssueLimit(self):
        return self.userIssueLimit

