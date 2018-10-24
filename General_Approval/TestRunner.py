# coding = utf-8
import time
import unittest
import NewHTMLTestRunner
from framework import getcwd
from framework.email_report import EmailReport
from framework.logger import logger

from testsuites.ApprBase.登录与注销.test_loginout import Loginout
#from testsuites.通用审批.test_process import Process

# 指定测试报告文件
report_path = getcwd.get_cwd() + '/test_report/'
now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))

HtmlFile = report_path + now + "HTMLtemplate.html"

    # 加载所有测试套件中的所有测试用例
# suite_path = getcwd.get_cwd() + r"\testsuites"
# suite = unittest.TestLoader().discover(suite_path)

suite = unittest.TestSuite()
suite.addTest(Loginout('test_login'))
suite.addTest(Loginout('test_logout'))
# suite.addTest(Process('test_01save'))
# suite.addTest(Process('test_02upload'))

if __name__ == '__main__':

    with open(HtmlFile, 'wb') as fp:   # 打开测试报告文件，用于写入测试报告
        runner = NewHTMLTestRunner.HTMLTestRunner(stream=fp, title=u"政务系统自动化测试报告", description=u"用例测试情况",verbosity=2)
        runner.run(suite)
    # 调用自动发邮件方法，不用时注释掉
    #email_report = EmailReport()
    #email_report.send_report()
    logger = logger(logger="TestRunner").remove_logs()
