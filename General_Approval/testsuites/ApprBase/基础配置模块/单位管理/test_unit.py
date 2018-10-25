import unittest,time
from framework.browser_engine import BrowserEngine
from pageobjects.ApprBase.基础配置模块.单位管理.unit_page import UnitPage
from pageobjects.ApprBase.登录与注销.login_logout_page import Login_logout


class Unit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        login = Login_logout(cls.driver)
        login.login("admin","abc123456")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_unit01(self):
        """增加顶级单位,所属地区为广东省，单位名称脚本局"""
        unit = UnitPage(self.driver)
        unit.add_tunit("脚本局")
        try:
            message = unit.get_message()
            self.assertEqual("新增单位成功！",message)
        except Exception as e:
            unit.get_windows_img()
            raise e

    def test_unit02(self):
        """不勾选顶级部门，直接点击增加子部门按钮，是否提示“请选择上级部门"""
        self.driver.refresh()
        time.sleep(2)
        unit = UnitPage(self.driver)
        try:
            message = unit.try_child()
            self.assertEqual("请选择上级单位",message)
        except  Exception as e:
            unit.get_windows_img()
            raise e


    def test_unit03(self):
        """检查“增加处/科室”页面是否正常"""
        self.driver.refresh()
        time.sleep(2)
        unit = UnitPage(self.driver)
        unit.add_keshi("脚本局","科/处室")
        try:
            message = unit.message()
            self.assertEqual("新增单位成功！",message)
        except Exception as e:
            unit.get_windows_img()
            raise e


    def test_unit04(self):
        """新增下级单位"""
        self.driver.refresh()
        time.sleep(2)
        unit = UnitPage(self.driver)
        unit.add_child("脚本局","脚本局子单位")
        try:
            message = unit.message()
            self.assertEqual("新增单位成功！",message)
        except Exception as e:
            unit.get_windows_img()
            raise e


    def test_unit05(self):
        """编辑单位功能：选中民政局，添加一个负责人"""
        self.driver.refresh()
        time.sleep(2)
        unit = UnitPage(self.driver)
        unit.edit_unit("脚本局","020-87239712")
        try:
            message = unit.message()
            self.assertEqual("更新单位成功！",message)
        except Exception as e:
            unit.get_windows_img()
            raise e


    def test_unit06(self):
        """通过地区进行查询"""
        self.driver.refresh()
        time.sleep(2)
        unit = UnitPage(self.driver)
        unit.query_diqu()   #通过地区进行查询
        try:
            message = unit.alert_message()
            self.assertEqual("自动化单位",message)
        except Exception as e:
            unit.get_windows_img()
            raise e

    def test_unit07(self):
        """通过单位进行查询"""
        self.driver.refresh()
        time.sleep(2)
        unit = UnitPage(self.driver)
        unit.query_fuzeren("自动人员")   #通过负责人进行查询
        try:
            message = unit.alert_message()
            self.assertEqual("自动化单位",message)
        except Exception as e:
            unit.get_windows_img()
            raise e


    def test_unit08(self):
        """删除单位功能"""
        self.driver.refresh()
        time.sleep(2)
        unit = UnitPage(self.driver)
        unit.delete_unit("脚本局")
        try:
            message = unit.delete_result()
            self.assertEqual("删除单位成功！",message)
        except Exception as e:
            unit.get_windows_img()
            raise e