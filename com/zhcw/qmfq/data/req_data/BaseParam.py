
class BaseParam :
    
    def setSrc(self,src):
        self.src=src
    
    def getSrc(self):
        return self.src
    
    def setBodyParam(self,param):
        self.paramValue=param
    
    def getBodyParam(self):
        return self.paramValue
    
    def setreqType(self,reqtype):
        self.reqtype=reqtype
    
    def getreqType(self):
        return self.reqtype
    
    def settransactionType(self,transactionType):
        self.transactionType = transactionType
    
    def gettransactionType(self):
        return self.transactionType
    
    def toString(self):
        print()