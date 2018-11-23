#!/usr/bin/env python
#! _*_ coding:utf-8 _*_
# @TIME   : 2018/11/19  19:29
# @Author : Noob
# @File   : webelement_interface.py

from selenium import webdriver
import unittest

class WebElement(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # 无浏览器的测试
        # option = webdriver.ChromeOptions()
        # option.add_argument('headless')
        # driver = webdriver.Chrome(
        #           chrome_options=option, executable_path='E:\\program\Python37\Scripts\chromedriver-2.43.exe')

        cls.driver = webdriver.Chrome('E:\\program\Python37\Scripts\chromedriver-2.43.exe')
        cls.driver.get('https:www.baidu.com')
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_size(self):
        u'获取元素大小'
        search_field = self.driver.find_element_by_id('kw')
        # 获取元素大小：size
        # 获取元素宽度：size['width']
        # 获取元素高度
        print(search_field.size['height'])
        self.assertEqual(22, search_field.size['height'])

    def test_tag_name(self):
        u'获取元素的HTML标签名称'
        search_field = self.driver.find_element_by_id('kw')
        print(search_field.tag_name)
        self.assertFalse('button' == search_field.tag_name)

    def test_text(self):
        u'获取元素的文本值'
        link_button = self.driver.find_element_by_id('cp')
        print(link_button.text)
        self.assertTrue('2018' in link_button.text)

if __name__ == '__main__':
    unittest.main(verbosity=2)