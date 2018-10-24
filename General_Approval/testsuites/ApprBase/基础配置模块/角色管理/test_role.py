import unittest,time
from framework.browser_engine import BrowserEngine
from pageobjects.ApprBase.登录与注销.login_logout_page import Login_logout
from pageobjects.ApprBase.基础配置模块.角色管理.role_page import RolePage


class Jobs(unittest.TestCase):
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
    def test_role01(self):
        """新增角色"""
        role = RolePage(self.driver)
        role.add_role("自动测试系统","测试科")
        try:
            message = role.get_message()
            self.assertEqual("保存成功!",message)
        except Exception as e:
            role.get_windows_img()
            raise e

    #@unittest.skip
    def test_role02(self):
        """通过角色名称查询"""
        self.driver.refresh()
        time.sleep(2)
        role = RolePage(self.driver)
        role.query_role("自动测试系统")
        try:
            name = role.get_name()
            self.assertEqual("自动测试系统",name)
        except Exception as e:
            role.get_windows_img()
            raise e

    #@unittest.skip
    def test_role03(self):
        """通过所属单位查询"""
        self.driver.refresh()
        time.sleep(2)
        role = RolePage(self.driver)
        role.query_unit()
        try:
            name = role.get_name()
            self.assertEqual("自动测试系统",name)
        except Exception as e:
            role.get_windows_img()
            raise e

    #@unittest.skip
    def test_role04(self):
        """编辑角色名称"""
        self.driver.refresh()
        time.sleep(2)
        role = RolePage(self.driver)
        role.edit_role("自动测试系统","自动化测试系统")
        try:
            message = role.get_message()
            self.assertEqual("保存成功!",message)
        except Exception as e:
            role.get_windows_img()
            raise e

    #@unittest.skip
    def test_role05(self):
        """分配用户"""
        self.driver.refresh()
        time.sleep(2)
        role = RolePage(self.driver)
        role.assign_user("自动化测试系统","cyl")
        try:
            message = role.peizhi_message()
            self.assertEqual("已配置",message)
        except Exception as e:
            role.get_windows_img()
            raise e

    #@unittest.skip
    def test_role06(self):
        """分配权限"""
        self.driver.refresh()
        time.sleep(2)
        role = RolePage(self.driver)
        role.assign_privelege("自动化测试系统")
        try:
            message = role.get_message()
            self.assertEqual("分配权限成功!",message)
        except Exception as e:
            role.get_windows_img()
            raise e


    def test_role07(self):
        """删除角色"""
        self.driver.refresh()
        time.sleep(2)
        role = RolePage(self.driver)
        role.delete_role("自动化测试系统")
        try:
            message = role.get_message()
            self.assertEqual("删除成功!",message)
        except Exception as e:
            role.get_windows_img()
            raise e
