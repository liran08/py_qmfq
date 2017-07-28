from com.zhcw.qmfq.inerfunc.loginRequest import LoginRequest
from com.zhcw.qmfq.tools import ResponseLog


class LoginTestCase:
    def loginTC_success(self):
        login = LoginRequest().login("loginTC_success")
        if login is not None:
            ResponseLog.responseDataLog(login)
