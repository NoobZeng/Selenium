# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/10  21:55
# @Author : Noob
# @File   : android_more.py

from appium import webdriver
import os
import sys
import yaml
import time
from tomorrow3 import threads

def get_desired_caps(devicesName='手机'):
    """
    从yaml读取desired_caps配置信息
    :param devicesName: 设备名称，如手机/夜神
    :return: desired_caps字典格式和port
    """
    cwd_path = os.path.dirname(os.path.realpath(sys.argv[0]))
    yaml_path = os.path.join(cwd_path, 'desiredcaps.yaml')
    print('配置地址：%s'%yaml_path)
    f = open(yaml_path, 'r', encoding='utf-8')
    d = f.read()
    f.close()
    cfg = yaml.load(d)
    for i in cfg:
        if devicesName in i['desc']:
            print(i)
            # 启动服务(嫌弃手工启动appium麻烦的入口，通过python启动appium服务）
            # start_appium(port=i['port'])
            return_args = (i['desired_caps'], i['port'])
            return return_args

@threads(2)
def run_app(devicesName):
    """
    运行app代码
    :param devicesName: 设备名称，如手机/夜神
    :return: None
    """
    # 配置参数
    desired_caps = get_desired_caps(devicesName)
    print(desired_caps)

    # 执行代码
    driver = webdriver.Remote('http://127.0.0.1:%s/wd/hub'%desired_caps[1], desired_caps[0])
    time.sleep(10)

    go_btn = driver.find_element_by_xpath('//*[@text="选好了"]')
    print(go_btn.text)
    go_btn.click()
    time.sleep(5)

    driver.find_element_by_accessibility_id('图书').click()
    driver.find_element_by_accessibility_id('小说').click()
    driver.find_element_by_id('com.baidu.yuedu:id/cb_choose_view').click()
    driver.find_element_by_id('com.baidu.yuedu:id/tv_confirm_button').click()
    time.sleep(5)
    driver.quit()

def start_appium(port=4723, uuid=''):
    a = os.popen('netstat -ano | findstr "%s"'%port)
    time.sleep(2)
    t1 = a.read()
    if 'LISTENING' in t1:
        # print('appium服务已经启动：%s'%t1)
        print('appium_start：%s' % t1)
    else:
        os.system('appium -a 127.0.0.1 -p %s -U %s --no-reset'%(port, uuid))

if __name__ == '__main__':
    devices = ['手机', '夜神']
    for n in devices:
        run_app(devicesName=n)