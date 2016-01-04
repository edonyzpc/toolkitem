#encoding=utf-8
print '中国'
#执行定时任务 在某个时刻执行该任务
import time, os, sys, sched
#执行计划 第一个参数要执行的时间，第二个参数用来等待一段时间
schedule=sched.scheduler(time.time, time.sleep)
def perform_command(cmd, inc):
    #enter 延迟时间 优先级 回调函数 参数
    os.system(cmd)
    print ''
    print time.time()
    schedule.enter(inc, 0, perform_command, (cmd,inc))

def CirculeGo(cmd, inc=60):
    schedule.enter(0, 0, perform_command, (cmd,inc))
    schedule.run()

#1、打开 https://pypi.python.org/pypi/APScheduler/2.1.2
#２、下载　https://pypi.python.org/pypi?:action=show_md5&digest=6862959d460c16ef325d63e1fc3a6684
#3、解压APScheduler-2.1.2.tar.gz
#4、cmd进入该目录，执行setup.py install


from apscheduler.scheduler import Scheduler

sched = Scheduler()
sched.daemonic = False

def job_function(text):
    print text

from datetime import datetime


#在某个时刻执行该任务
job = sched.add_date_job(job_function, datetime(2014, 03, 26, 00, 20, 00), ['Hello World'])

sched.start()

CirculeGo('type d:\\123.txt',10)



