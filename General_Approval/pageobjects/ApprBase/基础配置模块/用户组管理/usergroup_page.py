#-*- coding: UTF-8 -*-
import time
from framework.base_page import BasePage
from selenium.webdriver.common.by import By

class UsergroupPage(BasePage):

    model = "xpath=>//a[@href='/ApprBase/admin/system/role/toListUserGroup.do']"
    frame0 = "xpath=>//iframe[@src='/ApprBase/admin/system/role/toListUserGroup.do']"
    add_frame = (By.NAME,"new")
    edit_frame = (By.NAME,"edit")
    unit_frame = (By.NAME,"selectUnit")   #进入菜单页面及所有iframe

    add_button = "xpath=>//span[contains(text(),'新增用户组')]"
    group_name = "id=>roleName"
    select_unit = "id=>selectUnit"
    query_unit = "id=>unitName"
    query_button = "xpath=>//input[@value='查 询']"
    select_ceshi = "xpath=>//span[contains(text(),'测试科')]"
    confirm = "xpath=>//input[@value='确定']"
    submit = "id=>sumbitButton"     #添加用户组页面

    def add_group(self,name,unit):   #新增用户组
        self.execute_js(self.model)
        self.select_frame(self.find_element(self.frame0))
        time.sleep(1)
        self.click(self.add_button)
        time.sleep(1)
        self.wait_goframe(self.add_frame)
        self.type(self.group_name,name)
        self.click(self.select_unit)
        time.sleep(1)
        self.wait_goframe(self.unit_frame)
        self.type(self.query_unit,unit)
        self.click(self.query_button)
        time.sleep(1)
        self.click(self.select_ceshi)
        self.click(self.confirm)
        time.sleep(1)
        self.wait_goframe(self.add_frame)
        self.click(self.submit)
        time.sleep(2)

    alert = "xpath=>//div[@class='messager-body panel-body panel-body-noborder window-body']"
    confirm_alert = "xpath=>//span[contains(text(),'确定')]"

    def get_message(self):   #获取弹窗信息后并刷新菜单,一般通用
        message = self.get_element_text(self.alert)
        self.click(self.confirm_alert)
        self.top_windows()
        return message

    def query_group(self,group):   #用户组查询
        self.execute_js(self.model)
        self.select_frame(self.find_element(self.frame0))
        time.sleep(1)
        self.type(self.group_name,group)
        self.click(self.query_button)
        time.sleep(2)

    diyi = "xpath=>//div[@class='datagrid-cell datagrid-cell-c1-roleName']"
    def get_list(self):                 #查询列表数据
        message = self.get_element_text(self.diyi)
        self.top_windows()
        return message

    diqu = "xpath=>//td[contains(text(),'所属地区')]//following-sibling::td//a[@class='textbox-icon combo-arrow']"
    choosediqu = "xpath=>//span[contains(text(),'广东省')]"
    danwei = "xpath=>//td[contains(text(),'所属单位')]//following-sibling::td//a[@class='textbox-icon combo-arrow']"
    choosedanwei = "xpath=>//span[contains(text(),'测试科')]"

    def query_danwei(self):   #通过所属单位查询
        self.execute_js(self.model)
        self.select_frame(self.find_element(self.frame0))
        time.sleep(2)
        self.click(self.diqu)
        time.sleep(1)
        self.click(self.choosediqu)
        self.click(self.danwei)
        time.sleep(1)
        self.click(self.choosedanwei)
        time.sleep(1)
        self.click(self.query_button)
        time.sleep(2)

    choose = "xpath=>//input[@name='ck']"
    edit_button = "xpath=>//span[contains(text(),'编辑用户组')]"
    def edit_group(self,group,new):   #编辑用户组
        self.query_group(group)
        self.click(self.choose)
        self.click(self.edit_button)
        self.wait_goframe(self.edit_frame)
        self.type(self.group_name,new)
        self.click(self.submit)
        time.sleep(2)

    assign_button = "xpath=>//span[contains(text(),'分配用户')]"
    user = "id=>userCode"
    peizhi = "xpath=>//span[contains(text(),'配置')]"
    list_p = "xpath=>//tr[@id='datagrid-row-r2-2-0']//div[@class='datagrid-cell datagrid-cell-c2-userRole']"
    def assign_user(self,group,code):     #分配用户
        self.query_group(group)
        self.click(self.choose)
        self.click(self.assign_button)
        time.sleep(1)
        self.wait_goframe(self.edit_frame)
        self.type(self.user,code)
        self.click(self.query_button)
        time.sleep(1)
        self.click(self.choose)
        self.click(self.peizhi)
        time.sleep(1)
        self.click(self.confirm_alert)
        time.sleep(2)

    close = "id=>closeButton"
    def get_listp(self):     #获取分配用户的状态。
        message = self.get_element_text(self.list_p)
        self.click(self.close)
        self.top_windows()
        return message

    assign_p = "xpath=>//span[contains(text(),'分配权限')]"
    tab1 = 'xpath=>//div[text()="审批系统"]'
    tab2 = 'xpath=>//span[text()="工作台"]/../span[3]'
    #system = "xpath=>//span[contains(text(),'文书系统')]//preceding-sibling::span[@class='tree-checkbox tree-checkbox0']"

    def assign_privelege(self,group):
        self.query_group(group)
        self.click(self.choose)
        self.click(self.assign_p)
        time.sleep(1)
        self.wait_goframe(self.edit_frame)
        self.click(self.tab1)
        time.sleep(1)
        self.click(self.tab2)
        self.click(self.confirm)
        time.sleep(1)

    delete_button = "xpath=>//span[contains(text(),'删除用户组')]"

    def delete_group(self,group):
        self.query_group(group)
        self.click(self.choose)
        self.click(self.delete_button)
        time.sleep(1)
        self.click(self.confirm_alert)
        time.sleep(2)
