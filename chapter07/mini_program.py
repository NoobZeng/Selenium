# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/10  20:32
# @Author : Noob
# @File   : mini_program.py

"""摩拜单车"""

from appium import webdriver
import unittest
import warnings
import time

class MiniProgram(unittest.TestCase):

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
            'noReset': True,
            'chromeOptions': {'androidProcess': 'com.tencent.mm:appbrand0'}
        }
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                                       desired_capabilities=desired_caps)
        self.driver.implicitly_wait(10)

    def swipeDown(self, driver, t=3000, n=2):
        '''向下滑动屏幕'''
        l = driver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.25  # 起始y坐标
        y2 = l['height'] * 0.75  # 终点y坐标
        for i in range(n):
            driver.swipe(x1, y1, x1, y2, t)

    def testWechat(self):
        print('……test……')
        time.sleep(5)
        # 下滑
        self.swipeDown(self.driver)
        time.sleep(2)
        # 点开小程序
        self.driver.find_elements_by_id('com.tencent.mm:id/uq')[0].click()
        time.sleep(4)

        time.sleep(3)
        # 点击小头像，通过tap
        self.driver.tap([(582,1011), (720,1149)], 3000)
        time.sleep(2)

        # 点击我的钱包
        self.driver.find_element_by_android_uiautomator('className("android.view.View").text("我的钱包")').click()
        time.sleep(3)


    def tearDown(self):
        print('end')
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)