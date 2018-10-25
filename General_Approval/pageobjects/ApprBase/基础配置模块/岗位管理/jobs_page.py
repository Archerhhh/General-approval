import time
from framework.base_page import BasePage
from selenium.webdriver.common.by import By

class JobsPage(BasePage):

    model = "xpath=>//a[@href='/ApprBase/admin/system/role/toListPosition.do']"
    model_frame = "xpath=>//iframe[@src='/ApprBase/admin/system/role/toListPosition.do']"
    add_button = "xpath=>//span[contains(text(),'新增岗位')]"
    add_frame = (By.NAME,'new')
    edit_frame = (By.NAME,"edit")
    unit_frame = (By.NAME,"selectUnit")
    model_name = "id=>roleName"
    choose_unit = "id=>selectUnit"
    unit_name = "id=>unitName"
    query_button = "xpath=>//input[@value='查 询']"
    select_unit = "xpath=>//span[contains(text(),'测试科')]"
    confirm = "xpath=>//input[@value='确定']"
    submit = "id=>sumbitButton"                      #新增岗位页面定位

    def add_jobs(self,name,unit):   #新增岗位
        self.execute_js(self.model)
        self.select_frame(self.find_element(self.model_frame))
        self.click(self.add_button)
        self.wait_goframe(self.add_frame)
        time.sleep(1)
        self.type(self.model_name,name)
        self.click(self.choose_unit)
        self.wait_goframe(self.unit_frame)
        self.type(self.unit_name,unit)
        self.click(self.query_button)
        self.click(self.select_unit)
        self.click(self.confirm)
        self.wait_goframe(self.add_frame)
        self.click(self.submit)
        time.sleep(2)

    alert = "xpath=>//div[@class='messager-body panel-body panel-body-noborder window-body']"
    accept_alert = "xpath=>//span[contains(text(),'确定')]"

    def get_message(self):   #获取各个页面的弹窗，一般通用
        message = self.get_element_text(self.alert)
        self.click(self.accept_alert)
        self.top_windows()
        return message

    def query_name(self,name):   #通过岗位名称进行查询
        self.execute_js(self.model)
        self.select_frame(self.find_element(self.model_frame))
        self.type(self.model_name,name)
        self.click(self.query_button)
        time.sleep(1)

    list1 = "xpath=>//div[@class='datagrid-cell datagrid-cell-c1-roleName']"

    def check_query(self):    #验证查询结果
        message = self.get_element_text(self.list1)
        self.top_windows()
        return message

    diqu = "xpath=>//a[@class='textbox-icon combo-arrow']"
    zhankai="xpath=>//div[@id='_easyui_tree_2']//span[@class='tree-hit tree-collapsed']"
    choose = "xpath=>// span[contains(text(), '潮州市')]"

    def query_diqu(self):   #通过地区进行查询
        self.execute_js(self.model)
        self.select_frame(self.find_element(self.model_frame))
        self.click(self.diqu)
        time.sleep(1)
        self.execute_js(self.zhankai)
        time.sleep(1)
        self.click(self.choose)
        time.sleep(1)
        self.click(self.query_button)
        time.sleep(1)

    suoshudiqu = "xpath=>//td[contains(text(),'所属地区')]//following-sibling::td//a[@class='textbox-icon combo-arrow']"
    choose_1 = "xpath=>//span[contains(text(),'广东省')]"
    danwei = "xpath=>//td[contains(text(),'所属单位')]//following-sibling::td//a[@class='textbox-icon combo-arrow']"
    choose_2 = "xpath=>//span[contains(text(),'测试科')]"

    def query_danwei(self):    #通过单位进行查询
        self.execute_js(self.model)
        self.select_frame(self.find_element(self.model_frame))
        self.click(self.suoshudiqu)
        time.sleep(1)
        self.click(self.choose_1)
        time.sleep(1)
        self.click(self.danwei)
        time.sleep(1)
        self.click(self.choose_2)
        time.sleep(1)
        self.click(self.query_button)
        time.sleep(2)

    select = "xpath=>//input[@name='ck']"
    edit = "xpath=>//span[contains(text(),'编辑岗位')]"
    def edit_jobs(self,name,role):   #编辑岗位
        self.query_name(name)
        self.click(self.select)
        self.click(self.edit)
        time.sleep(1)
        self.wait_goframe(self.edit_frame)
        self.type(self.model_name,role)
        self.click(self.submit)
        time.sleep(1)

    assign_u = "xpath=>//span[contains(text(),'分配用户')]"
    usercode = "id=>userCode"
    peizhi = "xpath=>//span[contains(text(),'配置')]"
    def assign_user(self,name,code):      #分配用户
        self.query_name(name)
        self.click(self.select)
        self.click(self.assign_u)
        time.sleep(1)
        self.wait_goframe(self.edit_frame)
        self.type(self.usercode,code)
        self.click(self.query_button)
        time.sleep(1)
        self.click(self.select)
        self.click(self.peizhi)
        time.sleep(1)

    assign_p = "xpath=>//span[contains(text(),'分配权限')]"
    choose_menu = "xpath=>//span[contains(text(),'文书系统')]//preceding-sibling::span[@class='tree-checkbox tree-checkbox0']"
    def assign_privilege(self,name):       #分配权限
        self.query_name(name)
        self.click(self.select)
        self.click(self.assign_p)
        time.sleep(1)
        self.wait_goframe(self.edit_frame)
        self.click(self.choose_menu)
        self.click(self.confirm)
        time.sleep(1)

    delete_button = "xpath=>//span[contains(text(),'删除岗位')]"
    def delete_job(self,name):   #删除岗位
        self.query_name(name)
        self.click(self.select)
        self.click(self.delete_button)
        time.sleep(1)
        self.click(self.accept_alert)
        time.sleep(1)


