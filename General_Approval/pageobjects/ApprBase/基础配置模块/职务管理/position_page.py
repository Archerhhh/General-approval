import time
from framework.base_page import BasePage
from selenium.webdriver.common.by import By

class PositionPage(BasePage):

    model = "xpath=>//a[@href='/ApprBase/admin/system/role/toListJob.do']"
    frame0 ="xpath=>//iframe[@src='/ApprBase/admin/system/role/toListJob.do']"
    add_frame = (By.NAME,"new")
    edit_frame = (By.NAME,"edit")
    unit_frame = (By.NAME,"selectUnit")   #进入菜单页面及所有iframe

    #新增职务页面按钮
    add_button = "xpath=>//span[contains(text(),'新增职务')]"
    position = "id=>roleName"
    select_unit = "id=>selectUnit"
    query_unit = "id=>unitName"
    query_button = "xpath=>//input[@value='查 询']"
    choose_danwei = "xpath=>//span[contains(text(),'测试科')]"
    confrim = "xpath=>//input[@value='确定']"
    submit = "id=>sumbitButton"


    #获取弹窗信息元素，一般通用。
    alert = "xpath=>//div[@class='messager-body panel-body panel-body-noborder window-body']"
    close_alert = "xpath=>//span[contains(text(),'确定')]"

    def add_positon(self,name,unit):   #新增职务
        self.execute_js(self.model)
        self.select_frame(self.find_element(self.frame0))
        time.sleep(1)
        self.click(self.add_button)
        time.sleep(1)
        self.wait_goframe(self.add_frame)
        self.type(self.position,name)
        self.click(self.select_unit)
        time.sleep(1)
        self.wait_goframe(self.unit_frame)
        self.type(self.query_unit,unit)
        self.click(self.query_button)
        time.sleep(1)
        self.click(self.choose_danwei)
        self.click(self.confrim)
        time.sleep(1)
        self.wait_goframe(self.add_frame)
        self.click(self.submit)
        time.sleep(2)

    def get_message(self):    #获取弹窗信息，一般通用。
        message = self.get_element_text(self.alert)
        self.click(self.close_alert)
        self.top_windows()
        return message

    def query_position(self,name):   #通过职务名称查询
        self.execute_js(self.model)
        self.select_frame(self.find_element(self.frame0))
        time.sleep(1)
        self.type(self.position,name)
        self.click(self.query_button)
        time.sleep(2)

    list1= "xpath=>//div[@class='datagrid-cell datagrid-cell-c1-roleName']"
    def get_list(self):                 #获取查询后的列表字段
        message = self.get_element_text(self.list1)
        self.top_windows()
        return message

    diqu = "xpath=>//td[contains(text(),'所属地区')]//following-sibling::td//a[@class='textbox-icon combo-arrow']"
    select_g = "xpath=>//span[contains(text(),'广东省')]"
    danwei = "xpath=>//td[contains(text(),'所属单位')]//following-sibling::td//a[@class='textbox-icon combo-arrow']"
    select_d = "xpath=>//span[contains(text(),'测试科')]"

    def query_danwei(self):    #通过所属单位进行查询
        self.execute_js(self.model)
        self.select_frame(self.find_element(self.frame0))
        time.sleep(1)
        self.click(self.diqu)
        time.sleep(1)
        self.click(self.select_g)
        self.click(self.danwei)
        time.sleep(1)
        self.click(self.select_d)
        time.sleep(1)
        self.click(self.query_button)
        time.sleep(2)

    edit_button = "xpath=>//span[contains(text(),'编辑职务')]"
    choose = "xpath=>//input[@name='ck']"
    def edit_position(self,name,new):    #编辑职务
        self.query_position(name)
        self.click(self.choose)
        self.click(self.edit_button)
        time.sleep(1)
        self.wait_goframe(self.edit_frame)
        self.type(self.position,new)
        self.click(self.submit)
        time.sleep(2)

    assign_u = "xpath=>//span[contains(text(),'分配用户')]"
    userc = "id=>userCode"
    peizhi = "xpath=>//span[contains(text(),'配置')]"
    list2 = "xpath=>//tr[@id='datagrid-row-r2-2-0']//div[@class='datagrid-cell datagrid-cell-c2-userRole']"
    close = "id=>closeButton"
    def assign_user(self,name,code):  #分配用户
        self.query_position(name)
        self.click(self.choose)
        self.click(self.assign_u)
        time.sleep(1)
        self.wait_goframe(self.edit_frame)
        self.type(self.userc,code)
        self.click(self.query_button)
        time.sleep(1)
        self.click(self.choose)
        self.click(self.peizhi)
        time.sleep(1)
        self.click(self.close_alert)
        time.sleep(1)

    def get_peizhi(self):   #获取配置用户后的状态
        message = self.get_element_text(self.list2)
        self.click(self.close)
        self.top_windows()
        return message

    assign_p = "xpath=>//span[contains(text(),'分配权限')]"
    system = "xpath=>//span[contains(text(),'文书系统')]//preceding-sibling::span[@class='tree-checkbox tree-checkbox0']"
    def assign_privelege(self,name):
        self.query_position(name)
        self.click(self.choose)
        self.click(self.assign_p)
        time.sleep(1)
        self.wait_goframe(self.edit_frame)
        self.click(self.system)
        self.click(self.confrim)
        time.sleep(1)

    delete_button = "xpath=>//span[contains(text(),'删除职务')]"
    def delete_position(self,name):
        self.query_position(name)
        self.click(self.choose)
        self.click(self.delete_button)
        time.sleep(1)
        self.click(self.close_alert)
        time.sleep(1)


