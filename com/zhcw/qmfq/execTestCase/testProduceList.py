
import unittest

from com.zhcw.qmfq.testcase.produceListTestCase import ProduceListTC


class TestProduceList(unittest.TestCase):
    def testProduceList(self):
        ProduceListTC().checkProduceList()

#suite = unittest.makeSuite(TestProduceList,'test')
# r = unittest.TextTestRunner()
# r.run(suite)
    
