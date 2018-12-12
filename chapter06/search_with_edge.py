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
        warnings.simplefilter('ignore', ResourceWarning)
        desired_caps = DesiredCapabilities.EDGE.copy()
        desired_caps['platform'] = 'WINDOWS'
        desired_caps['version'] = '10'
        # self.driver = webdriver.Remote('http://localhost:8089/wd/hub', desired_caps)
        self.driver = webdriver.Remote(command_executor='http://localhost:8089/wd/hub', desired_capabilities=desired_caps)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
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