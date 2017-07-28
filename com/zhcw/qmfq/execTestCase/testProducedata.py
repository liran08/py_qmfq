#认购人次数(10040301)
import unittest

from com.zhcw.qmfq.testcase.userBuyNumberTestCase import UserBuyNumberTC


class TestUserBuyNumber(unittest.TestCase):
    def testUserBuyNumber(self):
        UserBuyNumberTC().userBuyNum()

#suite = unittest.makeSuite(TestUserBuyNumber,'test')
# r = unittest.TextTestRunner()
# r.run(suite)