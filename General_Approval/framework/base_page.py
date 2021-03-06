﻿#-*- coding: UTF-8 -*-
import time
# import win32api
# import win32gui
# import win32con
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from framework import getcwd
from framework.browser_engine import BrowserEngine
from framework.logger import logger


# create a logger instance
logger = logger(logger="BasePage").getlog()


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver

        # quit browser and end testing

    def quit_browser(self):
        self.driver.quit()

        # 浏览器前进操作

    def forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")

        # 浏览器后退操作

    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")

        # 隐式等待

    def implicitly_wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds." % seconds)

    def wait_elclickable(self,locator):
        try:
            El = WebDriverWait(self.driver,15).until(EC.element_to_be_clickable(locator))
            text = El.text
            logger.info("had wait for the elclickable: %s"%text)
        except TimeoutError as e:
            logger.error("can't wait fort the elclickable:%s"%e)
            self.get_windows_img()

        #显式等待某个元素
    def wait_element(self, locator):
        try:
            El = WebDriverWait(self.driver,15).until(EC.presence_of_element_located(locator))
            text = El.text
            logger.info("had wait for the element: %s"%text)
        except TimeoutError as e:
            logger.error("can't wait fort the element:%s"%e)
            self.get_windows_img()
        #locator 格式为：(By.ID,'id'),(By.NAME,'name'),(By.XPATH,'xpath')
        #WebDriverWait(self.driver,wait,waitFrequence).until(lambda x:x.find_element_by_id('id'))

        #显式等待多个元素,locator定位一组元素
    def wait_elements(self,locator):
        try:
            WebDriverWait(self.driver,15).until(EC.presence_of_all_elements_located(locator))
            logger.info("had wait for all elements")
        except TimeoutError as e:
            logger.error("can't wait for elements:%s"%e)
            self.get_windows_img()

        #显式等待frame并且进入frame
    def wait_goframe(self,locator):
        try:
            self.top_windows()
            WebDriverWait(self.driver, 15).until(EC.frame_to_be_available_and_switch_to_it(locator))
            logger.info("had wait and changed frame")
        except TimeoutError as e:
            logger.error("can't wait for frame:%s"%e)
            self.get_windows_img()
        #判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False
            #嵌套的ifram不需要切回主窗口，一层层切换进去。
    def wait_gonextframe(self, locator):
        try:
            WebDriverWait(self.driver, 15).until(EC.frame_to_be_available_and_switch_to_it(locator))
            logger.info("had wait and changed frame")
        except TimeoutError as e:
            logger.error("can't wait for frame:%s" % e)
            self.get_windows_img()

        #显式等待弹窗
    def wait_alert(self):
        try:
            WebDriverWait(self.driver,15).until(EC.alert_is_present())
            logger.info("had wait for the alert")
        except TimeoutError as e:
            logger.error("can't wait for alert:%s"%e)
            self.get_windows_img()

        #显式等待元素内容变成指定内容
    def wait_eltext(self,locator,text):  #locator内容需要括号括起来
        try:
            WebDriverWait(self.driver,15).until(EC.text_to_be_present_in_element(locator,text))
            logger.info('had wait for the text loaded:%s'%text)
        except TimeoutError as e:
            logger.error("can't wait for the text loaded:%s"%e)
            self.get_windows_img()

    #显式等待元素的值为text，一般用于输入框
    def wait_elvalue(self,locator,text):
        try:
            WebDriverWait(self.driver,15).until(EC.text_to_be_present_in_element_value(locator,text))
            logger.info('had wait for the input value:%s'%text)
        except TimeoutError as e:
            logger.error("can't wait for the input value:%s"%e)
            self.get_windows_img()

        # 点击关闭当前窗口

    def close(self):
        try:
            self.driver.close()
            logger.info("Closing and quit the browser.")
        except NameError as e:
            logger.error("Failed to quit the browser with %s" % e)

            # 保存图片

    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        file_path = getcwd.get_cwd() + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder : /screenshots")
            print(screen_name)
        except NameError as e:
            logger.error("Failed to take screenshot! %s" % e)

            # 定位元素方法

    def find_element(self, selector):
        """
         这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
         submit_btn = "id=>su"
         login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
         如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return: element
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()  # take screenshot
        elif selector_by == "n" or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("Had find the element \' %s \' successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

        # 输入

    def type(self, selector, text):

        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" % e)
            self.get_windows_img()

            # 清除文本框

    def clear(self, selector):

        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

            # 点击元素

    def click(self, selector):

        el = self.find_element(selector)
        try:
            text = el.text
            el.click()
            logger.info("The element \' %s \' was clicked." % text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

            # 获取网页标题

    def get_page_title(self):
        logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)

        # 获取元素内容
    def get_element_text(self, selector):
        el = self.find_element(selector)
        try:
            element_text = el.text
            logger.info("The element_text is: %s" % element_text)
            return element_text
        except NameError as e:
            logger.error("failed to get text:%s"%e)

     # 获取input里的内容
    def get_input_text(self,selector):
        el = self.find_element(selector)
        try:
            input_text = el.get_attribute('value')
            logger.info("the input_text is:%s"% input_text)
            return input_text
        except NameError as e:
            logger.error("failed to get input value:%s"%e)

        # 鼠标悬停操作
    def mouse_stop(self, selector):
        element = self.find_element(selector)
        try:
            ActionChains(self.driver).move_to_element(element).perform()
            logger.info("mouse stop on the element")
        except NameError as e:
            logger.error("can't mouse stop:%s"%e)

    def double_click(self,selector):
        element = self.find_element(selector)
        try:
            ActionChains(self.driver).double_click(element).perform()
            logger.info("double click on the element")
        except NameError as e:
            logger.error("can't double click:%s" % e)

        # 选择下拉框操作
    def select_dropdown(self, selector, text):
        element = self.find_element(selector)
        # Select(element).select_by_index(index)
        # Select(element).select_by_value(value)
        try:
            Select(element).select_by_visible_text(text)
            logger.info("had select %s"%text)
        except NameError as e:
            logger.error("can't select the text:%s"%e)
            self.get_windows_img()

        # 切换到指定的iframe
    def select_frame(self, reference):
        try:
            self.top_windows()
            self.driver.switch_to.frame(reference)
        #self.driver.switch_to.frame(0)  # 1.用frame的index来定位，第一个是0
        # self.driver.switch_to.frame("frame1")  # 2.用id来定位
        # self.driver.switch_to.frame("myframe")  # 3.用name来定位
        # self.driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))  # 4.用WebElement对象来定位
            logger.info("had changed the frame")
        except NameError as e:
            logger.error("can't change to frame:%s"%e)
            self.get_windows_img()

        # 从iframe切换回主窗口
    def top_windows(self):
        self.driver.switch_to.default_content()
        logger.info("had came back to the main frame")

        # 多窗口切换
    def select_windows(self):
        handles = self.driver.window_handles  #获取全部窗口

        for handle in handles:
            if handle != self.driver.current_window_handle:
                logger.info("switch to second window:%s "% handle)
                self.driver.switch_to_window(handle)

        # 将滚动条拉到顶部

    def scroll_top(self):
        try:
            browser = BrowserEngine(self)
            browser_name = browser.browse_name()
            if browser_name == "Chrome":
                js =  "var  q=document.body.scrollTop=0"

            else:
                js = "var q = document.documentElement.scrollTop=o"
            self.driver.execute_script(js)
            logger.info("had scroll to the top")
        except Exception as e:
            logger.error("can't scroll to top:%s"%e)
            self.get_windows_img()
        #将滚动条拉到底部

    def scroll_foot(self):
        try:
            browser = BrowserEngine(self)
            browser_name = browser.browse_name()
            if browser_name =="Chrome":
                js ="var q = document.body.scrollTop=10000"
            else:
                js ="var q = document.documentElement.scrollTop=10000"
            self.driver.execute_script(js)
            logger.info("had scroll to the foot")
        except Exception as e:
            logger.error("can't scoll to foot:%s"%e)
            self.get_windows_img()

        # 通过元素拉动滚动条到指定位置

    def scrollby_element(self,selector):
        el = self.find_element(selector)
        try:
            self.driver.excute_script("arguments[0].scrollIntoView(true);",el)
            logger.info("had scroll to the element target ")
        except NameError as e:
            logger.error("can't scoll to the element:%s"%e)

        #获取alert信息并关闭alert
    def get_alert(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_message = alert.text
            alert.accept()
            logger.info("closed alert and alert message is %s"%alert_message)
            return alert_message
        except Exception as e:
            logger.info("error to operater alert:%s"%e)
            self.get_windows_img()

        #通过pywin32进行文件上传操作。
    '''
    def upload(self,windowtitle,filepath):
        dialog = win32gui.FindWindow('#32770', windowtitle)  # 对话框
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
        Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
        button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button

        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, filepath)  # 往输入框输入绝对地址
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
    '''
        # 通过JS来点击元素。
    def execute_js(self,selector):
        element = self.find_element(selector)
        text = element.text
        self.driver.execute_script('$(arguments[0]).click()', element)
        logger.info("had click the button:%s"%text)

