# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/9  0:31
# @Author : Noob
# @File   : wechat.py

from appium import webdriver
import unittest
import warnings
import time

class WechatTest(unittest.TestCase):

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
            'chromeOptions': {'androidProcess': 'com.tencent.mm:toolsmp'}
        }
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)
        self.driver.implicitly_wait(10)

    def testWechat(self):
        print('……test……')
        self.driver.find_element_by_accessibility_id('搜索').click()
        time.sleep(3)
        self.driver.find_element_by_id('com.tencent.mm:id/ji').send_keys('yoyoketang')
        time.sleep(3)
        self.driver.find_element_by_id('com.tencent.mm:id/ok').click()
        time.sleep(3)

        # 进入公众号中有webview的页面
        id_text = 'resourceId("com.tencent.mm:id/aiu").text("精品分类")'
        self.driver.find_element_by_android_uiautomator(id_text).click()
        time.sleep(2)

        # context切换
        contexts = self.driver.contexts
        print(contexts)
        print(self.driver.current_context)
        self.driver.switch_to.context('WEBVIEW_com.tencent.mm:toolsmp')
        print(self.driver.current_context)
        time.sleep(3)

        # 点击webview上的元素
        # 这里会报错：找不到元素
        # self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]').click()
        # time.sleep(3)
        # 打印出来的源码中找不到要点击的元素
        print(self.driver.page_source)

        # 这里打印出来发现只有一个handle，所以不是这里的问题，所以切换webview；
        handles = self.driver.window_handles
        print(handles)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]').click()
        time.sleep(3)

        # 打印对应元素下的内容；
        lists = self.driver.find_elements_by_css_selector('.title.js_title')
        for i in lists:
            print(i.text)

    def tearDown(self):
        print('end')
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)