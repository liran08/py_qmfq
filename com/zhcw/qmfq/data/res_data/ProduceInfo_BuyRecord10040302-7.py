#2.3.2 认购记录列表(10040302)
from com.zhcw.qmfq.data.res_data.ResponseBaseData import ResponseBaseData


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
        def setUserName(self,userName ):
            self.userName  = userName
        def getUserName(self):
            return self.userName

        def setUserHeadUrl(self,userHeadUrl):
            self.userHeadUrl =userHeadUrl
        def getUserHeadUrl(self):
            return self.userHeadUrl

        def setAddressIp(self,addressIp):
            self.addressIp = addressIp
        def getAddressIp(self):
            return self.addressIp

        def setOrderId(self,orderId):
            self.orderId  =  orderId
        def getOrderId(self):
            return self.orderId

        def setItemBought(self,itemBought):
            self.itemBought = itemBought
        def getItemBought(self):
            return self.itemBought

        def setCreateTime(self,createTime):
            self.createTime = createTime
        def getCreateTime(self):
            return self.createTime
