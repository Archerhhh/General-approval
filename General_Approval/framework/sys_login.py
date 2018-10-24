from framework import getcwd
from framework.browser_engine import BrowserEngine
from pageobjects.ApprBase.登录与注销.login_logout_page import Login_logout


class Login(object):
    def login(self):
        u'''根据配置文件读取用户登录'''

        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)
        user_path = getcwd.get_cwd() + '/config/user_info.txt'
        loginpage = Login_logout(self.driver)
        user_file = open(user_path)
        all_values = user_file.readlines()
        values = all_values[0]
        user_file.close()
        username = values.split(',')[0]
        userpasswrod = values.split(',')[1]
        loginpage.login(username, userpasswrod)
        return self.driver