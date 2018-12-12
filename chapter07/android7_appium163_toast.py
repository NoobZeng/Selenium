# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/7  7:26
# @Author : Noob
# @File   : android7_appium163_toast.py

from appium import webdriver
import unittest
import warnings
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class ToastTest(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        print('start')
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '7.1',
            'deviceName': '127.0.0.1:62001',
            'appPackage': 'com.baidu.yuedu',
            'appActivity': '.splash.SplashActivity',
            'automationName': 'Uiautomator2',
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)

    def is_toast_exist(self, driver, text, timeout=30, poll_frequency=0.5):
        """is toast exist, return True or False
        :Args:
        :param driver:传driver
        :param text:toast的文本内容
        :param timeout:最大超时时间，默认为30s
        :param poll_frequency:间隔查询时间，默认0.5s查询一次
        :return:True or False
        :Usage:
        is_toast_exist(driver, 'toast文本')
        """
        try:
            toast_locator = ("xpath", ".//*[contains(@text,'%s')]" %text)
            WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_locator))
            return True
        except:
            return False

    def testToast(self):
        print('……test……')
        self.driver.find_element_by_accessibility_id('图书').click()
        self.driver.find_element_by_accessibility_id('小说').click()
        self.driver.find_element_by_id('com.baidu.yuedu:id/cb_choose_view').click()
        self.driver.find_element_by_id('com.baidu.yuedu:id/tv_confirm_button').click()

        time.sleep(10)

        # 等待当前页面加载，超过三十秒报错，每隔0.2秒看一次
        ca = self.driver.current_activity
        print(ca)
        self.driver.wait_activity(ca, 20)

        # 获取toast小弹框
        self.driver.back()

        # 定位toast元素
        # 这里是一组locator，元素在webview中，所以可以使用WebDriverWait的方式
        toast_locator = (By.XPATH, './/*[contains(@text,"再按一次退出")]')
        toast_el = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(toast_locator))
        print(toast_el)
        print(toast_el.text)

        # 验证封装的toast方法
        self.driver.back()
        print(self.is_toast_exist(self.driver, '再按一次退出'))

    def tearDown(self):
        print('end')
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)