#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/11/27  17:38
# @Author : Noob
# @File   : search_with_firefox.py

from selenium import webdriver
import unittest
import warnings
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class SearchTest(unittest.TestCase):

    def setUp(self):
        print('start')
        warnings.simplefilter('ignore', ResourceWarning)
        # c_options = webdriver.ChromeOptions()
        # 解决远程机器是Linux系统下Chrome浏览器无法打开的问题
        # c_options.add_argument('no-sandbox')
        # 解决远程机器是Linux系统下浏览器最大化的问题
        # c_options.add_argument('start-maximized')
        desired_caps = dict()
        desired_caps['browserName'] = 'firefox'
        desired_caps['platform'] = 'WINDOWS'
        # desired_caps['version'] = '10'
        # self.driver = webdriver.Remote('http://localhost:8089/wd/hub', desired_caps)
        # self.driver = webdriver.Remote(command_executor='http://192.168.0.103:8089/wd/hub', desired_capabilities=desired_caps, options=c_options)
        self.driver = webdriver.Remote(command_executor='http://192.168.0.103:8090/wd/hub', desired_capabilities=desired_caps)
        self.driver.implicitly_wait(10)
        # self.driver.maximize_window()
        self.driver.get('http://www.baidu.com')

    def tearDown(self):
        print('end')
        self.driver.close()
        # self.driver.quit()

    def test_search(self):
        self.driver.find_element_by_id('kw').send_keys('大角虫 Lily')
        self.driver.find_element_by_id('su').click()

if __name__ == '__main__':
    unittest.main(verbosity=2)