import time
from framework.base_page import BasePage
from selenium.webdriver.common.by import By


class AppStepsPage(BasePage):

    model = "xpath=>//a[@href='/ApprSupport/appr/flow/apprStep/toApprStepList.do']"
    model_frame = "xpath=>//iframe[@src='/ApprSupport/appr/flow/apprStep/toApprStepList.do']"
    add_frame = (By.NAME,'addApprStepWin')
    edit_frame = (By.NAME,'editApprStepWin')
    unit_frame = (By.NAME,'selectUnit')    #菜单按钮及所有frame

    #新增页面所有按钮
    add_button = "xpath=>//span[contains(text(),'新增步骤')]"
    step_input = "id=>stepName"
    danwei = "id=>selectUnit"
    unit_input = "id=>unitName"
    query_button = "xpath=>//input[@value='查 询']"
    choose_query = "xpath=>//input[@name='ck']"
    confirm = "xpath=>//input[@value='确定']"
    desc = "id=>stepDesc"
    submit_button = "id=>sumbitButton"

    #获取弹窗页面元素，一般通用
    alert = "xpath=>//div[@class='messager-body panel-body panel-body-noborder window-body']"
    close_alert = "xpath=>//span[contains(text(),'确定')]"

    def add_step(self,name,unit,desc):    #新增步骤
        self.execute_js(self.model)
        time.sleep(1)
        self.select_frame(self.find_element(self.model_frame))
        self.click(self.add_button)
        time.sleep(2)
        self.wait_goframe(self.add_frame)
        self.type(self.step_input,name)
        self.click(self.danwei)
        time.sleep(2)
        self.wait_goframe(self.unit_frame)
        self.type(self.unit_input,unit)
        self.click(self.query_button)
        time.sleep(2)
        self.click(self.choose_query)
        self.click(self.confirm)
        time.sleep(1)
        self.wait_goframe(self.add_frame)
        self.type(self.desc,desc)
        self.click(self.submit_button)
        time.sleep(2)


    #获取弹窗信息，一般通用
    def get_message(self):
        message = self.get_element_text(self.alert)
        self.click(self.close_alert)
        return message

    list1= "xpath=>//tr[@id='datagrid-row-r1-2-0']//td[@field='stepName']"
    def query_step(self,step):    #通过步骤名称查询
        self.driver.refresh()
        time.sleep(2)
        self.execute_js(self.model)
        time.sleep(1)
        self.select_frame(self.find_element(self.model_frame))
        self.type(self.step_input,step)
        self.click(self.query_button)
        time.sleep(2)

    def get_list(self):    #获得查询后列表中第一行的数据
        message = self.get_element_text(self.list1)
        return message

    diqu = "xpath=>//a[@class='textbox-icon combo-arrow']"
    zhankai = "xpath=>//div[@id='_easyui_tree_2']//span[@class='tree-hit tree-collapsed']"
    dongguan = "xpath=>// span[contains(text(), '潮州市')]"
    ssdanwei = "xpath=>//td[contains(text(),'所属单位')]//following-sibling::td//a[@class='textbox-icon combo-arrow']"
    choose = "xpath=>//span[contains(text(),'自动化单位')]"

    def query_danwei(self):         #根据所属单位查询
        self.driver.refresh()
        time.sleep(2)
        self.execute_js(self.model)
        time.sleep(1)
        self.select_frame(self.find_element(self.model_frame))
        self.click(self.diqu)
        time.sleep(1)
        self.click(self.zhankai)
        time.sleep(1)
        self.click(self.dongguan)
        self.click(self.ssdanwei)
        time.sleep(1)
        self.click(self.choose)
        self.click(self.query_button)
        time.sleep(2)

    edit_button = "xpath=>//span[contains(text(),'编辑步骤')]"
    def edit_step(self,step,new):    #编辑步骤
        self.query_step(step)
        self.click(self.list1)
        self.click(self.edit_button)
        time.sleep(2)
        self.wait_goframe(self.edit_frame)
        self.type(self.step_input,new)
        self.click(self.submit_button)
        time.sleep(2)

    delete_button = "xpath=>//span[contains(text(),'删除步骤')]"
    def delete_step(self,step):   #删除步骤
        self.query_step(step)
        self.click(self.list1)
        self.click(self.delete_button)
        time.sleep(2)
        self.click(self.close_alert)
        time.sleep(1)
