#计算详情(10040206)
from com.zhcw.qmfq.data.res_data.ResponseBaseData import ResponseBaseData

class JiSuanInfo(ResponseBaseData):

    def setEncashNum(self,encashNum):
        self.encashNum = encashNum
    def getEncashNum(self):
        return self.encashNum

    def setValueA(self,valueA):
        self.valueA = valueA
    def getValueA(self):
        return self.valueA

    def setList(self,list):
        self.list = list
    def getListr(self):
        return self.list

    class List:
        def setCreateTime(self,createTime):
            self.createTime = createTime
        def getCreateTime(self):
            return self.createTime

        def setNum(self,num):
            self.num = num
        def getNum(self):
            return self.num

        def setUserName(self,userName):
            self.userName = userName
        def getUserName(self):
            return self.userName
