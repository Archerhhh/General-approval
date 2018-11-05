#-*- coding: UTF-8 -*-
import time
import unittest
import HTMLTestRunner
from framework import getcwd
from framework.email_report import EmailReport
from framework.logger import logger
#from testsuites.ApprBase.登录与注销.test_loginout import Loginout


# 指定测试报告文件
report_path = getcwd.get_cwd() + '/test_report/'
now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))

HtmlFile = report_path + now + "report.html"

    # 加载所有测试套件中的所有测试用例
suite_path = getcwd.get_cwd() + r"\testsuites"
suite = unittest.TestLoader().discover(suite_path)

# suite = unittest.TestSuite()
# suite.addTest(Loginout('test_login'))
# suite.addTest(Loginout('test_logout'))

if __name__ == '__main__':

    with open(HtmlFile, 'wb') as fp:   # 打开测试报告文件，用于写入测试报告
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"政务系统自动化测试报告", description=u"备注：测试报告附件请用chorome打开，否则无法展开详情",verbosity=2)
        runner.run(suite)
    # 调用自动发邮件方法
    email_report = EmailReport()
    email_report.send_report()
    logger = logger(logger="TestRunner").remove_logs()
