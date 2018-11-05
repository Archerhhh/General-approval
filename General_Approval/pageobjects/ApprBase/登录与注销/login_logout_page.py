#-*- coding: UTF-8 -*-

import time
from framework.base_page import BasePage
from selenium.webdriver.common.by import By

class Login_logout(BasePage):


    input_user = "id=>j_username"
    input_pwd ="id=>j_password"
    #submit_btn="id=>login" #登录界面的元素定位
    submit_btn = "xpath=>//*[@id='login-tabs-item']/div/div[2]/div/div[1]/div/a[1]"
    wait_el = (By.XPATH,"//*[@id='header']/ul/li[1]")

    logout_btn ="xpath=>//span[contains(text(),'退出')]"  #登出按钮

    '''
    def type_user(self,text):
        self.type(self.input_user,text)

    def type_pwd(self,text):
        self.type(self.input_pwd,text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)
    '''
    #登录页面方法。
    def login(self,username,userpassword):
        self.type(self.input_user,username)
        self.type(self.input_pwd,userpassword)
        #self.find_element(self.submit_btn).submit()
        self.click(self.submit_btn)
        time.sleep(2)
        self.wait_element(self.wait_el)

    #写入一个页面元素定位类，用于登录后验证是否登录成功。
    def get_title(self):
        title = self.get_page_title()
        return title

    def logout(self):
        self.click(self.logout_btn)