#2.3.4 个人疯抢记录(10040304)
from com.zhcw.qmfq.data.res_data.ResponseBaseData import ResponseBaseData
from com.zhcw.qmfq.tools import ResponseDataAnayls
from com.zhcw.qmfq.tools.DataBaseOperator import DBOperator


class UserRecod(ResponseBaseData):

    def setTotalNum(self,totalNum):
        self.totalNum = totalNum
    def getTotalNum(self):
        return self.totalNum

    def setList(self,list):
        self.list = list
    def getList(self):
        return self.list

    class ProduceList:
        def setIssueName(self,issueName ):
            self.issueName  = issueName
        def getIssueName(self):
            return self.issueName

        def setIssueId(self,issueId):
            self.issueId =issueId
        def getIssueId(self):
            return self.issueId

        def setIssueState(self,issueState):
            self.issueState = issueState
        def getIssueState(self):
            return self.issueState

        def setItemId(self,itemId):
            self.itemId  =  itemId
        def getItemId(self):
            return self.itemId

        def setItemName(self,itemName):
            self.itemName = itemName
        def getItemName(self):
            return self.itemName

        def setItemType(self,itemType):
            self.itemType = itemType
        def getItemType(self):
            return self.itemType

        def setItemValue(self,itemValue):
            self.itemValue = itemValue
        def getItemValue(self):
            return self.itemValue

        def setItemUrl(self,itemUrl):
            self.itemUrl = itemUrl
        def getItemUrl(self):
            return self.itemUrl

        def setItemBought(self,itemBought):
            self.itemBought = itemBought
        def getItemBought(self):
            return self.itemBought

        def setWinId(self,winId):
            self.winId = winId
        def getWinId(self):
            return self.winId

        def setWinStatus(self,winStatus):
            self.winStatus = winStatus
        def getWinStatus(self):
            return self.winStatus

        def setShareStatus(self,shareStatus):
            self.shareStatus = shareStatus
        def getShareStatus(self):
            return self.shareStatus

        def setShareDesc(self,shareDesc):
            self.shareDesc = shareDesc
        def getShareDesc(self):
            return self.shareDesc

        def setCreateTime(self,createTime):
            self.createTime = createTime
        def getCreateTime(self):
            return self.createTime

        def setItemValueCD(self,itemValueCD):
            self.itemValueCD = itemValueCD
        def getItemValueCD(self):
            return self.itemValueCD

        def __call__(self, *args, **kwargs):
            return self.responseDataCheck(*args)

        def responseDataCheck(self,userId):
            res = DBOperator().search(userId)
            ur = UserRecod()
            # ur.setTotalNum()
            return ResponseDataAnayls.cmpResponse(self,ur)


        def toString(self):
            s = str(self.getCreateTime()+" " + self.getIssueId()+" " + self.getIssueName()+ " " +self.getIssueState()+" "\
                +self.getItemBought()+" "+self.getItemId()+" "+self.getItemName()+" " + self.getItemType()+" "\
                +self.getItemUrl()+" "+self.getItemValueCD()+" "+self.getShareDesc()+" "+self.getShareStatus()+" "\
                +self.getWinId()+" "+self.getWinStatus())
            return s