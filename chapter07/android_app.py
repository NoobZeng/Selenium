#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/3  23:43
# @Author : Noob
# @File   : android_web_actual.py

from appium import webdriver
import unittest
import time
import warnings

class AndroidWeb(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        print('start')
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '5.1',
            'deviceName': '127.0.0.1:62001',
            'appPackage': 'com.taobao.taobao',
            'appActivity': 'com.taobao.tao.welcome.Welcome',
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)

    def test_web(self):
        print('test……')
        # 等待页面加载
        time.sleep(5)
        self.driver.find_element_by_id('com.taobao.taobao:id/home_searchedit').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.taobao.taobao:id/searchEdit').click()
        self.driver.find_element_by_id('com.taobao.taobao:id/searchEdit').send_keys('猫')
        time.sleep(3)

    def tearDown(self):
        print('end')
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)