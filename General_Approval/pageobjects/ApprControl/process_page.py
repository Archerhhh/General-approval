#-*- coding: UTF-8 -*-
import time
import os
from framework.base_page import BasePage
from selenium.webdriver.common.by import By
from framework import getcwd

class ProcessPage(BasePage):

    # 选择模块
    model = 'xpath=>//*[@href="/ApprControl/apprItem/toItemDefToAcceptNew.do?isFta=0"]'
    wait_listel =(By.ID,'datagrid-row-r1-2-0')

    #  窗口登记按钮
    frame1 =  "xpath=>//iframe[@src='/ApprControl/apprItem/toItemDefToAcceptNew.do?isFta=0']"
    sign_button = 'xpath=>//*[@id="datagrid-row-r1-2-0"]/td[6]/div/a/font'

    # 填写企业信息
    frame2 ='iframeId'
    wait_frame2 =(By.ID,'iframeId')
    choose_button = 'xpath=>//*[@id="selectCustQY"]'
    wait_frame3 = (By.NAME,'ShowCustInfoList')
    wait_choose = (By.XPATH,'//*[@id="datagrid-row-r1-1-3"]/td[2]/div/input')
    choose_enterprise = 'xpath=>//*[@id="datagrid-row-r1-1-1"]/td[2]/div/input'
    confirm_button = 'xpath=>//*[@id="selectedButton"]'
    enterprise_name = (By.ID,'enterpriseName')

    # 填写申请人信息
    name = 'xpath=>//*[@id="custContactPerson"]'
    id_number = 'xpath=>//*[@id="idCard"]'
    phone_number = 'xpath=>//*[@id="custMobile"]'
    save_button ='id=>doSave'


    def open_model(self):                 #进入模块
        self.execute_js(self.model)
        time.sleep(3)

    def sign_tab(self):       #点击窗口登记并切换到窗口
        self.select_frame(self.find_element(self.frame1))
        #self.wait_element(self.wait_listel)
        time.sleep(6)
        self.click(self.sign_button)
        self.top_windows()
        time.sleep(5)
        self.select_windows()

    def add_message(self,name,id_number,phone_number):    #添加企业办件信息与保存
        self.wait_goframe(self.wait_frame2)
        time.sleep(1)
        self.click(self.choose_button)
        self.top_windows()
        self.wait_goframe(self.wait_frame3)
        self.wait_element(self.wait_choose)
        self.click(self.choose_enterprise)
        self.click(self.confirm_button)
        self.top_windows()
        self.select_frame(self.frame2)
        self.wait_elvalue(self.enterprise_name, '英司康有限公司')
        self.scroll_foot()
        self.type(self.name,name)
        self.type(self.id_number,id_number)
        self.type(self.phone_number,phone_number)
        self.top_windows()
        self.click(self.save_button)
        #self.wait_element(self.alert_message)
        time.sleep(3)

    geren = "xpath=>//input[@value='个人办理']"
    choose_ren = "xpath=>//input[@value='选择申请人']"
    choose_one = "xpath=>//*[@id='datagrid-row-r1-1-0']/td[2]/div/input"
    frame4 = 'ShowCustInfoList'
    def add_geren(self):      #添加个人办件并保存
        self.wait_goframe(self.wait_frame2)
        time.sleep(1)
        self.click(self.geren)
        time.sleep(1)
        self.click(self.choose_ren)
        time.sleep(2)
        self.select_frame(self.frame4)
        self.click(self.choose_one)
        self.click(self.confirm_button)
        time.sleep(2)
        self.top_windows()
        self.click(self.save_button)
        #self.wait_element(self.alert_message)
        time.sleep(3)


    def get_message(self):
        message1 = self.get_element_text(self.next_material)
        return message1

    # 切换到申报材料及进行材料上传
    material = 'id=>nav_sbcl'
    m_iframe = 'iframeId0'
    wait_mframe = (By.NAME,'iframeId0')
    wait_upload =(By.XPATH,'//*[@id="subWrap"]/div[1]/div/div/div/div[1]/a[1]')
    upload_button ='xpath=>//*[@id="subWrap"]/div[1]/div/div/div/div[1]/a[1]'
    wait_uiframe =( By.NAME,'uploadFile')
    choose_file ='xpath=>//*[@id="i_select_files"]/div'
    start = 'xpath=>/html/body/button[1]'
    close = 'xpath=>/html/body/div[6]/div/table/tbody/tr[1]/td/button'
    audit_result = 'id=>auditResult0'
    audit_advise = 'xpath=>//*[@id="datagrid-row-r1-2-0"]/td[10]/div/input'

    #纸质材料审核
    paperstuff = 'xpath=>//*[@id="subWrap"]/div[1]/div/div/div/div[1]/a[2]'
    wait_piframe =(By.NAME, 'addApprFlowWin')
    input = 'id=>contents'
    save_input = 'id=>savePaperStuff'

    def upload_material(self,stuff_ad):
        #上传文件并审核意见
        self.click(self.material)
        self.wait_goframe(self.wait_mframe)
        time.sleep(1)
        # self.wait_element(self.wait_upload)
        # self.click(self.upload_button)
        # self.top_windows()
        # self.wait_goframe(self.wait_uiframe)
        # self.click(self.choose_file)
        # time.sleep(1)
        # os.system('E:\\up.exe')
        # #self.upload("打开",filepath='E:\\upload.txt')
        # time.sleep(2)
        # self.click(self.start)
        # time.sleep(3)             #打开系统窗口，driver无法控制，只能强制等待，根据文件大小，需要更改等待时间。
        # self.top_windows()
        # self.click(self.close)
        # time.sleep(2)
        # self.select_frame(self.m_iframe)
        # self.select_dropdown(self.audit_result,result)
        # self.type(self.audit_advise,advise)
        #纸质材料齐全
        self.click(self.paperstuff)
        self.top_windows()
        self.wait_goframe(self.wait_piframe)
        self.type(self.input,stuff_ad)
        self.click(self.save_input)

    def get_alertmessage(self):    #获取保存弹窗信息
        self.wait_alert()
        alert_message = self.get_alert()
        return alert_message

    #选择审核结果并提交

    select_result = 'id=>attaStatusSelect'
    next_material ='id=>doSend'
    wait_next = (By.ID,'dosend')

    def enter_material(self,text):
        #点击进入材料审核
        self.top_windows()
        self.select_frame(self.m_iframe)
        self.select_dropdown(self.select_result,text)
        self.top_windows()
        self.click(self.next_material)
        time.sleep(3)

        #点击进入受理
    def enter_shouli(self):
        self.click(self.save_button)
        time.sleep(1)
        self.click(self.next_material)
        time.sleep(3)

        #点击受理
    def shouli(self):
        self.click(self.save_button)
        time.sleep(1)

        #点击进入承办
    cancel_button = 'xpath=>//button[text()="跳过"]'
    wait_tiaoguo = (By.XPATH,'//button[text()="跳过"')

    def enter_chenban(self):
        self.click(self.next_material)
        #self.wait_element(self.wait_tiaoguo)
        time.sleep(3)
        # self.click(self.cancel_button)
        # time.sleep(3)

        #点击保存承办并转入审核 #点击保存审核并进入批准，# 点击保存办结并进入下一步，此处共用。
    def save_chenban(self):
        self.click(self.save_button)
        time.sleep(1)
        self.click(self.next_material)
        time.sleep(3)

        # 点击出件并结束
    def end(self):
        self.click(self.save_button)
        time.sleep(1)
        self.click(self.next_material)
        #self.wait_element(self.wait_tiaoguo)
        # time.sleep(1)
        # self.click(self.cancel_button)
        time.sleep(4)

    # 获取全部窗口进行校验是否正常结束流程并关闭窗口
    def get_allwindows(self):
        handles = self.driver.window_handles
        return handles











