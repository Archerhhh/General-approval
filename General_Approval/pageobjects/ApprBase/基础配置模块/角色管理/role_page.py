import time
from framework.base_page import BasePage
from selenium.webdriver.common.by import By

class RolePage(BasePage):

    model = "xpath=>//a[@href='/ApprBase/admin/system/role/toListRole.do']"
    frame0 = "xpath=>//iframe[@src='/ApprBase/admin/system/role/toListRole.do']"
    add_button = "xpath=>//span[contains(text(),'新增角色')]"
    add_frame = (By.NAME,'new')
    role = "id=>roleName"
    selectunit = "id=>selectUnit"
    select_iframe = (By.NAME,'selectUnit')
    unit = "id=>unitName"
    query_button = "xpath=>//input[@value='查 询']"
    choose_unit = "xpath=>//span[contains(text(),'测试科')]"
    confirm = "xpath=>//input[@value='确定']"
    submit = "id=>sumbitButton"        #从进入菜单到新增角色所有按钮

    alert = "xpath=>//div[@class='messager-body panel-body panel-body-noborder window-body']"
    close_alert = "xpath=>//span[contains(text(),'确定')]"    #弹窗相关按钮

    def add_role(self,name,unit):        #新增角色
        self.execute_js(self.model)
        time.sleep(2)
        self.select_frame(self.find_element(self.frame0))
        self.click(self.add_button)
        time.sleep(1)
        self.wait_goframe(self.add_frame)
        self.type(self.role,name)
        self.click(self.selectunit)
        time.sleep(1)
        self.wait_goframe(self.select_iframe)
        self.type(self.unit,unit)
        self.click(self.query_button)
        time.sleep(1)
        self.click(self.choose_unit)
        self.click(self.confirm)
        time.sleep(1)
        self.wait_goframe(self.add_frame)
        self.click(self.submit)
        time.sleep(2)

    def get_message(self):     #获取弹窗信息并关闭弹窗，一般多处调用。
        message = self.get_element_text(self.alert)
        self.click(self.close_alert)
        self.top_windows()
        return message

    name_01 = "xpath=>//div[@class='datagrid-cell datagrid-cell-c1-roleName']"
    def query_role(self,name):   #通过角色名称进行查询
        self.execute_js(self.model)
        time.sleep(2)
        self.select_frame(self.find_element(self.frame0))
        self.type(self.role,name)
        self.click(self.query_button)
        time.sleep(1)

    def get_name(self):   #获取查询后的数据
        name = self.get_element_text(self.name_01)
        self.top_windows()
        return name

    suoshudiqu = "xpath=>//a[@class='textbox-icon combo-arrow']"
    cantoon = "xpath=>//span[contains(text(),'广东省')]"
    belong_unit = "xpath=>//td[contains(text(),'所属单位')]//following-sibling::td//a[@class='textbox-icon combo-arrow']"
    ceshike = "xpath=>//span[contains(text(),'测试科')]"

    def query_unit(self):   #通过所属单位进行查询
        self.execute_js(self.model)
        time.sleep(2)
        self.select_frame(self.find_element(self.frame0))
        self.click(self.suoshudiqu)
        time.sleep(1)
        self.click(self.cantoon)
        time.sleep(1)
        self.click(self.belong_unit)
        time.sleep(1)
        self.click(self.ceshike)
        time.sleep(1)
        self.click(self.query_button)
        time.sleep(2)

    select = "xpath=>//input[@name='ck']"
    edit_button = "xpath=>//span[contains(text(),'编辑角色')]"
    edit_frame = (By.NAME,'edit')
    def edit_role(self,name,new):   #编辑角色
        self.query_role(name)
        self.click(self.select)
        self.click(self.edit_button)
        self.wait_goframe(self.edit_frame)
        self.type(self.role,new)
        self.click(self.submit)
        time.sleep(2)

    assign_button = "xpath=>//span[contains(text(),'分配用户')]"
    user = "id=>userCode"
    peizhi = "xpath=>//span[contains(text(),'配置')]"
    list = "xpath=>//tr[@id='datagrid-row-r2-2-0']//div[@class='datagrid-cell datagrid-cell-c2-userRole']"
    def assign_user(self,name,code):   #分配用户
        self.query_role(name)
        self.click(self.select)
        self.click(self.assign_button)
        time.sleep(1)
        self.wait_goframe(self.edit_frame)
        self.type(self.user,code)
        self.click(self.query_button)
        time.sleep(1)
        self.click(self.select)
        self.click(self.peizhi)
        time.sleep(1)
        self.click(self.close_alert)
        time.sleep(2)

    close_button = "id=>closeButton"
    def peizhi_message(self):
        message = self.get_element_text(self.list)
        self.click(self.close_button)
        self.top_windows()
        return message

    assign_p = "xpath=>//span[contains(text(),'分配权限')]"
    wenshu = "xpath=>//span[contains(text(),'文书系统')]//preceding-sibling::span[@class='tree-checkbox tree-checkbox0']"

    def assign_privelege(self,name):
        self.query_role(name)
        self.click(self.select)
        self.click(self.assign_p)
        time.sleep(1)
        self.wait_goframe(self.edit_frame)
        self.click(self.wenshu)
        self.click(self.confirm)
        time.sleep(2)

    delete_button = "xpath=>//span[contains(text(),'删除角色')]"
    def delete_role(self,name):
        self.query_role(name)
        self.click(self.select)
        self.click(self.delete_button)
        time.sleep(1)
        self.click(self.close_alert)
        time.sleep(2)


