#获取用户开期限额 (10040102)
from com.zhcw.qmfq.data.res_data.ResponseBaseData import ResponseBaseData


class UserNumberBuyLimitData(ResponseBaseData):

    def serUserIssueLimit(self,userIssueLimit):
        self.userIssueLimit = userIssueLimit
    def getUserIssueLimit(self):
        return self.userIssueLimit

    def setUserIssueLimitRD(self,userIssueLimitRD):
        self.userIssueLimitRD = userIssueLimitRD
    def getUserIssueLimitRD(self):
        return  self.userIssueLimitRD

