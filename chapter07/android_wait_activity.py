# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/6  19:38
# @Author : Noob
# @File   : android_wait_activity.py

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
            'platformVersion': '5.1',
            'deviceName': '127.0.0.1:62001',
            'appPackage': 'com.baidu.yuedu',
            'appActivity': '.splash.SplashActivity',
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)

    def testActivity(self):
        print('……test……')
        # 进入可滑动页面
        self.driver.find_element_by_accessibility_id('图书').click()
        self.driver.find_element_by_accessibility_id('小说').click()
        self.driver.find_element_by_id('com.baidu.yuedu:id/cb_choose_view').click()
        self.driver.find_element_by_id('com.baidu.yuedu:id/tv_confirm_button').click()
        # time.sleep(5)
        print(self.driver.current_activity)
        ca = self.driver.current_activity
        # 如果使用time.sleep(5)，那么无论该元素是否加载出来都必须等待五秒
        # self.driver.find_element_by_id('com.baidu.yuedu:id/btn_cancel').click()

        # 这里改用wait_activity等待页面的activity加载，这样就不用再规定时间之后才能开始进行下一步操作
        self.driver.wait_activity(ca, 30)
        self.driver.find_element_by_id('com.baidu.yuedu:id/btn_cancel').click()

    def tearDown(self):
        print('end')
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)