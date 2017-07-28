
from com.zhcw.qmfq.inerfunc.loginRequest import LoginRequest
from com.zhcw.qmfq.inerfunc.personRecordRequest import UserRecorde
from com.zhcw.qmfq.tools import ResponseLog


class UserRecordeTC:
    def userRecorde(self):
        login = LoginRequest().login("loginTC_success")
        if login is not None:
            ur = UserRecorde().request_zhengchang(login.getUserId(),login.getCookie(),"userRecorde")
            if ur is not None:
                ResponseLog.responseDataLog(login, ur)
