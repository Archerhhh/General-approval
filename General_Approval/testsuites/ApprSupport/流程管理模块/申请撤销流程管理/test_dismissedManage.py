#-*- coding: UTF-8 -*-
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.ApprSupport.流程管理模块.延期申请流程管理.delayManage_page import DelayManagePage
from pageobjects.ApprBase.登录与注销.login_logout_page import Login_logout


class delayManage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        login = Login_logout(cls.driver)
        login.login("admin","abc123456")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    #@unittest.skip
    def test_dismissedmanage01(self):
        """新增申请撤销流程"""
        dismiss = DelayManagePage(self.driver)
        dismiss.add_flow("自动化流程","测试科","测试专用流程")
        try:
            message =dismiss.get_message()
            self.assertEqual("新增延期申请流程成功!",message)
        except Exception as e:
            dismiss.get_windows_img()
            raise e

    def test_dismissedmanage02(self):
        """查询流程名称"""
        dismiss = DelayManagePage(self.driver)
        dismiss.query_flow("自动化流程")
        try:
            message =dismiss.get_list()
            self.assertEqual("自动化流程(配置中)",message)
        except Exception as e:
            dismiss.get_windows_img()
            raise e

    def test_dismissedmanage03(self):
        """查询所属单位"""
        dismiss = DelayManagePage(self.driver)
        dismiss.query_danwei()
        try:
            message =dismiss.get_list()
            self.assertEqual("自动化查询流程*",message)
        except Exception as e:
            dismiss.get_windows_img()
            raise e

    def test_dismissedmanage04(self):
        """对申请撤销流程进行编辑：修改流程名称"""
        dismiss = DelayManagePage(self.driver)
        dismiss.edit_step("自动化流程","自动流程")
        try:
            message =dismiss.get_message()
            self.assertEqual("编辑延期申请流程成功!",message)
        except Exception as e:
            dismiss.get_windows_img()
            raise e

    def test_dismissedmanage05(self):
        """复制流程"""
        dismiss = DelayManagePage(self.driver)
        dismiss.copy_flow("自动流程","海珠区延期")
        try:
            message =dismiss.get_list()
            self.assertEqual("自动流程*",message)
        except Exception as e:
            dismiss.get_windows_img()
            raise e

    def test_dismissedmanage06(self):
        """删除流程"""
        dismiss = DelayManagePage(self.driver)
        dismiss.delete_flow("自动流程")
        try:
            message =dismiss.get_message()
            self.assertEqual("删除流程成功！",message)
        except Exception as e:
            dismiss.get_windows_img()
            raise e
