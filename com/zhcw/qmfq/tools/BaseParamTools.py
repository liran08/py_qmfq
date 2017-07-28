import configparser

from com.zhcw.qmfq.data.req_data import BaseParam


class BaseParamTools:
    
    @classmethod
    def getParam(cls,fpn,name):
        # print(fpn)
        # print(name)
        bp = BaseParam.BaseParam()
        cp =configparser.ConfigParser()
        cp.read(fpn,encoding='utf-8')
        if cp.has_section(name):
            bp.setreqType(cp.get(name,"reqtype"))
            bp.setSrc(cp.get(name,"src"))
            bp.setBodyParam(cp.get(name,"info"))
            bp.settransactionType(cp.get(name,"transactionType"))
            return bp
        else:
            return  None