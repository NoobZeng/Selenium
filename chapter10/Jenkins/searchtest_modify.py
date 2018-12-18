# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/10/29  21:23
# @Author : Noob
# @File   : searchtest_modify.py

import unittest
from selenium import webdriver
import os

class SearchTests (unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Chrome session
        cls.driver = webdriver.Chrome('E:\program\Python37\Scripts\chromedriver-2.43.exe')
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to the application home page
        cls.driver.get('https://www.baidu.com/')
        cls.driver.title

    def test_search_by_category(self):
        self.search_field = self.driver.find_element_by_id('kw')
        self.search_field.clear()
        self.search_field.send_keys('大角虫')
        self.search_field.submit()
        products = self.driver.find_elements_by_partial_link_text('漫画')
        self.assertEqual(12, len(products))
        self.driver.get_screenshot_as_file(os.getcwd() + '\cartoon.png')

    def test_search_by_name(self):
        self.search_field = self.driver.find_element_by_name('wd')
        self.search_field.clear()
        self.search_field.send_keys('Lily')
        self.search_field.submit()
        products = self.driver.find_elements_by_xpath('//th/a[contains(text(),"漫画")]')
        self.assertEqual(4,len(products))

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()