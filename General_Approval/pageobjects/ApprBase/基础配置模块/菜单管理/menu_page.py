#-*- coding: UTF-8 -*-
import time
from framework.base_page import BasePage

class MenuPage(BasePage):

    menu_model = "xpath=>//a[@href='/ApprBase/admin/system/indexTree/toIndexTree.do']"
    frame0 = "xpath=>//iframe[@src='/ApprBase/admin/system/indexTree/toIndexTree.do']"
    add_father = "xpath=>//div[contains(text(),'新增顶级节点')]"
    new_node = "xpath=>//input[@id='nodeUrl']"
    drop_down = "xpath=>//select[@id='apprIndexTreeVo_nodeType']"
    select_value = "xpath=>//option[@value='2']"
    tijiao = "xpath=>//input[@value='提交']"

    def add_top(self,url):   #新增顶级节点
        self.execute_js(self.menu_model)   #打开菜单管理
        time.sleep(1)
        self.select_frame(self.find_element(self.frame0))
        self.execute_js(self.add_father)     #点击新增顶级节点
        self.click(self.new_node)
        self.type(self.new_node,url)
        self.click(self.drop_down)
        self.click(self.select_value)
        self.click(self.tijiao)

    message_el = "xpath=>//div[@class='messager-body panel-body panel-body-noborder window-body']"
    button = "xpath=>//span[contains(text(),'确定')]"
    # 获取弹窗信息
    def get_message(self):
        message = self.get_element_text(self.message_el)
        self.click(self.button)
        return message

    #删除菜单
    xinjiedian = "xpath=>//div[contains(@id,'_easyui_tree_')]/span[contains(text(),'新节点')]"
    shanchu = "xpath=>//div[contains(text(),'删除节点')]"
    def delete_menu(self):
        self.click(self.xinjiedian)
        time.sleep(1)
        self.execute_js(self.shanchu)
        time.sleep(1)

    #获取弹框并确定
    confirm_el = "xpath=>//div[@class='messager-body panel-body panel-body-noborder window-body']"
    confirm_button = "xpath=>//span[contains(text(),'确定')]"
    def get_confirm(self):
        message = self.get_element_text(self.confirm_el)
        self.click(self.confirm_button)
        return message



