import unittest,time
from framework.browser_engine import BrowserEngine
from pageobjects.ApprBase.登录与注销.login_logout_page import Login_logout
from pageobjects.ApprBase.基础配置模块.职务管理.position_page import PositionPage


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
    def test_position01(self):
        """新增职务"""
        position = PositionPage(self.driver)
        position.add_positon("自动测试系统","测试科")
        try:
            message =position.get_message()
            self.assertEqual("保存成功!",message)
        except Exception as e:
            position.get_windows_img()
            raise e

    #@unittest.skip
    def test_position02(self):
        """通过职务名称进行查询"""
        self.driver.refresh()
        time.sleep(2)
        position = PositionPage(self.driver)
        position.query_position("自动测试系统")
        try:
            message =position.get_list()
            self.assertEqual("自动测试系统",message)
        except Exception as e:
            position.get_windows_img()
            raise e

    #@unittest.skip
    def test_position03(self):
        """通过所属单位进行查询"""
        self.driver.refresh()
        time.sleep(2)
        position = PositionPage(self.driver)
        position.query_danwei()
        try:
            message = position.get_list()
            self.assertEqual("自动测试系统", message)
        except Exception as e:
            position.get_windows_img()
            raise e

    #@unittest.skip
    def test_position04(self):
        """编辑职务"""
        self.driver.refresh()
        time.sleep(2)
        position = PositionPage(self.driver)
        position.edit_position("自动测试系统","自动化测试系统")
        try:
            message = position.get_message()
            self.assertEqual("保存成功!", message)
        except Exception as e:
            position.get_windows_img()
            raise e

    #@unittest.skip
    def test_position05(self):
        """分配用户"""
        self.driver.refresh()
        time.sleep(2)
        position = PositionPage(self.driver)
        position.assign_user("自动化测试系统","cyl")
        try:
            message = position.get_peizhi()
            self.assertEqual("已配置", message)
        except Exception as e:
            position.get_windows_img()
            raise e


    #@unittest.skip
    def test_position06(self):
        """分配权限"""
        self.driver.refresh()
        time.sleep(2)
        position = PositionPage(self.driver)
        position.assign_privelege("自动化测试系统")
        try:
            message = position.get_message()
            self.assertEqual("分配权限成功!", message)
        except Exception as e:
            position.get_windows_img()
            raise e


    def test_position07(self):
        """删除职务"""
        self.driver.refresh()
        time.sleep(2)
        position = PositionPage(self.driver)
        position.delete_position("自动化测试系统")
        try:
            message = position.get_message()
            self.assertEqual("删除成功!", message)
        except Exception as e:
            position.get_windows_img()
            raise e
