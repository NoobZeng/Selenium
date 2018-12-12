# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/6  17:38
# @Author : Noob
# @File   : appium_api_swipe_test.py

from appium import webdriver
import unittest
import warnings
import time
import chapter07.appium_api_swipe as SA

class TestSwipe(unittest.TestCase):

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

    def testSwipe(self):
        print('……test……')

        # 进入可滑动页面
        self.driver.find_element_by_accessibility_id('图书').click()
        self.driver.find_element_by_accessibility_id('小说').click()
        self.driver.find_element_by_id('com.baidu.yuedu:id/cb_choose_view').click()
        self.driver.find_element_by_id('com.baidu.yuedu:id/tv_confirm_button').click()
        time.sleep(5)
        self.driver.find_element_by_id('com.baidu.yuedu:id/btn_cancel').click()

        # flick 从一点滑动到另一点
        self.driver.flick(360, 960, 360, 320)
        time.sleep(5)

        # swipe开始滑动
        SA.swipeUp(self.driver, n=2)
        SA.swipeLeft(self.driver, n=2)
        time.sleep(10)

        # driver.drag_and_drop(origin_el, destination_el) 将origin元素拖到destination元素

        # 模拟手势点击坐标
        # 导航栏：女生
        self.driver.tap([(516,132), (620,228)], 500)
        time.sleep(5)
        # 分类按钮
        self.driver.tap([(599,64), (690,112)], 500)
        time.sleep(5)

    def tearDown(self):
        print('end')
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)