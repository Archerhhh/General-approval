import unittest,time
from framework.browser_engine import BrowserEngine
from pageobjects.ApprBase.登录与注销.login_logout_page import Login_logout
from pageobjects.ApprBase.基础配置模块.岗位管理.jobs_page import JobsPage


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
    def test_jobs01(self):
        """新增岗位"""
        jobs = JobsPage(self.driver)
        jobs.add_jobs("自动测试系统","测试科")
        try:
            message = jobs.get_message()
            self.assertEqual("保存成功!",message)
        except Exception as e:
            jobs.get_windows_img()
            raise e


    #@unittest.skip
    def test_jobs02(self):
        """根据岗位名称进行查询"""
        self.driver.refresh()
        time.sleep(2)
        jobs = JobsPage(self.driver)
        jobs.query_name("自动化岗位")
        try:
            message = jobs.check_query()
            self.assertEqual("自动化岗位",message)
        except Exception as e:
            jobs.get_windows_img()
            raise e


    #@unittest.skip
    def test_jobs03(self):
        """根据所属地区进行查询"""
        self.driver.refresh()
        time.sleep(2)
        jobs = JobsPage(self.driver)
        jobs.query_diqu()
        try:
            message = jobs.check_query()
            self.assertEqual("自动化岗位",message)
        except Exception as e:
            jobs.get_windows_img()
            raise e

    #@unittest.skip
    def test_jobs04(self):
        """根据所属单位进行查询"""
        self.driver.refresh()
        time.sleep(2)
        jobs = JobsPage(self.driver)
        jobs.query_danwei()
        try:
            message = jobs.check_query()
            self.assertEqual("自动测试系统",message)
        except Exception as e:
            jobs.get_windows_img()
            raise e

    #@unittest.skip
    def test_jobs05(self):
        "编辑岗位名称"
        self.driver.refresh()
        time.sleep(2)
        jobs = JobsPage(self.driver)
        jobs.edit_jobs("自动测试系统","自动化测试系统")
        try:
            message = jobs.get_message()
            self.assertEqual("保存成功!",message)
        except Exception as e:
            jobs.get_windows_img()
            raise e

    #@unittest.skip
    def test_jobs06(self):
        "分配用户"
        self.driver.refresh()
        time.sleep(2)
        jobs = JobsPage(self.driver)
        jobs.assign_user("自动化测试系统","cyl")
        try:
            message = jobs.get_message()
            self.assertEqual("操作成功!",message)
        except Exception as e:
            jobs.get_windows_img()
            raise e

    #@unittest.skip
    def test_jobs07(self):
        "分配权限"
        self.driver.refresh()
        time.sleep(2)
        jobs = JobsPage(self.driver)
        jobs.assign_privilege("自动化测试系统")
        try:
            message = jobs.get_message()
            self.assertEqual("分配权限成功!",message)
        except Exception as e:
            jobs.get_windows_img()
            raise e


    def test_jobs08(self):
        "删除岗位"
        self.driver.refresh()
        time.sleep(2)
        jobs = JobsPage(self.driver)
        jobs.delete_job("自动化测试系统")
        try:
            message = jobs.get_message()
            self.assertEqual("删除成功!",message)
        except Exception as e:
            jobs.get_windows_img()
            raise e
