#-*- coding: UTF-8 -*-
import time
from framework.base_page import BasePage
from selenium.webdriver.common.by import By

class AreaPage(BasePage):

    diqu = "xpath=>//a[@href='/ApprBase/admin/system/area/toListArea.do']"
    diqu_frame = "xpath=>//iframe[@src='/ApprBase/admin/system/area/toListArea.do']"
    top_area = "xpath=>//span[contains(text(),'添加顶级地区')]"
    alert_message = "xpath=>//div[@class='messager-body panel-body panel-body-noborder window-body']"
    confirm_button = "xpath=>//span[contains(text(),'确定')]"

    def try_top(self):  #新增顶级地区
        self.execute_js(self.diqu)
        self.select_frame(self.find_element(self.diqu_frame))
        self.click(self.top_area)
        time.sleep(1)

    def get_message(self):   #获取弹窗
        message = self.get_element_text(self.alert_message)
        self.click(self.confirm_button)
        return message

    child_area = "xpath=>//span[contains(text(),'增加下属地区')]"

    def try_child(self):  #不选择顶级地区时新增下级地区
        self.execute_js(self.diqu)
        self.select_frame(self.find_element(self.diqu_frame))
        self.click(self.child_area)
        time.sleep(1)

    edit_area = "xpath=>//span[contains(text(),'编辑地区')]"

    def try_edit(self):   #不选择地区时编辑地区
        self.execute_js(self.diqu)
        self.select_frame(self.find_element(self.diqu_frame))
        self.click(self.child_area)
        time.sleep(1)

    delete_area = "xpath=>//span[contains(text(),'删除地区')]"

    def try_delete(self):   #不选择地区时删除地区
        self.execute_js(self.diqu)
        self.select_frame(self.find_element(self.diqu_frame))
        self.click(self.delete_area)
        time.sleep(1)

    top_select = 'xpath=>//span[contains(text(),"广东省")]'
    edit_frame = (By.NAME,'edit')
    area_name = "xpath=>//input[@name='areaName']"
    code_name = "xpath=>//input[@name='jcAreaSeq']"
    area_grad = "xpath=>//td[contains(text(),'区域等级')]/following-sibling::td//a[@class='textbox-icon combo-arrow']"
    choose_city = "xpath=>//div[contains(text(),'地市级')]"
    submit = "id=>sumbitButton"

    #新增下级地区
    def add_child(self,name,code):
        self.execute_js(self.diqu)
        self.select_frame(self.find_element(self.diqu_frame))
        self.click(self.top_select)
        self.click(self.child_area)
        self.top_windows()
        self.wait_goframe(self.edit_frame)
        self.type(self.area_name,name)
        self.type(self.code_name,code)
        self.click(self.area_grad)
        self.click(self.choose_city)
        self.click(self.submit)
        time.sleep(2)

    top_list = "xpath=>//tr[@id='datagrid-row-r1-2-1']//td[@field='areaName']//span"
    jiangmen = "xpath=>//span[contains(text(),'江门市')]"
    phone = "xpath=>//input[@name= 'monitorPhone']"

    #编辑下级地区信息

    def edit_child(self,number):
        self.execute_js(self.diqu)
        self.select_frame(self.find_element(self.diqu_frame))
        self.click(self.top_list)
        time.sleep(1)
        self.click(self.jiangmen)
        self.click(self.edit_area)
        time.sleep(2)
        self.wait_goframe(self.edit_frame)
        self.type(self.phone,number)
        self.click(self.submit)
        time.sleep(2)

    #删除地区

    def delete_child(self):
        self.execute_js(self.diqu)
        self.select_frame(self.find_element(self.diqu_frame))
        self.click(self.top_list)
        time.sleep(1)
        self.click(self.jiangmen)
        self.click(self.delete_area)
        self.click(self.confirm_button)
        time.sleep(2)



