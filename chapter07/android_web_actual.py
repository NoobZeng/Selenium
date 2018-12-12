#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/3  23:43
# @Author : Noob
# @File   : android_web_actual.py

from selenium import webdriver
import unittest
import time
import warnings

class AndroidWeb(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        print('start')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        desired_caps = dict()
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'Y15QKCP7226TB'
        desired_caps['browserName'] = 'Chrome'
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps, options=chrome_options)
        self.driver.get('http://weibo.com')
        time.sleep(10)

    def testWeb(self):
        print('test……')

    def tearDown(self):
        print('end')
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)