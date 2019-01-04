#-*- coding: UTF-8 -*-
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.ApprBase.登录与注销.login_logout_page import Login_logout
from pageobjects.ApprSynthesis.综合窗口收件.SJ_page import SJPage
from pageobjects.ApprSynthesis.综合窗口出件.CJ_page import CJPage

class SJ(unittest.TestCase):
    code = ''
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
        u"""保存个人办件信息"""
        sj= SJPage(self.driver)
        sj.open_sign()
        SJ.code = sj.add_geren()
        #print(SJ.code)
        try:
            message = sj.get_message()
            self.assertEqual("下一步", message)
        except Exception as e:
            sj.get_windows_img()
            raise e

    def test_02upload(self):
        u"""上传材料并填写审核结果"""
        sj= SJPage(self.driver)
        sj.upload_material("纸质材料收集完毕")
        try:
            message = sj.get_alertmessage()
            self.assertEqual("保存成功", message)
        except Exception as e:
            sj.get_windows_img()
            raise e

    def test_03approve(self):
        u"""点击进入材料审核"""
        sj= SJPage(self.driver)
        sj.enter_material("合格")
        try:
            message = sj.get_message()
            self.assertEqual("进入受理", message)
        except Exception as e:
            sj.get_windows_img()
            raise e

    def test_04toshouli(self):
        u"""点击进入受理"""
        sj= SJPage(self.driver)
        sj.enter_shouli()
        try:
            message = sj.get_message()
            self.assertEqual("进入承办", message)
        except Exception as e:
            sj.get_windows_img()
            raise e

    def test_05shouli(self):
        u"""点击受理"""
        sj= SJPage(self.driver)
        sj.shouli()
        try:
            message = sj.get_alertmessage()
            self.assertEqual("受理之后，办件开始倒计时。", message)
        except Exception as e:
            sj.get_windows_img()
            raise e

    def test_06tochenban(self):
        u"""点击进入承办"""
        sj= SJPage(self.driver)
        sj.enter_chenban()
        try:
            message = sj.get_message()
            self.assertEqual("转入审核", message)
        except Exception as e:
            sj.get_windows_img()
            raise e

    def test_07toapproval(self):
        u"""点击保存承办并进入审核"""
        sj= SJPage(self.driver)
        sj.save_chenban()
        try:
            message = sj.get_message()
            self.assertEqual("进入批准", message)
        except Exception as e:
            sj.get_windows_img()
            raise e

    def test_08took(self):
        u"""点击保存审核并进入批准"""
        sj= SJPage(self.driver)
        sj.save_chenban()
        try:
            message = sj.get_message()
            self.assertEqual("办结", message)
        except Exception as e:
            sj.get_windows_img()
            raise e

    def test_09tonext(self):
        u"""点击保存批准并进入办结"""
        sj= SJPage(self.driver)
        sj.save_chenban()
        try:
            message = sj.get_message()
            self.assertEqual("出件", message)
        except Exception as e:
            sj.get_windows_img()
            raise e

    def test_10tostep(self):
        u"""点击保存审批意见并点击下一步"""
        sj= SJPage(self.driver)
        sj.save_chenban()
        try:
            message = sj.get_message()
            self.assertEqual("结束", message)
        except Exception as e:
            sj.get_windows_img()
            raise e


class ZCJ(unittest.TestCase):    #必须先收件再出件，所以为了让收件用例先运行，这里类的命名加个Z。
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)
        login = Login_logout(cls.driver)
        login.login('ceshi1', 'abc123456!')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01qianshou(self):
        u"""进行个人签收"""
        cj= CJPage(self.driver)
        cj.open_qianfa(SJ.code)
        cj.qs()
        try:
            message = cj.get_message1()
            self.assertEqual("出件窗发证", message)
        except Exception as e:
            cj.get_windows_img()
            raise e

    def test_02fazheng(self):
        u"""进行个人发证"""
        cj= CJPage(self.driver)
        cj.fz()
        try:
            message = cj.get_message2()
            self.assertEqual("结束", message)
        except Exception as e:
            cj.get_windows_img()
            raise e

    def test_03end(self):
        u"""结束"""
        cj= CJPage(self.driver)
        cj.end()
        try:
            handles = cj.get_allwindows()  # 返回list类型的数据
            number = len(handles)    # 获取返回的list的长度
            self.assertEqual(1, number)
        except Exception as e:
            cj.get_windows_img()
            raise e

if __name__ == '__main__':
    unittest.main()
