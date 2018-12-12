# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/9  13:49
# @Author : Noob
# @File   : long_press.py

from appium import webdriver
import unittest
import warnings
import time
from appium.webdriver.common.touch_action import TouchAction

class LongpressTest(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        print('start')
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '5.1',
            'deviceName': 'Y15QKCP7226TB',
            'appPackage': 'com.tencent.mm',
            'appActivity': '.ui.LauncherUI',
            'automationName': 'Uiautomator2',
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'noReset': True
        }
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
        self.driver.implicitly_wait(10)

    def testWechat(self):
        print('……test……')

        # 选择聊天记录表中第一个记录长按
        el = self.driver.find_elements_by_id('com.tencent.mm:id/azj')[0]
        TouchAction(self.driver).long_press(el).perform()
        time.sleep(3)

    def tearDown(self):
        print('end')
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)