import json
import subprocess
import platform
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import os

def ping(host, n):
    param = '-n'
    if platform.system() == 'Windows':
        param = '-n'
    else:
        param = '-c'
    order = "ping " + param + ' ' + str(n) + ' ' + host
    ret = subprocess.run(order, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, encoding='gbk')
    return ret.returncode == 0


def start_ruijie():
    order = "../Ruijie Supplicant/RuijieSupplicant.exe"
    subprocess.run(order, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, encoding='gbk')


def job():
    global run_times
    run_times = run_times + 1
    mode = 'a+'
    if run_times % 10 == 0:
        run_times = 0
        mode = 'w'
    with open('./log.txt', mode, encoding='gbk') as file:
        file.write(datetime.datetime.now().strftime('%H:%M:%S ') + ' 第 ' + str(run_times) + ' 次调用成功\n')
        
    if ping('1.1.1.1', 1) == False:
        start_ruijie()


def main():
    # 定时执行 job 函数
    job()
    scheduler = BlockingScheduler(timezone='Asia/Shanghai')
    scheduler.add_job(job, "interval", hours=1)
    scheduler.start()


if __name__ == '__main__':
    run_times = 0
    main()