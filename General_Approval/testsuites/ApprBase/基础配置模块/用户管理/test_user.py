import unittest,time
import random
from framework.browser_engine import BrowserEngine
from pageobjects.ApprBase.登录与注销.login_logout_page import Login_logout
from pageobjects.ApprBase.基础配置模块.用户管理.user_page import UserPage


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

    code = "damon_" + str(random.randint(1, 1000))

    #@unittest.skip
    def test_user01(self):
        """新增用户"""
        user = UserPage(self.driver)
        user.add_user(self.code,"cheny","chen1995/","chen1995/","测试科")
        try:
            message = user.get_message()
            self.assertEqual("新增用户成功!",message)
        except Exception as e:
            user.get_windows_img()
            raise e

    #@unittest.skip
    def test_user02(self):
        """启用不启用用户"""
        self.driver.refresh()
        time.sleep(2)
        user = UserPage(self.driver)
        user.enable_disable(self.code,"cheny")
        try:
            message = user.get_message()
            self.assertEqual("启用用户成功!",message)
        except Exception as e:
            user.get_windows_img()
            raise e

    #@unittest.skip
    def test_user03(self):
        """编辑用户"""
        self.driver.refresh()
        time.sleep(2)
        user = UserPage(self.driver)
        user.edit_user(self.code,"cheny","87392")
        try:
            message = user.get_message()
            self.assertEqual("编辑用户成功!",message)
        except Exception as e:
            user.get_windows_img()
            raise e


    def test_user04(self):
        """设置用户密码"""
        self.driver.refresh()
        time.sleep(2)
        user = UserPage(self.driver)
        user.change_password(self.code,"cheny","chen1996/","chen1996/")
        try:
            message = user.get_message()
            self.assertEqual("设置密码成功!",message)
        except Exception as e:
            user.get_windows_img()
            raise e
