# _*_ coding:utf-8 _*_
import configparser
from selenium import webdriver
from framework import getcwd
from framework.logger import logger

logger = logger(logger="BrowserEngine").getlog()

class BrowserEngine(object):

    dir = getcwd.get_cwd()
    #chrome_driver_path = dir + '/tools/chromedriver.exe'
    firefox_driver_path = dir + '/tools/geckodriver.exe'
    ie_driver_path = dir + '/tools/IEDriverServer.exe'

    def __init__(self,driver):
        self.driver = driver

    def open_browser(self,driver):
        config = configparser.ConfigParser()
        file_path = getcwd.get_cwd() + '/config/config.ini'
        config.read(file_path)

        browser = config.get("browserType","browserName")
        logger.info("you had select %s browser." % browser)
        url = config.get("testServer","URL")
        logger.info("The test server url is:%s" % url)

        if browser == "Firefox":
            driver = webdriver.Firefox(executable_path=self.firefox_driver_path)
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--headless')  # 指定无界面形式运行
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--no-sandbox')
            #chrome_options.add_argument('--start-maximized')
            chrome_options.add_argument('window-size=1920x1080')  # 指定浏览器分辨率
            chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
            #driver = webdriver.Chrome()
            driver = webdriver.Chrome(chrome_options=chrome_options)
            logger.info("Starting chrome browser.")
        elif browser =="IE":
            driver=webdriver.Ie(self.ie_driver_path)
            logger.info("Starting IE browser")

        driver.get(url)
        logger.info("Open url:%s" % url)
        driver.maximize_window()
        logger.info("Maxmize the current window.")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 8 seconds.")
        return driver

    def browse_name(self):
        config = configparser.ConfigParser()
        file_path = getcwd.get_cwd() + '/config/config.ini'
        config.read(file_path)
        browser = config.get("browserType", "browserName")
        return browser

    def quit_browse(self):
        logger.info("Now,close and quit the browser")
        self.driver.quit()


