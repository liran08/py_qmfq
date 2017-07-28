
import unittest

from com.zhcw.qmfq.testcase.producePayTestCase import ProducePayTC


class TestProducePay(unittest.TestCase):
    def testProducePay(self):
        ProducePayTC().checkProducePay()

    
#suite = unittest.makeSuite(TestProducePay,'test')
# r = unittest.TextTestRunner()
# r.run(suite)