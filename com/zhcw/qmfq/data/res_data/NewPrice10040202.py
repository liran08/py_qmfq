#最新中奖(10040202)

from com.zhcw.qmfq.data.res_data.ResponseBaseData import ResponseBaseData


class NewPrice(ResponseBaseData):

    def setTimeId(self,timeId):
        self.timeId = timeId
    def getTimeId(self):
        return self.timeId

    def setList(self,list):
        self.list = list
    def getList(self):
        return self.list

    class PriceList:

        def setIssueId(self,issueId):
            self.issueId = issueId
        def getIssueId(self):
            return self.issueId

        def setUserName(self,userName):
            self.userName = userName
        def getUserName(self):
            return self.userName

        def setIssueName(self,issueName):
            self.issueName = issueName
        def getIssueName(self):
            return self.issueName

        def setItemName(self,itemName):
            self.itemName  = itemName
        def getItemName(self):
            return self.itemName

