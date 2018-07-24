#encoding:utf8
import logging
import getpass
import sys

class MyLog(object):
    def __init__(self):
        self.user = getpass.getuser()
        self.logger = logging.getLogger(self.user)
        self.logger.setLevel(logging.DEBUG)
        #日志文件名
        self.logFile = sys.argv[0][0:-3] + '.log'
        self.formatter = logging.Formatter('%(asctime)-12s %(levelname)-8s %(name)-10s %(message)-12s\r\n')
        #日志显示到控制台并保存到日志文件
        self.logHand = logging.FileHandler(self.logFile,encoding='utf8')
        self.logHand.setFormatter(self.formatter)
        self.logHand.setLevel(logging.DEBUG)

        self.logHandSt = logging.StreamHandler()
        self.logHandSt.setFormatter(self.formatter)
        self.logHandSt.setLevel(logging.DEBUG)

        self.logger.addHandler(self.logHand)
        self.logger.addHandler(self.logHandSt)
    #日志的五个级别，对应以下五个函数
    def debug(self,msg):
        self.logger.debug(msg)

    def info(self,msg):
        self.logger.info(msg)

    def warn(self,msg):
        self.logger.warn(msg)

    def error(self,msg):
        self.logger.error(msg)

    def critical(self,msg):
        self.logger.critical(msg)

if __name__ == '__main__':
    mylog = MyLog()
    mylog.debug(u"I am debug.测试中文")
    mylog.info(u"I am info.测试中文")
    mylog.warn(u"I am warn.测试中文")
    mylog.error(u"I am error.测试中文")
    mylog.critical(u"I am critical.测试中文")
