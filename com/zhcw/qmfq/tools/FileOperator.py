import os
import configparser
import logging  
import logging.handlers  

class FileOperator:

    def getFileConfigName(self):
        filePath = os.getcwd()         
        fpn = filePath.__add__("//param.conf")
        return  fpn
      
    def writeResultLog(self,mesg):

        # 创建一个logger 
        logger = logging.getLogger('mylogger') 
        logger.setLevel(logging.DEBUG) 
        
        # 创建一个handler，用于写入日志文件 
        fh = logging.FileHandler('result.log','a',encoding = "UTF-8") 
        fh.setLevel(logging.DEBUG) 
 
        fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'  
          
        formatter = logging.Formatter(fmt)   # 实例化formatter  
        fh.setFormatter(formatter)      # 为handler添加formatter  
        logger.addHandler(fh)           # 为logger添加handler

        logger.info(mesg)

        logger.removeHandler(fh)
        fh.close()