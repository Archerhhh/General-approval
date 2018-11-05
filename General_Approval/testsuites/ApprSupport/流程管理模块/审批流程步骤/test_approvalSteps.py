#-*- coding: UTF-8 -*-
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.ApprSupport.流程管理模块.审批流程步骤.approvalSteps_page import AppStepsPage
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
    def test_approvalteps01(self):
        """新增流程步骤"""
        appstep = AppStepsPage(self.driver)
        appstep.add_step("自动化步骤","测试科","测试专用步骤")
        try:
            message =appstep.get_message()
            self.assertEqual("新增审批流程步骤成功!",message)
        except Exception as e:
            appstep.get_windows_img()
            raise e

    def test_approvalteps02(self):
        """根据步骤名称查询"""
        appstep = AppStepsPage(self.driver)
        appstep.query_step("自动化步骤")
        try:
            message =appstep.get_list()
            self.assertEqual("自动化步骤",message)
        except Exception as e:
            appstep.get_windows_img()
            raise e

    def test_approvalteps03(self):
        """所属单位查询"""
        appstep = AppStepsPage(self.driver)
        appstep.query_danwei()
        try:
            message =appstep.get_list()
            self.assertEqual("自动化查询步骤",message)
        except Exception as e:
            appstep.get_windows_img()
            raise e

    def test_approvalteps04(self):
        """编辑流程步骤"""
        appstep = AppStepsPage(self.driver)
        appstep.edit_step("自动化步骤","自动步骤")
        try:
            message =appstep.get_message()
            self.assertEqual("编辑审批流程步骤成功!",message)
        except Exception as e:
            appstep.get_windows_img()
            raise e

    def test_approvalteps05(self):
        """删除流程步骤"""
        appstep = AppStepsPage(self.driver)
        appstep.delete_step("自动步骤")
        try:
            message =appstep.get_message()
            self.assertEqual("删除审批流程步骤成功！",message)
        except Exception as e:
            appstep.get_windows_img()
            raise e