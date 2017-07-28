#2.4.1 领取（选择地址）（实物）(10040401)

from com.zhcw.qmfq.data.res_data.ResponseBaseData import ResponseBaseData

class LingQuInfo_SW(ResponseBaseData):

    def setCall(self,call):
        self.call = call
    def getCal(self):
        return self.call

    def setAccepter(self,accepter):
        self.accepter = accepter
    def getAccepter(self):
        return self.accepter

    def setCreateTime(self,createTime):
        self.createTime = createTime
    def getCreateTime(self):
        return self.createTime

    def setAddress(self,address):
        self.address = address
    def getAddress(self):
        return self.address

    def setexpress(self,express):
        self.express = express
    def getexpress(self):
        return self.express

    def setpressId(self,pressId):
        self.pressId = pressId
    def getpressId(self):
        return self.pressId

    def setsendItemDesc(self,sendItemDesc):
        self.sendItemDesc =sendItemDesc
    def getsendItemDesc(self):
        return self.sendItemDesc

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