# 往期揭晓/最新揭晓(10040203)

from com.zhcw.qmfq.data.res_data.ResponseBaseData import ResponseBaseData


class ZuixinJiexiao(ResponseBaseData):

    def serIssueList(self, issueList):
        self.issueList = issueList

    def getIssueList(self):
        return self.issueList

    def setTotalNum(self, totalNum):
        self.totalNum = totalNum

    def getTotalNum(self):
        return self.totalNum

    class IssueList():
        def setIssueId(self, issueId):
            self.issueId = issueId
        def getIssueId(self, issueId):
            return self.issueId

        def setIssueName(self, issueName):
            self.issueName = issueName
        def getIssueName(self):
            return self.issueName

        def setStatus(self, status):
            self.status = status
        def getStatus(self):
            return self.status

        def setItemUrl(self, itemUrl):
            self.itemUrl = itemUrl
        def getItemUrl(self):
            self.itemUrl

        def setItemName(self, itemName):
            self.itemName = itemName
        def getItemName(self):
            return self.itemName

        def setTimeDown(self, timeDown):
            self.timeDown = timeDown
        def getTimeDown(self):
            return self.timeDown

        def setItemBought(self, itemBought):
            self.itemBought = itemBought
        def getItemBought(self):
            return self.itemBought

        def setEndTime(self, endTime):
            self.itemRemainTimes = endTime
        def getEndTime(self):
            return self.endTime

        def setUserName(self, userName):
            self.userIssueLimit = userName
        def getUserName(self):
            return self.userName

        def setEachPartNum(self, eachPartNum):
            self.eachPartNum = eachPartNum
        def getEachPartNum(self):
            return self.eachPartNum

        def setImgUrl(self,imgUrl):
            self.imgUrl = imgUrl
        def getImgUrl(self):
            return self.imgUrl
