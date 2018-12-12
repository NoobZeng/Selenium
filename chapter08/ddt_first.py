# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/11  22:29
# @Author : Noob
# @File   : ddt_first.py

from selenium import webdriver
from ddt import ddt, data, unpack
import unittest

@ddt
class SearchDDT(unittest.TestCase):

    def setUp(self):
        print('start')
        self.driver = webdriver.Chrome(executable_path='E:\program\Python37\Scripts\chromedriver-2.43.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('https://www.baidu.com/')

    @data(('怦然心跳', True), ('LilyLove', False))
    @unpack
    def testSearch(self, search_value, expected_bool):
        print('……test……')
        self.driver.find_element_by_id('kw').send_keys(search_value)
        self.driver.find_element_by_id('su').click()
        lists = self.driver.find_elements_by_partial_link_text('百度百科')
        self.assertEqual(expected_bool, len(lists) >= 1)

    def tearDown(self):
        print('end')
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)