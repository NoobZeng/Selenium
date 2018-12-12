# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/7  18:05
# @Author : Noob
# @File   : appium_xpath.py

from appium import webdriver
import unittest
import warnings
import time

class Xpath(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        print('start')
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '5.1',
            'deviceName': 'Y15QKCP7226TB',
            'appPackage': 'com.baidu.yuedu',
            'appActivity': '.splash.SplashActivity',
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)

    def testXpath(self):
        print('……test……')
        # appium v1.5以上的版本通过name定位会报错
        # go_btn = self.driver.find_element_by_name('选好了')
        go_btn = self.driver.find_element_by_xpath('//*[@text="选好了"]')
        print(go_btn.text)
        go_btn.click()
        time.sleep(5)

        self.driver.find_element_by_accessibility_id('图书').click()
        self.driver.find_element_by_accessibility_id('小说').click()
        self.driver.find_element_by_id('com.baidu.yuedu:id/cb_choose_view').click()
        self.driver.find_element_by_id('com.baidu.yuedu:id/tv_confirm_button').click()
        time.sleep(5)

        fenlei_btn = self.driver.find_element_by_xpath('//android.widget.TextView[@text="分类"]')
        print(fenlei_btn)
        fenlei_btn.click()
        time.sleep(5)

    def tearDown(self):
        print('end')
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)