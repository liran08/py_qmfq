#用户登陆(10020102)
from com.zhcw.qmfq.data.res_data.ResponseBaseData import ResponseBaseData


class Login(ResponseBaseData):
    def setUserId(self,userId):
        self.userId = userId
    def getUserId(self):
        return self.userId

    def setCookies(self,cookie):
        self.cookie = cookie
    def getCookie(self):
        return self.cookie

