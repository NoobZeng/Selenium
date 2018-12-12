#!/usr/bin/env python
#! _*_ coding:utf-8 _*_
# @TIME   : 2018/11/30  23:27
# @Author : Noob
# @File   : mixed_os_grid.py

from selenium import webdriver
import unittest
import warnings
import sys

class SearchTest(unittest.TestCase):

    # 默认平台名称、默认浏览器名称、默认远程ip及端口号
    PLATFORM = 'WINDOWS'
    BROWSER = 'internet explorer'
    nodeURL = '192.168.0.103:8091'

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        desired_caps = dict()
        desired_caps['platform'] = self.PLATFORM
        desired_caps['browserName'] = self.BROWSER
        self.driver = webdriver.Remote(command_executor='http://' + self.nodeURL + '/wd/hub', desired_capabilities=desired_caps)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://www.baidu.com')

    def tearDown(self):
        print('end')
        self.driver.close()

    def test_search(self):
        self.driver.find_element_by_id('kw').send_keys('大角虫 Lily')
        self.driver.find_element_by_id('su').click()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        SearchTest.BROWSER = sys.argv.pop()
        SearchTest.PLATFORM = sys.argv.pop()
        SearchTest.nodeURL = sys.argv.pop()
    unittest.main(verbosity=2)