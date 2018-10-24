import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.ApprSupport.流程管理模块.业务流程管理.businessmanage_page import BusinessPage
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
    def test_business01(self):
        """新增流程步骤"""
        business = BusinessPage(self.driver)
        business.add_flow("自动化流程","测试科","测试专用流程")
        try:
            message =business.get_message()
            self.assertEqual("新增业务流程成功!",message)
        except Exception as e:
            business.get_windows_img()
            raise e

    #@unittest.skip
    def test_business02(self):
        """通过流程名称进行查询"""
        business = BusinessPage(self.driver)
        business.query_name("自动化流程")
        try:
            message =business.get_result()
            self.assertEqual("自动化流程(配置中)",message)
        except Exception as e:
            business.get_windows_img()
            raise e

    #@unittest.skip
    def test_business03(self):
        """通过所属单位进行查询"""
        business = BusinessPage(self.driver)
        business.query_danwei()
        try:
            message =business.get_result()
            self.assertEqual("自动化查询流程*",message)
        except Exception as e:
            business.get_windows_img()
            raise e

    #@unittest.skip
    def test_business04(self):
        """编辑流程"""
        business = BusinessPage(self.driver)
        business.edit_flow("自动化流程","自动流程")
        try:
            message =business.get_message()
            self.assertEqual("编辑业务流程成功!",message)
        except Exception as e:
            business.get_windows_img()
            raise e

    #@unittest.skip
    def test_business05(self):
        """复制流程"""
        business = BusinessPage(self.driver)
        business.copy_flow("自动流程","跨层级已办流程")
        try:
            message =business.get_result()
            self.assertEqual("自动流程*",message)
        except Exception as e:
            business.get_windows_img()
            raise e

    def test_business06(self):
        """删除流程"""
        business = BusinessPage(self.driver)
        business.delete_flow("自动流程")
        try:
            message =business.get_message()
            self.assertEqual("删除流程成功！",message)
        except Exception as e:
            business.get_windows_img()
            raise e