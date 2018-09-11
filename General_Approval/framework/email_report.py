#coding=utf-8
import smtplib
from email.mime.text import MIMEText
import time,os
from framework.logger import logger
from framework import getcwd

logger = logger(logger="EmailReport").getlog()
class EmailReport():

    def send_mail(self,file_new):   #定义发送邮件的方法
         #发信邮箱
        mail_from = "1051137151@qq.com"
        #收信邮箱
        mail_to = "lizw@minstone.com.cn"
        #定义正文
        f = open(file_new,'rb')
        mail_body = f.read()
        f.close()
        msg = MIMEText(mail_body,_subtype='html',_charset='utf-8')
        #定义标题
        msg['subject'] = u"自动化测试报告"
        #定义发送时间
        msg['date'] = time.strftime('%a,%d %b %Y %H:%M:%S $z')

        logger.info('connectting email server.....')
        s=smtplib.SMTP_SSL('smtp.qq.com',465)  #QQ邮箱使用安全连接，需要使用SMTP_SSL方法
        #用户名与密码
        logger.info('logging email.....')
        s.login('1051137151', 'kdwjnxrahtofbeaf')
        s.sendmail(mail_from,mail_to,msg.as_string())
        s.quit()
        logger.info('email has sent')

    def send_report(self):
         dir = getcwd.get_cwd()
         result_dir = dir +'/test_report'
         lists = os.listdir(result_dir)
         lists.sort(key= lambda fn: os.path.getatime(result_dir+"\\"+fn))
         #找到最新生成的文件
         file_new = os.path.join(result_dir,lists[-1])
         logger.info("the report:" + file_new + "will be send" )
         self.send_mail(file_new)
