#-*- coding: UTF-8 -*-
import time,os
import unittest
import HTMLTestRunner
import threading
from framework import getcwd
from framework.email_report import EmailReport
from framework.logger import logger

class runner():
    casedir1 = getcwd.get_cwd()+'//testsuites/ApprBase'
    casedir2 = getcwd.get_cwd() + '//testsuites/ApprControl'
    casedir3 = getcwd.get_cwd() + '//testsuites/ApprSupport'
    casedir4 = getcwd.get_cwd() + '//testsuites/ApprSynthesis'
    #（unittest.defaultTestLoader(): defaultTestLoader()类，通过该类下面的discover()方法可自动更具测试目录start_dir匹配查找测试用例文件（test*.py），
#并将查找到的测试用例组装到测试套件，因此可以直接通过run()方法执行discover）
    discover1 = unittest.defaultTestLoader.discover(casedir1)
    print("ApprBse cases:%s"%discover1)
    discover2 = unittest.defaultTestLoader.discover(casedir2,top_level_dir="testsuites")
    print("ApprControl cases:%s"%discover2)
    discover3 = unittest.defaultTestLoader.discover(casedir3,top_level_dir="testsuites")
    print("ApprSupport cases:%s"%discover3)
    discover4 = unittest.defaultTestLoader.discover(casedir4,top_level_dir="testsuites")
    print("ApprSynthesis cases:%s"%discover4)

    #lastPath = os.path.dirname(os.getcwd())#获取当前路径的上一级
    resultDir = getcwd.get_cwd() + '/test_report/' #报告存放路径
    now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    filename = resultDir + now + "report.html"
    fp = open(filename, 'wb')
    cases=['ApprBase','ApprControl','ApprSupoort','ApprSynthesis']
    def run(self,discover,s):
        runner = HTMLTestRunner.HTMLTestRunner(stream=self.fp,title=str(self.cases[s])+u'测试报告',description=u'用例执行情况：')
        runner.run(discover)
    def muti_run(self):
        t1 = threading.Thread(target=self.run,args=(self.discover1,0,))
        t2 = threading.Thread(target=self.run, args=(self.discover2,1,))
        t3 = threading.Thread(target=self.run,args=(self.discover3,2,))
        t4 = threading.Thread(target=self.run,args=(self.discover4,3,))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t1.join()
        t2.join()
        t3.join()
        t4.join()
        self.fp.close()
if __name__ == '__main__':
    run = runner()
    run.muti_run()
    # email_report = EmailReport()
    # email_report.send_report()
    logger = logger(logger="MutithreadRunner").remove_logs()   #定期清理7天前过期日志截图及报告功能