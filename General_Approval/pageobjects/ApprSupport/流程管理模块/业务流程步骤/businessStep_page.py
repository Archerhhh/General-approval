import time
from framework.base_page import BasePage
from selenium.webdriver.common.by import By


class BusiStepPage(BasePage):
    model = "xpath=>//a[@href='/ApprSupport/appr/flow/apprStep/toApprLayerStepList.do']"
    model_frame = "xpath=>//iframe[@src='/ApprSupport/appr/flow/apprStep/toApprLayerStepList.do']"
    add_frame = (By.NAME,"addApprStepWin")
    edit_frame = (By.NAME,"editApprStepWin")
    unit_frame = (By.NAME,"selectUnit")    #菜单及页面所有frame

    #新增步骤所有元素
    add_button = "xpath=>//span[contains(text(),'新增步骤')]"
    step = "id=>stepName"
    grade = "id=>areaLevel"
    value ="xpath=>//option[@value='2']"
    danwei = "id=>selectUnit"
    unit = "id=>unitName"
    query_button = "xpath=>//input[@value='查 询']"
    choose_result = "xpath=>//input[@name='ck']"
    confirm = "xpath=>//input[@value='确定']"
    stepdes = "id=>stepDesc"
    submit = "id=>sumbitButton"

    #弹窗信息，一般通用
    alert = "xpath=>//div[@class='messager-body panel-body panel-body-noborder window-body']"
    close_alert = "xpath=>//span[contains(text(),'确定')]"

    def add_step(self,step,unit,stepdes):       #新增流程步骤
        self.execute_js(self.model)
        time.sleep(1)
        self.select_frame(self.find_element(self.model_frame))
        self.click(self.add_button)
        self.wait_goframe(self.add_frame)
        time.sleep(1)
        self.type(self.step,step)
        self.click(self.grade)
        time.sleep(1)
        self.click(self.value)
        self.click(self.danwei)
        time.sleep(1)
        self.wait_goframe(self.unit_frame)
        self.type(self.unit,unit)
        self.click(self.query_button)
        time.sleep(2)
        self.click(self.choose_result)
        self.click(self.confirm)
        time.sleep(1)
        self.wait_goframe(self.add_frame)
        self.type(self.stepdes,stepdes)
        self.click(self.submit)
        time.sleep(2)

    def get_message(self):   #获取弹窗消息，一般通用
        message = self.get_element_text(self.alert)
        self.click(self.close_alert)
        return message

    def query_stepname(self,step):  #通过步骤名称进行查询
        self.driver.refresh()
        time.sleep(2)
        self.execute_js(self.model)
        time.sleep(1)
        self.select_frame(self.find_element(self.model_frame))
        self.type(self.step,step)
        self.click(self.query_button)
        time.sleep(2)

    list1 = "xpath=>//tr[@id='datagrid-row-r1-2-0']//td[@field='stepName']"
    def get_result(self): #获取查询后的列表数据
        result = self.get_element_text(self.list1)
        return result

    suoshudanwei = "xpath=>//td[contains(text(),'所属单位')]//following-sibling::td//a[@class='textbox-icon combo-arrow']"
    choosedanwei = "xpath=>//span[contains(text(),'自动化单位')]"

    def query_danwei(self):   #所属单位查询
        self.driver.refresh()
        time.sleep(2)
        self.execute_js(self.model)
        time.sleep(1)
        self.select_frame(self.find_element(self.model_frame))
        self.click(self.suoshudanwei)
        time.sleep(1)
        self.click(self.choosedanwei)
        self.click(self.query_button)
        time.sleep(2)

    diqu = "xpath=>//a[@class='textbox-icon combo-arrow']"
    zhankai = "xpath=>//div[@id='_easyui_tree_2']//span[@class='tree-hit tree-collapsed']"
    choose_c = "xpath=>// span[contains(text(), '潮州市')]"
    def query_diqu(self):   #所属地区查询
        self.driver.refresh()
        time.sleep(2)
        self.execute_js(self.model)
        time.sleep(1)
        self.select_frame(self.find_element(self.model_frame))
        self.click(self.diqu)
        time.sleep(1)
        self.execute_js(self.zhankai)
        time.sleep(1)
        self.click(self.choose_c)
        self.click(self.query_button)
        time.sleep(2)

    edit_button = "xpath=>//span[contains(text(),'编辑步骤')]"
    new_value = "xpath=>//option[@value='3']"
    def edit_step(self,step,new):
        self.query_stepname(step)
        self.click(self.list1)
        self.click(self.edit_button)
        time.sleep(2)
        self.wait_goframe(self.edit_frame)
        self.type(self.step,new)
        self.click(self.grade)
        time.sleep(1)
        self.click(self.new_value)
        self.click(self.submit)
        time.sleep(2)

    delete_button = "xpath=>//span[contains(text(),'删除步骤')]"
    def delete_step(self,step):
        self.query_stepname(step)
        self.click(self.list1)
        self.click(self.delete_button)
        time.sleep(1)
        self.click(self.close_alert)
        time.sleep(1)






