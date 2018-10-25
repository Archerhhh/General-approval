import time
from framework.base_page import BasePage
from selenium.webdriver.common.by import By


class UnitPage(BasePage):
    unit_model = 'xpath=>//a[@href="/ApprBase/admin/system/unit/toListUnit.do"]'  #打开模块并切换页面
    frame0 = "xpath=>//iframe[@src='/ApprBase/admin/system/unit/toListUnit.do']"
    add_top = "xpath=>//span[contains(text(),'增加顶级单位')]"
    edit_frame = (By.NAME,'edit')
    diqu = "xpath=>//a[@class='textbox-icon combo-arrow']"   #选择所属地区
    xiala = "xpath=>//div[@id='_easyui_tree_2']//span[@class='tree-hit tree-collapsed']"
    choose = 'xpath=>//span[contains(text(),"广东省")]'
    unit_name = "xpath=>//input[@name='unitName']" #填写地区名称
    tijiao = "id=>sumbitButton"  #提交按钮

    def add_tunit(self,name):   #新增增加顶级单位
        self.execute_js(self.unit_model)
        time.sleep(2)
        self.select_frame(self.find_element(self.frame0))
        self.click(self.add_top)
        time.sleep(1)
        self.top_windows()
        self.wait_goframe(self.edit_frame)
        self.click(self.diqu)
        self.click(self.xiala)
        time.sleep(1)
        self.click(self.choose)
        self.type(self.unit_name,name)
        self.click(self.tijiao)
        time.sleep(2)

    alert = "xpath=>//div[@class='messager-body panel-body panel-body-noborder window-body']"
    close_alert = "xpath=>//span[contains(text(),'确定')]"
    def get_message(self):     #获取提交后的弹窗信息
        message = self.get_element_text(self.alert)
        self.click(self.close_alert)
        self.top_windows()
        return message

    add_xiaji = "xpath=>//span[contains(text(),'增加下级单位')]"
    tanchuang = "xpath=>//div[@class='messager-body panel-body panel-body-noborder window-body']"
    queding = "xpath=>//span[contains(text(),'确定')]"

    def try_child(self):  #点击新增下级单位并关闭弹窗
        self.execute_js(self.unit_model)
        self.select_frame(self.find_element(self.frame0))
        self.click(self.add_xiaji)
        message = self.get_element_text(self.tanchuang)
        self.click(self.queding)
        self.top_windows()
        return message

    unitname = "id=>unitName"
    query = "xpath=>//input[@value='查 询']"
    quan_xuan = "xpath=>//input[@type='checkbox']"
    keshi_chu="xpath=>//span[contains(text(),'增加处/科室')]"
    keshi_name="xpath=>//input[@id='unitName']"
    submit = "id=>sumbitButton"
    def add_keshi(self,unit,keshi):   #新增科室
        self.execute_js(self.unit_model)
        time.sleep(2)
        self.select_frame(self.find_element(self.frame0))
        self.type(self.unitname,unit)
        self.click(self.query)
        time.sleep(1)
        self.click(self.quan_xuan)
        self.click(self.keshi_chu)
        time.sleep(2)
        self.wait_goframe(self.edit_frame)
        self.type(self.keshi_name,keshi)
        self.click(self.submit)
        time.sleep(2)

    alertmessage = "xpath=>//div[@class='messager-body panel-body panel-body-noborder window-body']"
    button = "xpath=>//span[contains(text(),'确定')]"
    def message(self):             #获取新增科室后的信息并关闭窗口
        message = self.get_element_text(self.alertmessage)
        self.click(self.button)
        self.top_windows()
        return message

    def add_child(self,unit,name):    #增加下级菜单 ，获取弹窗消息时共用上面的message()方法
        self.execute_js(self.unit_model)
        time.sleep(2)
        self.select_frame(self.find_element(self.frame0))
        self.type(self.unitname, unit)
        self.click(self.query)
        time.sleep(1)
        self.click(self.quan_xuan)
        self.click(self.add_xiaji)
        time.sleep(2)
        self.wait_goframe(self.edit_frame)
        self.click(self.diqu)
        self.click(self.xiala)
        time.sleep(1)
        self.click(self.choose)
        self.type(self.unit_name,name)
        self.click(self.tijiao)
        time.sleep(2)

    edit = "xpath=>//span[contains(text(),'编辑单位/处（科）室')]"
    number = "id=>unitTel"
    def edit_unit(self,unit,number):#编辑单位
        self.execute_js(self.unit_model)
        time.sleep(2)
        self.select_frame(self.find_element(self.frame0))
        self.type(self.unitname, unit)
        self.click(self.query)
        time.sleep(1)
        self.click(self.quan_xuan)
        self.click(self.edit)
        time.sleep(2)
        self.wait_goframe(self.edit_frame)
        self.type(self.number,number)
        self.click(self.tijiao)
        time.sleep(2)

    suoshudiqu="xpath=>//a[@class='textbox-icon combo-arrow']"
    zhankai = "xpath=>//*[@id='_easyui_tree_2']/span"
    chaozhou = "xpath=>//span[contains(text(),'潮州市')]"
    query_result = "xpath=>//*[contains(text(),'自动化单位')]"

    def query_diqu(self):    #通过地区进行查询
        self.execute_js(self.unit_model)
        time.sleep(2)
        self.select_frame(self.find_element(self.frame0))
        self.click(self.suoshudiqu)
        time.sleep(1)
        self.execute_js(self.zhankai)
        time.sleep(1)
        self.click(self.chaozhou)
        self.click(self.query)
        time.sleep(2)

    def alert_message(self):
        message = self.get_element_text(self.query_result)
        self.top_windows()
        return message

    fuzeren = "xpath=>//input[@id='leaderName']"

    def query_fuzeren(self,name):    #通过负责人进行查询
        self.execute_js(self.unit_model)
        self.select_frame(self.find_element(self.frame0))
        self.type(self.fuzeren,name)
        self.click(self.query)
        time.sleep(2)

    delete = "xpath=>//span[contains(text(),'删除单位')]"
    confirm_delete = "xpath=>//span[contains(text(),'确定')]"

    def delete_unit(self,unit):  #删除单位
        self.execute_js(self.unit_model)
        self.select_frame(self.find_element(self.frame0))
        self.type(self.unitname, unit)
        self.click(self.query)
        time.sleep(1)
        self.click(self.quan_xuan)
        self.click(self.delete)
        self.click(self.confirm_delete)
        time.sleep(2)

    def delete_result(self):
        message = self.get_element_text(self.alertmessage)
        self.click(self.confirm_delete)
        return message



