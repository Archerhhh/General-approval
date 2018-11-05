#-*- coding: UTF-8 -*-
import unittest,time
import random
from framework.browser_engine import BrowserEngine
from pageobjects.ApprSupport.事项管理模块.事项管理.item_page import ItemPage
from pageobjects.ApprBase.登录与注销.login_logout_page import Login_logout


class Item(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        login = Login_logout(cls.driver)
        login.login("admin","abc123456")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def test_item01(self):
        """新增独立事项"""
        item = ItemPage(self.driver)
        num = random.randint(0, 1000)
        number = str(num)
        item.add_duli("独立事项cyl-1",number,"测试科","5","5")
        try:
            message = item.get_message()
            self.assertEqual("保存事项信息成功",message)
        except Exception as e:
            item.get_windows_img()
            raise e


    def test_item02(self):
        """新增目录事项"""
        self.driver.refresh()
        time.sleep(2)
        item = ItemPage(self.driver)
        num = random.randint(0, 1000)
        number = str(num)
        item.add_mulu("独立事项cyl-1",number,"测试科")
        try:
            message = item.get_message()
            self.assertEqual("保存事项信息成功",message)
        except Exception as e:
            item.get_windows_img()
            raise e

    def test_item03(self):
        """事项编号查询"""
        self.driver.refresh()
        time.sleep(2)
        item = ItemPage(self.driver)
        message = item.query_item("201807131356")
        try:
            self.assertEqual("201807131356",message)
        except Exception as e:
            item.get_windows_img()
            raise e

    def test_item04(self):
        """办理方式查询"""
        self.driver.refresh()
        time.sleep(2)
        item = ItemPage(self.driver)
        message = item.query_way()
        try:
            self.assertEqual("行政罚款",message)
        except Exception as e:
            item.get_windows_img()
            raise e


    def test_item05(self):
        """所属单位查询"""
        self.driver.refresh()
        time.sleep(2)
        item = ItemPage(self.driver)
        message = item.query_danwei()
        try:
            self.assertEqual("自动化单位",message)
        except Exception as e:
            item.get_windows_img()
            raise e
