#商品列表(10040201)
from com.zhcw.qmfq.data.res_data.ResponseBaseData import ResponseBaseData


class ProduceListData(ResponseBaseData):

    def setItemList(self,itemList):
        self.itemList = itemList
    def getItemList(self):
        return self.itemList

    def setTotalNum(self,totalNum):
        self.totalNum = totalNum
    def getTotalNum(self):
        return  self.totalNum

    class ItemList ():
        def setIssueId(self,issueId):
            self.issueId = issueId
        def getIssueId(self,issueId):
            return  self.issueId

        def setIssueName(self,issueName):
            self.issueName = issueName
        def getIssueName(self):
            return self.issueName

        def setItemId(self,itemId):
            self.itemId= itemId
        def getItemId(self):
            return self.itemId

        def setItemUrl(self,itemUrl):
            self.itemUrl = itemUrl
        def getItemUrl(self):
            self.itemUrl

        def setItemName(self,itemName):
            self.itemName  = itemName
        def getItemName(self):
            return self.itemName

        def setItemPeoTimes(self,itemPeoTimes):
            self.itemPeoTimes = itemPeoTimes
        def getItemPeoTimes(self):
            return self.itemPeoTimes

        def setItemBought(self,itemBought):
            self.itemBought = itemBought
        def getItemBought(self):
            return self.itemBought

        def setItemRemainTimes(self,itemRemainTimes):
           self.itemRemainTimes = itemRemainTimes
        def getItemRemainTimes(self):
            return self.itemRemainTimes

        def  setUserIssueLimit(self,userIssueLimit):
            self.userIssueLimit = userIssueLimit
        def getUserIssueLimit(self):
            return self.userIssueLimit

        def setEachPartNum(self,eachPartNum):
            self.eachPartNum = eachPartNum
        def getEachPartNum(self):
            return self.eachPartNum