#-*- coding: UTF-8 -*-
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.ApprSupport.流程管理模块.业务流程步骤.businessStep_page import BusiStepPage
from pageobjects.ApprBase.登录与注销.login_logout_page import Login_logout


class BusiStep(unittest.TestCase):
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
    def test_busistep01(self):
        """新增流程步骤"""
        busistep = BusiStepPage(self.driver)
        busistep.add_step("自动化步骤","测试科","测试专用步骤")
        try:
            message =busistep.get_message()
            self.assertEqual("新增业务步骤成功!",message)
        except Exception as e:
            busistep.get_windows_img()
            raise e

    def test_busistep02(self):
        """通过步骤名称查询"""
        busistep = BusiStepPage(self.driver)
        busistep.query_stepname("自动化步骤")
        try:
            message =busistep.get_result()
            self.assertEqual("自动化步骤",message)
        except Exception as e:
            busistep.get_windows_img()
            raise e

    def test_busistep03(self):
        """通过所属地区查询"""
        busistep = BusiStepPage(self.driver)
        busistep.query_diqu()
        try:
            message =busistep.get_result()
            self.assertEqual("自动化查询步骤",message)
        except Exception as e:
            busistep.get_windows_img()
            raise e

    def test_busistep04(self):
        """通过所属单位查询"""
        busistep = BusiStepPage(self.driver)
        busistep.query_danwei()
        try:
            message =busistep.get_result()
            self.assertEqual("自动化查询步骤",message)
        except Exception as e:
            busistep.get_windows_img()
            raise e

    def test_busistep05(self):
        """编辑流程步骤"""
        busistep = BusiStepPage(self.driver)
        busistep.edit_step("自动化步骤","自动步骤")
        try:
            message =busistep.get_message()
            self.assertEqual("编辑业务步骤成功!",message)
        except Exception as e:
            busistep.get_windows_img()
            raise e

    def test_busistep06(self):
        """删除流程步骤"""
        busistep = BusiStepPage(self.driver)
        busistep.delete_step("自动步骤")
        try:
            message =busistep.get_message()
            self.assertEqual("删除业务步骤成功！",message)
        except Exception as e:
            busistep.get_windows_img()
            raise e