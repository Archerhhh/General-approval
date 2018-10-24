import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.ApprBase.登录与注销.login_logout_page import Login_logout
from pageobjects.ApprBase.基础配置模块.菜单管理.menu_page import MenuPage

class Menu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        login = Login_logout(cls.driver)
        login.login('admin', 'abc123456')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_menu01(self):
        u"""新增顶级节点"""
        menu = MenuPage(self.driver)
        menu.add_top("http://baidu.com")
        try:
            message = menu.get_message()
            self.assertEqual("保存成功！",message)
        except Exception as e:
            menu.get_windows_img()
            raise e


    def test_menu02(self):
        u"""删除菜单"""
        menu = MenuPage(self.driver)
        menu.delete_menu()
        try:
            message = menu.get_confirm()
            self.assertEqual("确认删除此节点？",message)
        except Exception as e:
            menu.get_windows_img()
            raise e