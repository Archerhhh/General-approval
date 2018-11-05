#-*- coding: UTF-8 -*-
import os,time

k=1
while k < 2:
     now_time = time.strftime('%H_%M')
     if now_time == "17_14":
         print("start run script")
         os.chdir(r"D:\PycharmProjects\General Approval\testsuites")
         os.system('python TestRunner.py') #执行脚本
         print("run script ended")
         break   #如何想每天定时运行任务，只需去掉break
     else:
        time.sleep(10)
        print(now_time)
