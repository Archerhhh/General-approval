import time
from framework.base_page import BasePage
from selenium.webdriver.common.by import By


class BusinessPage(BasePage):

    model = "xpath=>//a[@href='/ApprSupport/appr/flow/apprFlow/toApprLayerFlowList.do']"
    model_frame = "xpath=>//iframe[@src='/ApprSupport/appr/flow/apprFlow/toApprLayerFlowList.do']"
    add_frame = (By.NAME,"addApprFlowWin")
    edit_frame = (By.NAME,"editApprFlowWin")
    unit_frame = (By.NAME,"selectUnit")
    copy_frame = (By.NAME,"copyApprFlowWin")    #菜单及所有frame

    #新增页面所有frame
    add_button = "xpath=>//span[contains(text(),'新增业务流程')]"
    flow = "id=>flowName"
    select_unit = "id=>selectUnit"
    unit_name = "id=>unitName"
    query_button = "xpath=>//input[@value='查 询']"
    choose_result = "xpath=>//input[@name='ck']"
    confirm = "xpath=>//input[@value='确定']"
    desc = "id=>flowDesc"
    submit = "id=>sumbitButton"

    #弹窗的元素，一般通用
    alert = "xpath=>//div[@class='messager-body panel-body panel-body-noborder window-body']"
    alert_close = "xpath=>//span[contains(text(),'确定')]"

    def add_flow(self,flow,name,desc):  #新增流程
        self.execute_js(self.model)
        time.sleep(1)
        self.select_frame(self.find_element(self.model_frame))
        self.click(self.add_button)
        time.sleep(1)
        self.wait_goframe(self.add_frame)
        self.type(self.flow,flow)
        self.click(self.select_unit)
        time.sleep(2)
        self.wait_goframe(self.unit_frame)
        self.type(self.unit_name,name)
        self.click(self.query_button)
        time.sleep(2)
        self.click(self.choose_result)
        self.click(self.confirm)
        time.sleep(1)
        self.wait_goframe(self.add_frame)
        self.type(self.desc,desc)
        self.click(self.submit)
        time.sleep(2)

    def get_message(self):      #获取弹窗信息
        message = self.get_element_text(self.alert)
        self.click(self.alert_close)
        return message

    list1 = "xpath=>//tr[@id='datagrid-row-r1-2-0']//td[@field='flowName']"
    def query_name(self,name):   #通过流程名称查询
        self.driver.refresh()
        time.sleep(2)
        self.execute_js(self.model)
        time.sleep(1)
        self.select_frame(self.find_element(self.model_frame))
        self.type(self.flow,name)
        self.click(self.query_button)
        time.sleep(2)

    def get_result(self):   #获取查询列表数据
        result = self.get_element_text(self.list1)
        return result

    diqu = "xpath=>//a[@class='textbox-icon combo-arrow']"
    zhankai = "xpath=>//div[@id='_easyui_tree_2']//span[@class='tree-hit tree-collapsed']"
    chao = "xpath=>// span[contains(text(), '潮州市')]"
    danwei = "xpath=>//td[contains(text(),'所属单位')]//following-sibling::td//a[@class='textbox-icon combo-arrow']"
    choose = "xpath=>//span[contains(text(),'自动化单位')]"

    def query_danwei(self):    #通过单位进行查询
        self.driver.refresh()
        time.sleep(2)
        self.execute_js(self.model)
        time.sleep(1)
        self.select_frame(self.find_element(self.model_frame))
        self.click(self.diqu)
        time.sleep(1)
        self.click(self.zhankai)
        time.sleep(1)
        self.click(self.chao)
        self.click(self.danwei)
        time.sleep(1)
        self.click(self.choose)
        self.click(self.query_button)
        time.sleep(2)

    result = "xpath=>//tr[@id='datagrid-row-r1-2-0']//td[@field='flowName']"
    edit_button = "xpath=>//span[contains(text(),'编辑业务流程')]"
    def edit_flow(self,name,new):    #编辑流程
        self.query_name(name)
        self.click(self.result)
        self.click(self.edit_button)
        time.sleep(1)
        self.wait_goframe(self.edit_frame)
        self.type(self.flow,new)
        self.click(self.submit)
        time.sleep(2)

    copy_button = "xpath=>//span[contains(text(),'复制流程')]"
    copy = "xpath=>//span[contains(text(),'复制')]"
    close = "id=>closeButton"
    def copy_flow(self,name,new):   #复制流程
        self.query_name(name)
        self.click(self.result)
        self.click(self.copy_button)
        time.sleep(1)
        self.wait_goframe(self.copy_frame)
        self.type(self.flow,new)
        self.click(self.query_button)
        time.sleep(1)
        self.click(self.choose_result)
        self.click(self.copy)
        time.sleep(1)
        self.click(self.close)
        time.sleep(1)
        self.select_frame(self.find_element(self.model_frame))

    delete_button = "xpath=>//span[contains(text(),'删除业务流程')]"

    def delete_flow(self,name):
        self.query_name(name)
        self.click(self.result)
        self.click(self.delete_button)
        time.sleep(1)
        self.click(self.alert_close)
        time.sleep(1)






