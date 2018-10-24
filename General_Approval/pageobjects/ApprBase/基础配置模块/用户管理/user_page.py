import time
from framework.base_page import BasePage
from selenium.webdriver.common.by import By

class UserPage(BasePage):

    model = "xpath=>//a[@href='/ApprBase/admin/system/user/toListUser.do']"
    iframe0 = "xpath=>//iframe[@src='/ApprBase/admin/system/user/toListUser.do']"
    new_frame = (By.NAME,'new')
    edit_frame = (By.NAME,'edit')
    password_frame = (By.NAME,'update')
    unit_frame = (By.NAME,'selectUnit')  #菜单及页面所有ifram


    add_button = "xpath=>//span[contains(text(),'新增用户')]"
    usercode = "id=>userCode"
    username = "id=>fullName"
    userpassword1 = "id=>userPwd"
    userpassword2 = "id=>userPwd2"  #填写用户信息

    belong_unit = "id=>selectUnit"
    unit_name  ="xpath=>//input[@id='unitName']"
    query_button = "xpath=>//input[@value='查 询']"
    select = "xpath=>//input[@name='ck']"
    confrim = "xpath=>//input[@value='确定']"   #选择所属单位所有元素

    user_type = "id=>userRole"
    choose = "xpath=>//option[@value=2]"    #用户类型
    submit = "id=>sumbitButton"

    alert = "xpath=>//div[@class='messager-body panel-body panel-body-noborder window-body']"
    close_alert = "xpath=>//span[contains(text(),'确定')]"

    def  add_user(self,code,name,password1,password2,unit):   #新增用户
        self.execute_js(self.model)
        self.select_frame(self.find_element(self.iframe0))
        time.sleep(1)
        self.click(self.add_button)
        time.sleep(1)
        self.wait_goframe(self.new_frame)
        self.type(self.usercode,code)
        self.type(self.username,name)
        self.type(self.userpassword1,password1)
        self.type(self.userpassword2,password2)
        self.click(self.belong_unit)
        time.sleep(1)
        self.wait_goframe(self.unit_frame)
        self.type(self.unit_name,unit)
        self.click(self.query_button)
        time.sleep(1)
        self.click(self.select)
        self.click(self.confrim)
        self.wait_goframe(self.new_frame)
        self.click(self.user_type)
        self.click(self.choose)
        time.sleep(1)
        self.click(self.submit)
        time.sleep(2)

    def get_message(self):   #获取弹窗信息，一般通用
        message = self.get_element_text(self.alert)
        self.click(self.close_alert)
        self.top_windows()
        return message

    query_code = "id=>userCode"
    query_name = "id=>userName"
    disable = "xpath=>//span[contains(text(),'不启用')]"
    enable = "xpath=>//span[contains(text(),'启用')]"

    def enable_disable(self,code,name):
        self.execute_js(self.model)
        self.select_frame(self.find_element(self.iframe0))
        time.sleep(1)
        self.type(self.query_code,code)
        self.type(self.query_name,name)
        self.click(self.query_button)
        time.sleep(1)
        self.click(self.select)
        self.click(self.disable)
        time.sleep(1)
        self.click(self.close_alert)
        time.sleep(1)
        self.click(self.close_alert)
        time.sleep(1)
        self.click(self.select)
        self.click(self.enable)
        time.sleep(1)
        self.click(self.close_alert)
        time.sleep(1)

    edit_button="xpath=>//span[contains(text(),'编辑用户')]"
    gonghao = "xpath=>//*[@id='submitForm']/table/tbody/tr[17]/td[2]/textarea"
    def edit_user(self,code,name,id):
        self.execute_js(self.model)
        self.select_frame(self.find_element(self.iframe0))
        time.sleep(1)
        self.type(self.query_code,code)
        self.type(self.query_name,name)
        self.click(self.query_button)
        time.sleep(1)
        self.click(self.select)
        self.click(self.edit_button)
        self.wait_goframe(self.edit_frame)
        self.type(self.gonghao,id)
        self.click(self.submit)
        time.sleep(2)

    set_passwrod = "xpath=>//span[contains(text(),'设置密码')]"

    def change_password(self,code,name,pwd1,pwd2):
        self.execute_js(self.model)
        self.select_frame(self.find_element(self.iframe0))
        time.sleep(1)
        self.type(self.query_code,code)
        self.type(self.query_name,name)
        self.click(self.query_button)
        time.sleep(1)
        self.click(self.select)
        self.click(self.set_passwrod)
        self.wait_goframe(self.password_frame)
        self.type(self.userpassword1,pwd1)
        self.type(self.userpassword2,pwd2)
        self.click(self.submit)
        time.sleep(2)
