#认购人次数(10040301)
from com.zhcw.qmfq.inerfunc.loginRequest import LoginRequest
from com.zhcw.qmfq.inerfunc.userBuyNumberRequest import UserBuyNumRequest
from com.zhcw.qmfq.tools import ResponseLog

class UserBuyNumberTC:
    def userBuyNum(self):
        login = LoginRequest().login("loginTC_success")
        if login is not None:
            userNum = UserBuyNumRequest().my_request(login.getUserId(),"bugNumber",login.getCookie())
            if userNum is not None:
                ResponseLog.responseDataLog(login, userNum)
