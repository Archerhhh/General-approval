import time
from framework.base_page import BasePage
from selenium.webdriver.common.by import By


class ItemPage(BasePage):
    model = "xpath=>//a[@href='/ApprSupport/appr/item/itemManage/init/toItemList.do']"
    frame0 = "xpath=>//iframe[@src='/ApprSupport/appr/item/itemManage/init/toItemList.do']"
    add_frame = (By.NAME,"edit")
    unit_frame = (By.NAME,"selectUnit")
    deal_frame = (By.ID,"dealLimit")    #打开模板及页面所有frame

     #基本信息页面所有元素
    duli_button = "xpath=>//span[contains(text(),'独立事项')]"
    item_name = "xpath=>//input[@id='_easyui_textbox_input1']"
    jiancha_code = "xpath=>//input[@id='_easyui_textbox_input2']"
    choose_danwei = "id=>bzUnitBtn"
    unit_name = "id=>unitName"
    query_button = "xpath=>//input[@value='查 询']"
    choose_ke = "xpath=>//span[contains(text(),'测试科')]"
    confirm = "xpath=>//input[@value='确定']"
    item_type = "xpath=>//td[contains(text(),'事项类型')]//following-sibling::td//a[@class='textbox-icon combo-arrow']"
    xing = "xpath=>//div[contains(text(),'行政许可')]"
    server = "xpath=>//td[contains(text(),'服务对象')]//following-sibling::td//span[@class='textbox combo']"
    geren = "xpath=>//div[contains(text(),'企业/个人')]"

      # 办理时限tab元素
    banli = "xpath=>//span[contains(text(),'办理时限')]"
    add_list = "xpath=>/html/body/div[1]/div/div/div/div[1]/table/tbody/tr/td[1]/a/span/span[1]"
    list = "xpath=>//tr[@id='datagrid-row-r1-2-0']//td[@field='ptLimit']"
    shixian = "xpath=>//tr[@id='datagrid-row-r1-2-0']//td[@field='ptLimit']//input[@class='textbox-text validatebox-text textbox-prompt']"
    fading = "xpath=>//td[@field='ptLegalLimit']//input[@class='textbox-text validatebox-text textbox-prompt']"
    save = "xpath=>//a[@onclick='doSave()']"
    close_alert = "xpath=>//span[contains(text(),'确定')]"
    close = "xpath=>//button[@i='close']"

    def add_duli(self,name,number,unitname,time1,time2):
         #基本信息页面操作
        self.execute_js(self.model)
        time.sleep(1)
        self.select_frame(self.find_element(self.frame0))
        self.execute_js(self.duli_button)
        time.sleep(3)
        self.wait_goframe(self.add_frame)
        self.type(self.item_name,name)
        self.type(self.jiancha_code,number)
        self.click(self.choose_danwei)
        time.sleep(1)
        self.wait_goframe(self.unit_frame)
        self.type(self.unit_name,unitname)
        self.click(self.query_button)
        time.sleep(1)
        self.click(self.choose_ke)
        self.click(self.confirm)
        time.sleep(1)
        self.wait_goframe(self.add_frame)
        self.click(self.item_type)
        self.click(self.xing)
        self.click(self.server)
        self.click(self.geren)
         # 办理时限页面操作
        self.click(self.banli)
        time.sleep(2)
        self.wait_gonextframe(self.deal_frame)
        self.click(self.add_list)
        self.double_click(self.list)
        time.sleep(1)
        self.type(self.shixian,time1)
        self.type(self.fading,time2)
        self.wait_goframe(self.add_frame)
        self.click(self.save)
        time.sleep(3)

    alert = "xpath=>//div[@class='messager-body panel-body panel-body-noborder window-body']"

    def get_message(self):     #获取保存后的弹窗信息
        message = self.get_element_text(self.alert)
        self.click(self.close_alert)
        time.sleep(4)
        self.top_windows()
        self.click(self.close)
        return message

    mulu_button = "xpath=>//span[contains(text(),'事项目录')]"
    def add_mulu(self,name,number,unitname):   #新增目录事项
        self.execute_js(self.model)
        time.sleep(1)
        self.select_frame(self.find_element(self.frame0))
        self.execute_js(self.mulu_button)
        time.sleep(3)
        self.wait_goframe(self.add_frame)
        self.type(self.item_name,name)
        self.type(self.jiancha_code,number)
        self.click(self.choose_danwei)
        time.sleep(1)
        self.wait_goframe(self.unit_frame)
        self.type(self.unit_name,unitname)
        self.click(self.query_button)
        time.sleep(1)
        self.click(self.choose_ke)
        self.click(self.confirm)
        time.sleep(1)
        self.wait_goframe(self.add_frame)
        self.click(self.save)

    item_qu = "id=>itemCode"
    list1 = "xpath=>//tr[@id='datagrid-row-r1-2-328b1e95b7cf4fb7aba3f9e830006b27']//td[@field='itemCode']"
    def query_item(self,code):  #事项编号查询并取得查询结果
        self.execute_js(self.model)
        time.sleep(1)
        self.select_frame(self.find_element(self.frame0))
        self.type(self.item_qu,code)
        self.click(self.query_button)
        time.sleep(3)
        message = self.get_element_text(self.list1)
        self.top_windows()
        return message

    way = "xpath=>//td[contains(text(),'办理方式')]//following-sibling::td//span[@class='textbox combo']"
    choose = "xpath=>//div[@class='combo-panel panel-body panel-body-noheader']//div[contains(text(),'行政罚款')]"
    list2 = "xpath=>//tr[@id='datagrid-row-r1-2-6678']//td[@field='approveDealwithWay']"
    def query_way(self):  #办理方式查询并取得查询结果
        self.execute_js(self.model)
        time.sleep(1)
        self.select_frame(self.find_element(self.frame0))
        self.click(self.way)
        self.click(self.choose)
        self.click(self.query_button)
        time.sleep(3)
        message = self.get_element_text(self.list2)
        self.top_windows()
        return message

    diqu = "xpath=>//td[contains(text(),'所属地区')]//following-sibling::td//a[@class='textbox-icon combo-arrow']"
    zhankai = "xpath=>//div[@id='_easyui_tree_2']//span[@class='tree-hit tree-collapsed']"
    choose_c = "xpath=>// span[contains(text(), '潮州市')]"
    danwei = "xpath=>//td[contains(text(),'所属单位')]//following-sibling::td//a[@class='textbox-icon combo-arrow']"
    click_danwei = "xpath=>//span[contains(text(),'自动化单位')]"
    list3 = "xpath=>//tr[@id='datagrid-row-r1-2-328b1e95b7cf4fb7aba3f9e830006b27']//td[@field='unitName']"

    def query_danwei(self):  #所属单位查询并取得查询结果
        self.execute_js(self.model)
        time.sleep(1)
        self.select_frame(self.find_element(self.frame0))
        self.click(self.diqu)
        time.sleep(2)
        self.click(self.zhankai)
        time.sleep(2)
        self.click(self.choose_c)
        self.click(self.danwei)
        time.sleep(1)
        self.click(self.click_danwei)
        self.click(self.query_button)
        time.sleep(2)
        message = self.get_element_text(self.list3)
        self.top_windows()
        return message






