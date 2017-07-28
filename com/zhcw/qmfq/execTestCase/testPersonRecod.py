
import unittest

from com.zhcw.qmfq.testcase.personRecordTestCase import UserRecordeTC


class TestUserRecord(unittest.TestCase):
    def testUserRecord(self):
        l = UserRecordeTC()
        l.userRecorde()

#suite = unittest.makeSuite(TestUserRecord,'test')
# r = unittest.TextTestRunner()
# r.run(suite)