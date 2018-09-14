#coding utf-8

import unittest

from framework import getcwd
from framework.browser_engine import BrowserEngine
from pageobjects.login_logout.login_logout_page import Login_logout


class Loginout(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        browser=BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):

        cls.driver.quit()

    def test_login(self):

        u'''登录政务系统测试用例,用户名：admin'''

        user_path = getcwd.get_cwd() + '/config/user_info.txt'
        loginpage= Login_logout(self.driver)
        user_file = open(user_path)
        all_values= user_file.readlines()
        values = all_values[0]
        user_file.close()
        username = values.split(',')[0]
        userpasswrod = values.split(',')[1]
        loginpage.login(username,userpasswrod)
        try:
            title = loginpage.get_title()
            self.assertEqual ('网上审批系统',title)
        except Exception as e:
            loginpage.get_windows_img()
            raise e
        '''
        if page_text=="网上审批系统":
            print (u"登录成功")
        else:
            raise NameError(u'网上审批系统')
        '''

    def test_logout(self):
        u'''登出系统用例'''

        logoutpage = Login_logout(self.driver)
        logoutpage.logout()
        title = logoutpage.get_title()
        try:
            self.assertEqual (title,'登录')
        except Exception as e:
            logoutpage.get_windows_img()
            raise e

if __name__ == '__main__':
    unittest.main()