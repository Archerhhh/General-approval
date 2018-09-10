# _*_coding:utf-8_*_
import logging
import os.path
import time
import getcwd

class logger(object):

    def __init__(self,logger):

        #创建一个logger
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        #创建一个handler,用于写入日志文件
        rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        log_path = getcwd.get_cwd()+'/logs/'
        #log_path=os.path.dirname(os.path.dirname(os.getcwd()))+'/logs/'
        # log_path = (os.path.dirname(os.getcwd()) + '/Logs/'
        # log_path = 'D:\PycharmProjects\General Approval'+'/logs/'
        log_name = log_path + rq + '.log'
        fh= logging.FileHandler(log_name,encoding = 'utf-8')
        fh.setLevel(logging.INFO)

        #再创建一个handler，用于输出控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        #定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        #给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger


