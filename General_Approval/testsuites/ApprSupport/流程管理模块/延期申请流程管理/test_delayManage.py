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
    def test_delaymanage01(self):
        """新增审批流程"""
        delay = DelayManagePage(self.driver)
        delay.add_flow("自动化流程","测试科","测试专用流程")
        try:
            message =delay.get_message()
            self.assertEqual("新增延期申请流程成功!",message)
        except Exception as e:
            delay.get_windows_img()
            raise e

    def test_delaymanage02(self):
        """通过流程名称查询"""
        delay = DelayManagePage(self.driver)
        delay.query_flow("自动化流程")
        try:
            message =delay.get_list()
            self.assertEqual("自动化流程(配置中)",message)
        except Exception as e:
            delay.get_windows_img()
            raise e

    def test_delaymanage03(self):
        """通过所属单位查询"""
        delay = DelayManagePage(self.driver)
        delay.query_danwei()
        try:
            message =delay.get_list()
            self.assertEqual("自动化查询流程*",message)
        except Exception as e:
            delay.get_windows_img()
            raise e

    def test_delaymanage04(self):
        """编辑审批流程"""
        delay = DelayManagePage(self.driver)
        delay.edit_step("自动化流程","自动流程")
        try:
            message =delay.get_message()
            self.assertEqual("编辑延期申请流程成功!",message)
        except Exception as e:
            delay.get_windows_img()
            raise e

    def test_delaymanage05(self):
        """复制审批流程"""
        delay = DelayManagePage(self.driver)
        delay.copy_flow("自动流程","云浮延期流程")
        try:
            message =delay.get_list()
            self.assertEqual("自动流程*",message)
        except Exception as e:
            delay.get_windows_img()
            raise e

    def test_delaymanage06(self):
        """删除审批流程"""
        delay = DelayManagePage(self.driver)
        delay.delete_flow("自动流程")
        try:
            message =delay.get_message()
            self.assertEqual("删除流程成功！",message)
        except Exception as e:
            delay.get_windows_img()
            raise e