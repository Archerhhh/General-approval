# coding utf-8
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.ApprBase.登录与注销.login_logout_page import Login_logout
from pageobjects.ApprControl.process_page import ProcessPage


class Process(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        login = Login_logout(cls.driver)
        login.login('ceshi1', 'abc123456!')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01save(self):
        u"""保存办件信息"""
        process = ProcessPage(self.driver)
        process.open_model()
        process.sign_tab()
        process.add_message("damon", "362421199303019322", "13148907967")
        try:
            message = process.get_message()
            self.assertEqual("进入材料审核", message)
        except Exception as e:
            process.get_windows_img()
            raise e

    def test_02upload(self):
        u"""上传材料并填写审核结果"""
        process = ProcessPage(self.driver)
        process.upload_material("合格", "审核通过", "纸质材料收集完毕")
        try:
            message = process.get_alertmessage()
            self.assertEqual("保存成功", message)
        except Exception as e:
            process.get_windows_img()
            raise e

    def test_03approve(self):
        u"""点击进入材料审核"""
        process = ProcessPage(self.driver)
        process.enter_material("合格")
        try:
            message = process.get_message()
            self.assertEqual("进入受理", message)
        except Exception as e:
            process.get_windows_img()
            raise e

    def test_04toshouli(self):
        u"""点击进入受理"""
        process = ProcessPage(self.driver)
        process.enter_shouli()
        try:
            message = process.get_message()
            self.assertEqual("进入承办", message)
        except Exception as e:
            process.get_windows_img()
            raise e

    def test_05shouli(self):
        u"""点击受理"""
        process = ProcessPage(self.driver)
        process.shouli()
        try:
            message = process.get_alertmessage()
            self.assertEqual("受理之后，办件开始倒计时。", message)
        except Exception as e:
            process.get_windows_img()
            raise e

    def test_06tochenban(self):
        u"""点击进入承办"""
        process = ProcessPage(self.driver)
        process.enter_chenban()
        try:
            message = process.get_message()
            self.assertEqual("转入审核", message)
        except Exception as e:
            process.get_windows_img()
            raise e

    def test_07toapproval(self):
        u"""点击保存承办并进入审核"""
        process = ProcessPage(self.driver)
        process.save_chenban()
        try:
            message = process.get_message()
            self.assertEqual("进入批准", message)
        except Exception as e:
            process.get_windows_img()
            raise e

    def test_08took(self):
        u"""点击保存审核并进入批准"""
        process = ProcessPage(self.driver)
        process.save_chenban()
        try:
            message = process.get_message()
            self.assertEqual("办结", message)
        except Exception as e:
            process.get_windows_img()
            raise e

    def test_09tonext(self):
        u"""点击保存批准并进入办结"""
        process = ProcessPage(self.driver)
        process.save_chenban()
        try:
            message = process.get_message()
            self.assertEqual("下一步", message)
        except Exception as e:
            process.get_windows_img()
            raise e

    def test_10tostep(self):
        u"""点击保存审批意见并点击下一步"""
        process = ProcessPage(self.driver)
        process.save_chenban()
        try:
            message = process.get_message()
            self.assertEqual("结束", message)
        except Exception as e:
            process.get_windows_img()
            raise e

    def test_11end(self):
        u"""点击出件并点击结束"""
        process = ProcessPage(self.driver)
        process.end()
        try:
            handles = process.get_allwindows()  # 返回列表类型的数据
            number = len(handles)    # 获取返回的list的长度
            self.assertEqual(1, number)
        except Exception as e:
            process.get_windows_img()
            raise e
        # else:
        #     handle = ''.join(handles)   # 将列表类型转换为字符串类型
        #     self.driver.switch_to_window(handle)
        #     process.get_windows_img()

if __name__ == '__main__':
    unittest.main()
