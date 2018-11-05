#-*- coding: UTF-8 -*-
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.ApprSupport.流程管理模块.特别程序流程管理.specialManage_page import SpecialManagePage
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
    def test_specialmanage01(self):
        """新增审批流程"""
        special = SpecialManagePage(self.driver)
        special.add_flow("自动化流程","测试科","测试专用流程")
        try:
            message =special.get_message()
            self.assertEqual("新增特别程序流程成功!",message)
        except Exception as e:
            special.get_windows_img()
            raise e

    def test_specialmanage02(self):
        """通过流程名称查询"""
        special = SpecialManagePage(self.driver)
        special.query_flow("自动化流程")
        try:
            message =special.get_list()
            self.assertEqual("自动化流程(配置中)",message)
        except Exception as e:
            special.get_windows_img()
            raise e

    def test_specialmanage03(self):
        """通过所属单位查询"""
        special = SpecialManagePage(self.driver)
        special.query_danwei()
        try:
            message =special.get_list()
            self.assertEqual("自动化查询流程*",message)
        except Exception as e:
            special.get_windows_img()
            raise e

    def test_specialmanage04(self):
        """编辑审批流程"""
        special = SpecialManagePage(self.driver)
        special.edit_step("自动化流程","自动流程")
        try:
            message =special.get_message()
            self.assertEqual("编辑特别程序流程成功!",message)
        except Exception as e:
            special.get_windows_img()
            raise e

    def test_specialmanage05(self):
        """复制审批流程"""
        special = SpecialManagePage(self.driver)
        special.copy_flow("自动流程","云浮特别程序流程")
        try:
            message =special.get_list()
            self.assertEqual("自动流程*",message)
        except Exception as e:
            special.get_windows_img()
            raise e

    def test_specialmanage06(self):
        """删除审批流程"""
        special = SpecialManagePage(self.driver)
        special.delete_flow("自动流程")
        try:
            message =special.get_message()
            self.assertEqual("新增延期申请流程成功!",message)
        except Exception as e:
            special.get_windows_img()
            raise e