#-*- coding: UTF-8 -*-
import unittest,time
from framework.browser_engine import BrowserEngine
from pageobjects.ApprBase.登录与注销.login_logout_page import Login_logout
from pageobjects.ApprBase.基础配置模块.用户组管理.usergroup_page import UsergroupPage


class User(unittest.TestCase):
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
    def test_usergroup01(self):
        """新增用户组"""
        usergroup = UsergroupPage(self.driver)
        usergroup.add_group("自动测试系统","测试科")
        try:
            message = usergroup.get_message()
            self.assertEqual("保存成功!",message)
        except Exception as e:
            usergroup.get_windows_img()
            raise e

    #@unittest.skip
    def test_usergroup02(self):
        """根据用户组名称查询"""
        self.driver.refresh()
        time.sleep(2)
        usergroup = UsergroupPage(self.driver)
        usergroup.query_group("自动测试系统")
        try:
            message = usergroup.get_list()
            self.assertEqual("自动测试系统",message)
        except Exception as e:
            usergroup.get_windows_img()
            raise e


    #@unittest.skip
    def test_usergroup03(self):
        """根据所属单位进行查询"""
        self.driver.refresh()
        time.sleep(2)
        usergroup = UsergroupPage(self.driver)
        usergroup.query_danwei()
        try:
            message = usergroup.get_list()
            self.assertEqual("自动测试系统",message)
        except Exception as e:
            usergroup.get_windows_img()
            raise e


    #@unittest.skip
    def test_usergroup04(self):
        """编辑用户组"""
        self.driver.refresh()
        time.sleep(2)
        usergroup = UsergroupPage(self.driver)
        usergroup.edit_group("自动测试系统","自动化测试系统")
        try:
            message = usergroup.get_message()
            self.assertEqual("保存成功!",message)
        except Exception as e:
            usergroup.get_windows_img()
            raise e

    #@unittest.skip
    def test_usergroup05(self):
        """分配用户"""
        self.driver.refresh()
        time.sleep(2)
        usergroup = UsergroupPage(self.driver)
        usergroup.assign_user("自动化测试系统","cyl")
        try:
            message = usergroup.get_listp()
            self.assertEqual("已配置",message)
        except Exception as e:
            usergroup.get_windows_img()
            raise e

    #@unittest.skip
    def test_usergroup06(self):
        """分配权限"""
        self.driver.refresh()
        time.sleep(2)
        usergroup = UsergroupPage(self.driver)
        usergroup.assign_privelege("自动化测试系统")
        try:
            message = usergroup.get_message()
            self.assertEqual("分配权限成功!",message)
        except Exception as e:
            usergroup.get_windows_img()
            raise e


    def test_usergroup07(self):
        """分配权限"""
        self.driver.refresh()
        time.sleep(2)
        usergroup = UsergroupPage(self.driver)
        usergroup.delete_group("自动化测试系统")
        try:
            message = usergroup.get_message()
            self.assertEqual("删除成功!",message)
        except Exception as e:
            usergroup.get_windows_img()
            raise e
