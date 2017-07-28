#获取最新开期(10040205)

from com.zhcw.qmfq.data.res_data.ResponseBaseData import ResponseBaseData


class ZuixinJiexiao(ResponseBaseData):

        def setIssueId(self, issueId):
            self.issueId = issueId
        def getIssueId(self, issueId):
            return self.issueId

        def setIssueName(self, issueName):
            self.issueName = issueName
        def getIssueName(self):
            return self.issueName
