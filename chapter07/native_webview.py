# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/5  17:13
# @Author : Noob
# @File   : native_webview.py

from appium import webdriver
import unittest
import warnings
import time

class NativeWebview(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        print('start')
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '7.1',
            'deviceName': '127.0.0.1：62001',
            'appPackage': 'com.baidu.yuedu',
            'appActivity': '.splash.SplashActivity',
            'automationName': 'Uiautomator2',
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)

    def test_AW(self):
        print('……test……')
        self.driver.find_element_by_accessibility_id('图书').click()
        self.driver.find_element_by_accessibility_id('小说').click()
        self.driver.find_element_by_id('com.baidu.yuedu:id/cb_choose_view').click()
        self.driver.find_element_by_id('com.baidu.yuedu:id/tv_confirm_button').click()
        time.sleep(25)
        # 这里打印app环境
        print(self.driver.contexts)
        # contexts = self.driver.contexts
        # self.driver.switch_to.context(contexts[1])
        # print(self.driver.current_context)

    def tearDown(self):
        print('end')
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)