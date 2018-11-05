#-*- coding: UTF-8 -*-
import unittest,time
from framework.browser_engine import BrowserEngine
from pageobjects.ApprBase.登录与注销.login_logout_page import Login_logout
from pageobjects.ApprBase.基础配置模块.地区管理.area_page import AreaPage

class Area(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        login = Login_logout(cls.driver)
        login.login("admin","abc123456")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def test_area01(self):
        """增加顶级地区：验证顶级地区的唯一性"""
        area = AreaPage(self.driver)
        area.try_top()
        try:
            message = area.get_message()
            self.assertEqual("只能有一个顶级地区",message)
        except Exception as e:
            area.get_windows_img()
            raise e


    def test_area02(self):
        """不选择顶级地区时，点击“下级地区”按钮"""
        self.driver.refresh()
        time.sleep(2)
        area = AreaPage(self.driver)
        area.try_child()
        try:
            message = area.get_message()
            self.assertEqual("请选择一个地区",message)
        except Exception as e:
            area.get_windows_img()
            raise e


    def test_area03(self):
        """不选择顶级地区时，点击“下级地区”按钮"""
        self.driver.refresh()
        time.sleep(2)
        area = AreaPage(self.driver)
        area.try_edit()
        try:
            message = area.get_message()
            self.assertEqual("请选择一个地区",message)
        except Exception as e:
            area.get_windows_img()
            raise e


    def test_area04(self):
        """不选择顶级地区时，点击“下级地区”按钮"""
        self.driver.refresh()
        time.sleep(2)
        area = AreaPage(self.driver)
        area.try_delete()
        try:
            message = area.get_message()
            self.assertEqual("请选择地区",message)
        except Exception as e:
            area.get_windows_img()
            raise e

    def test_area05(self):
        """新增下级地区"""
        self.driver.refresh()
        time.sleep(2)
        area = AreaPage(self.driver)
        area.add_child("江门市","440700")
        try:
            message = area.get_message()
            self.assertEqual("新增地区成功!",message)
        except Exception as e:
            area.get_windows_img()
            raise e


    def test_area06(self):
        """编辑下级地区"""
        self.driver.refresh()
        time.sleep(2)
        area = AreaPage(self.driver)
        area.edit_child("020-87239712")
        try:
            message = area.get_message()
            self.assertEqual("编辑地区成功!",message)
        except Exception as e:
            area.get_windows_img()
            raise e


    def test_area07(self):
        """删除该下级地区"""
        self.driver.refresh()
        time.sleep(2)
        area = AreaPage(self.driver)
        area.delete_child()
        try:
            message = area.get_message()
            self.assertEqual("删除地区成功!",message)
        except Exception as e:
            area.get_windows_img()
            raise e


