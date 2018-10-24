# _*_coding:utf-8_*_
import logging
import time
import os
import datetime
from framework import getcwd


class logger(object):

    def __init__(self,logger):

        #创建一个logger
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        #创建一个handler,用于写入日志文件
        rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        log_path = getcwd.get_cwd() + '/logs/'
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

    def TimeStampToTime(self, timestamp):
        """格式化时间"""
        timeStruct = time.localtime(timestamp)
        return str(time.strftime('%Y-%m-%d', timeStruct))

    def remove_logs(self):
        """到期删除日志,截图，报告文件"""
        dir_list = ['logs', 'screenshots','test_report']  # 要删除文件的目录名
        for dir in dir_list:
            dirPath = getcwd.get_cwd() + '\\' + dir  # 拼接删除目录完整路径
            file_list = os.listdir(dirPath)  # 返回目录下的文件list
            for i in file_list:
                file_path = os.path.join(dirPath, i)  # 拼接文件的完整路径
                t_list = self.TimeStampToTime(os.path.getctime(file_path)).split('-')
                now_list = self.TimeStampToTime(time.time()).split('-')
                t = datetime.datetime(int(t_list[0]), int(t_list[1]), int(t_list[2]))  # 将时间转换成datetime.datetime 类型
                now = datetime.datetime(int(now_list[0]), int(now_list[1]), int(now_list[2]))
                if (now - t).days > 6 or os.path.getsize(file_path) > 1048576:  # 时间大于6天，大小大于1m删除
                    os.remove(file_path)
                    print("had delete file:%s" % i)
            # if len(file_list) > 4: # 日志，截图和报告超过四条的删除
            #     file_list = file_list[0:-4]
            #     for i in file_list:
            #         file_path = os.path.join(dirPath, i)  # 拼接文件的完整路径
            #         os.remove(file_path)
            #         print("had delete file:%s"%i)

