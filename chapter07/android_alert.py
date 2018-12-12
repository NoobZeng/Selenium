# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/9  13:24
# @Author : Noob
# @File   : android_alert.py

from appium import webdriver
import warnings
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class AndroidAlert(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        print('start')
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '5.1',
            'deviceName': 'Y15QKCP7226TB',
            'appPackage': 'com.sankuai.meituan',
            'appActivity': 'com.meituan.android.pt.homepage.activity.Welcome',
            'automationName': 'Uiautomator2',
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            'noReset': True
        }
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                                       desired_capabilities=desired_caps)

    def always_allow(self, driver, number=5):
        """
        function:权限弹窗-始终允许
        :param driver:
        :param number:默认弹窗数量为5个
        :return:
        WebDriverWait：1s超时，0.5秒判断一次
        """
        for i in range(number):
            loc = (By.XPATH, '//*[@text="始终允许"]')
            try:
                el = WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located(loc))
                el.click()
            except:
                pass

    def testAlways(self):
        print('……test……')
        time.sleep(3)
        self.always_allow(self.driver, 5)

    def tearDown(self):
        print('end')
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)