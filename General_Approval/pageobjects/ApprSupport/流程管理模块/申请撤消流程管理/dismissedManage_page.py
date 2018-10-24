import time
from framework.base_page import BasePage
from selenium.webdriver.common.by import By


class SpecialManagePage(BasePage):
    model = "xpath=>//a[@href='/ApprSupport/appr/flow/apprFlow/toCancelFlowList.do']"
    model_frame = "xpath=>//iframe[@src='/ApprSupport/appr/flow/apprFlow/toCancelFlowList.do']"
    add_frame = (By.NAME,"addApprFlowWin")
    edit_frame = (By.NAME,"editApprFlowWin")
    unit_frame = (By.NAME,"selectUnit")
    copy_frame = (By.NAME,"copyApprFlowWin")   #菜单及所有frame

    #新增页面所有元素
    add_button = "xpath=>//span[contains(text(),'新增申请撤销流程')]"
    flow = "id=>flowName"
    unit = "id=>selectUnit"
    unit_name = "id=>unitName"
    query_button = "xpath=>//input[@value='查 询']"
    choose = "xpath=>//input[@name='ck']"
    confirm = "xpath=>//input[@value='确定']"
    desc = "id=>flowDesc"
    submit_button = "id=>sumbitButton"

    #弹窗信息页面
    alert = "xpath=>//div[@class='messager-body panel-body panel-body-noborder window-body']"
    close_alert ="xpath=>//span[contains(text(),'确定')]"

    def add_flow(self,unit,name,desc):      #新增流程
        self.execute_js(self.model)
        time.sleep(1)
        self.select_frame(self.find_element(self.model_frame))
        self.click(self.add_button)
        time.sleep(1)
        self.wait_goframe(self.add_frame)
        self.type(self.flow,unit)
        self.click(self.unit)
        time.sleep(2)
        self.wait_goframe(self.unit_frame)
        self.type(self.unit_name,name)
        self.click(self.query_button)
        time.sleep(2)
        self.click(self.choose)
        self.click(self.confirm)
        time.sleep(1)
        self.wait_goframe(self.add_frame)
        self.type(self.desc,desc)
        self.click(self.submit_button)
        time.sleep(2)

    def get_message(self):   #获取弹窗信息，一般通用
        message = self.get_element_text(self.alert)
        self.click(self.close_alert)
        return message

    def query_flow(self,name):
        self.driver.refresh()
        time.sleep(2)
        self.execute_js(self.model)
        time.sleep(1)
        self.select_frame(self.find_element(self.model_frame))
        self.type(self.flow,name)
        self.click(self.query_button)
        time.sleep(2)

    list1 = "xpath=>//tr[@id='datagrid-row-r1-2-0']//td[@field='flowName']"
    def get_list(self):
        message = self.get_element_text(self.list1)
        return message

    diqu = "xpath=>//a[@class='textbox-icon combo-arrow']"
    zhankai = "xpath=>//div[@id='_easyui_tree_2']//span[@class='tree-hit tree-collapsed']"
    dongguan = "xpath=>// span[contains(text(), '潮州市')]"
    ssdanwei = "xpath=>//td[contains(text(),'所属单位')]//following-sibling::td//a[@class='textbox-icon combo-arrow']"
    choose1 = "xpath=>//span[contains(text(),'自动化单位')]"

    def query_danwei(self):         #根据所属单位查询
        self.driver.refresh()
        time.sleep(2)
        self.execute_js(self.model)
        time.sleep(1)
        self.select_frame(self.find_element(self.model_frame))
        self.click(self.diqu)
        time.sleep(2)
        self.click(self.zhankai)
        time.sleep(1)
        self.click(self.dongguan)
        self.click(self.ssdanwei)
        time.sleep(1)
        self.click(self.choose1)
        self.click(self.query_button)
        time.sleep(2)

    edit_button = "xpath=>//span[contains(text(),'编辑申请撤销流程')]"
    def edit_step(self,name,new):    #编辑流程
        self.query_flow(name)
        self.click(self.list1)
        time.sleep(1)
        self.click(self.edit_button)
        time.sleep(2)
        self.wait_goframe(self.edit_frame)
        self.type(self.flow,new)
        time.sleep(1)
        self.click(self.submit_button)
        time.sleep(2)

    copy_button = "xpath=>//span[contains(text(),'复制流程')]"
    flow_1 = "xpath=>//input[@id='flowName']"
    copy = "xpath=>//span[contains(text(),'复制')]"
    close = "id=>closeButton"

    def copy_flow(self,name,new):   #复制流程
        self.query_flow(name)
        self.click(self.list1)
        self.click(self.copy_button)
        time.sleep(2)
        self.wait_goframe(self.copy_frame)
        self.type(self.flow_1,new)
        self.click(self.query_button)
        time.sleep(2)
        self.click(self.choose)
        self.click(self.copy)
        time.sleep(1)
        self.click(self.close)
        time.sleep(2)
        self.select_frame(self.find_element(self.model_frame))


    delete_button = "xpath=>//span[contains(text(),'删除申请撤销流程')]"
    def delete_flow(self,name):   #删除流程
        self.query_flow(name)
        self.click(self.list1)
        self.click(self.delete_button)
        time.sleep(2)
        self.click(self.close_alert)
        time.sleep(1)