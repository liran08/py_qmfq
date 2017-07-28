#参与校验(10040305)
from com.zhcw.qmfq.data.res_data.ResponseBaseData import ResponseBaseData


class CanYuCheck(ResponseBaseData):
    def setMaAccount(self,maAccount):
        self.maAccount = maAccount
    def getmaAccount(self):
        return self.maAccount

    def setAccount(self,account):
        self.account = account
    def getAccount(self):
        return self.account

    def setUserId(self,userId):
        self.userId = userId
    def getUserId(self):
        return self.userId

    def setItemId(self,itemId):
        self.itemId =  itemId
    def getItemId(self):
        return self.itemId

    def setIssueName(self,issueName):
        self.issueName = issueName
    def getIssueName(self):
        return self.issueName

    def setTimeNumber(self,timeNumber):
        self.timeNumber = timeNumber
    def getTimeNumber(self):
        return self.timeNumber

    def setRemain(self,remain):
        self.remain = remain
    def getRemain(self):
        return self.remain

    def setcCurIssue(self,curIssue):
        self.curIssue = curIssue
    def getCurIssue(self):
        return self.curIssue

    def setUserIssueLimitRd(self,userIssueLimitRd):
        self.userIssueLimitRd = userIssueLimitRd

    def getUserIssueLimitRd(self):
        return  self.userIssueLimitRd

    def setEachPartNum(self,eachPartNum):
        self.eachPartNum = eachPartNum
    def geteachPartNum(self):
        return self.eachPartNum