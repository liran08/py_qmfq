
import unittest

from com.zhcw.qmfq.testcase.produceinfoTestCase import ProduceInfoTC


class TestProduceinfo(unittest.TestCase):

    def testProduceinfoShow(self):
        req = ProduceInfoTC()
        req.produceInfo()

#suite = unittest.makeSuite(TestProduceinfo,'test')
# r = unittest.TextTestRunner()
# r.run(suite)