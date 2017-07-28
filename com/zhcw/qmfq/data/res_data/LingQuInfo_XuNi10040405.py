#2.4.1 领取（选择地址）（实物）(10040401)

from com.zhcw.qmfq.data.res_data.ResponseBaseData import ResponseBaseData

class LingQuInfo_XN(ResponseBaseData):

    def setCreateTime(self,createTime):
        self.createTime = createTime
    def getCreateTime(self):
        return self.createTime

    def setpullType(self,pullType):
        self.pullType = pullType
    def getpullType(self):
        return self.pullType

    def setrechargeCell(self,rechargeCell):
        self.rechargeCell = rechargeCell
    def getrechargeCell(self):
        return self.rechargeCell

    def setitemName(self,itemName):
        self.itemName = itemName
    def getitemName(self):
        return self.itemName