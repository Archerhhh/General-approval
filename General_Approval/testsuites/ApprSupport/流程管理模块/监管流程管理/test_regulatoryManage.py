import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.ApprSupport.流程管理模块.监管流程管理.regulatoryManage_page import regulatoryManagepage
from pageobjects.ApprBase.登录与注销.login_logout_page import Login_logout


class RegulaManage(unittest.TestCase):
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
    def test_regulamanage01(self):
        """新增监管流程"""
        regula = regulatoryManagepage(self.driver)
        regula.add_flow("自动化流程","测试科","测试专用流程")
        try:
            message =regula.get_message()
            self.assertEqual("新增监管流程成功!",message)
        except Exception as e:
            regula.get_windows_img()
            raise e

    def test_regulamanage02(self):
        """查询流程名称"""
        regula = regulatoryManagepage(self.driver)
        regula.query_flow("自动化流程")
        try:
            message =regula.get_list()
            self.assertEqual("自动化流程(配置中)",message)
        except Exception as e:
            regula.get_windows_img()
            raise e

    def test_regulamanage03(self):
        """查询所属单位"""
        regula = regulatoryManagepage(self.driver)
        regula.query_danwei()
        try:
            message =regula.get_list()
            self.assertEqual("自动化查询流程*",message)
        except Exception as e:
            regula.get_windows_img()
            raise e

    def test_regulamanage04(self):
        """编辑监管流程"""
        regula = regulatoryManagepage(self.driver)
        regula.edit_step("自动化流程","自动流程")
        try:
            message =regula.get_message()
            self.assertEqual("编辑监管流程成功!",message)
        except Exception as e:
            regula.get_windows_img()
            raise e

    def test_regulamanage05(self):
        """复制流程"""
        regula = regulatoryManagepage(self.driver)
        regula.copy_flow("自动流程","自动化查询流程")
        try:
            message =regula.get_list()
            self.assertEqual("自动流程*",message)
        except Exception as e:
            regula.get_windows_img()
            raise e

    def test_regulamanage06(self):
        """删除流程"""
        regula = regulatoryManagepage(self.driver)
        regula.delete_flow("自动流程")
        try:
            message =regula.get_message()
            self.assertEqual("删除流程成功！",message)
        except Exception as e:
            regula.get_windows_img()
            raise e
