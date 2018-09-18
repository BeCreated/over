# -*- coding: utf-8 -*
# Time    : 2018/9/6 9:55

import schedule
import time


def job():
    ti = time.localtime()
    t = time.strftime('%Y-%m-%d %H-%M-%S', ti)
    print("I'm working...", t)

# 设置任务计划
# 多个任务定时设置是阻塞式运行的

schedule.every(1).seconds.do(job)
# 每十分钟执行一次
schedule.every(10).minutes.do(job)
# 每小时执行一次
schedule.every().hour.do(job)
# 每天执行一次
schedule.every().day.at("10:30").do(job)
# 每月执行一次
schedule.every().monday.do(job)
# 每周执行一次
schedule.every().wednesday.at("13:15").do(job)

while True:
    ti = time.localtime()
    t = time.strftime('%Y-%m-%d %H-%M-%S', ti)
    # while循环，一直执行任务
    schedule.run_pending()
    time.sleep(1)