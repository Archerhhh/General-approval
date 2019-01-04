#-*- coding: UTF-8 -*-
import time
import os
from framework.base_page import BasePage
from selenium.webdriver.common.by import By
from framework import getcwd

class CJPage(BasePage):
    # 选择模块按钮
    menu = 'xpath=>//a[@href="/ApprSynthesis/appr/synthesis/deliver/toDeliverList.do"]'
    frame1=  'xpath=>//iframe[@src="/ApprSynthesis/appr/synthesis/deliver/toDeliverList.do"]'
    waite_code = (By.XPATH,'//input[@id="controlSeq"]')
    query_code = 'xpath=>//input[@id="controlSeq"]'
    query_button = 'xpath=>//input[@value="查 询"]'
    qianfa = 'xpath=>//font[contains(text(),"签收发证")]'

    def open_qianfa(self,code):     # 打开页面并点击签收发证
        self.execute_js(self.menu)
        time.sleep(2)
        self.select_frame(self.find_element(self.frame1))
        #self.wait_element(self.waite_code)
        self.type(self.query_code,code)
        self.click(self.query_button)
        time.sleep(2)
        self.click(self.qianfa)
        time.sleep(3)

    save_button = 'id=>doSave'
    qianshou = 'id=>doCertReceive'
    frame2 =(By.NAME,"editTransferWin")
    select_qs = 'xpath=>//a[contains(text(),"选择移交人")]'
    frame3 = (By.NAME,"userSelect")
    ceshi2 = 'xpath=>//div[contains(text(),"测试2")]'
    queding = 'id=>selectedButton'
    submit = 'id=>sumbitButton'

    def qs(self):  # 出件窗签收
        self.select_windows()
        self.click(self.save_button)
        time.sleep(3)
        self.click(self.qianshou)
        time.sleep(2)
        self.wait_goframe(self.frame2)
        self.click(self.select_qs)
        time.sleep(2)
        self.wait_goframe(self.frame3)
        self.click(self.ceshi2)
        self.click(self.queding)
        time.sleep(1)
        self.wait_goframe(self.frame2)
        self.click(self.submit)
        self.top_windows()
        time.sleep(3)

    def get_message1(self):
        message = self.get_element_text(self.fazheng)
        return message

    fazheng = 'id=>sendCertificate'
    frame4 = (By.NAME,'sendCertificate')
    fafang = 'id=>sign'
    jiesu = 'id=>doSend'
    sure = 'xpath=>//button[contains(text(),"确定")]'

    def fz(self):   # 发证
        self.click(self.fazheng)
        time.sleep(2)
        self.wait_goframe(self.frame4)
        self.click(self.fafang)
        time.sleep(3)

    def get_message2(self):
        message = self.get_element_text(self.jiesu)
        return message

    def end(self):    # 结束
        self.click(self.jiesu)
        time.sleep(1)
        self.click(self.sure)
        time.sleep(3)

    def get_allwindows(self):       # 获取全部窗口进行校验是否正常结束流程并关闭窗口
        handles = self.driver.window_handles
        return handles

