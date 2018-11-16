#!/usr/bin/env python
#! _*_ coding:utf-8 _*_
# @TIME   : 2018/11/15  16:57
# @Author : Noob
# @File   : by_element.py

from selenium import webdriver
import unittest
import utx

class ByElement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('start')
        cls.driver = webdriver.Chrome('E:\program\Python37\Scripts\chromedriver-2.43.exe')
        cls.driver.get('https://www.baidu.com/')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        print(cls.driver.title)

    def test_by_id(self):
        u'id定位'
        by_id = self.driver.find_element_by_id('kw')
        self.assertEqual('255', by_id.get_attribute('maxlength'))

    def test_by_name(self):
        u'name定位'
        by_name = self.driver.find_element_by_name('wd')
        self.assertTrue(by_name.get_attribute('maxlength') == '255')

    def test_by_class(self):
        u'class定位'
        by_class = self.driver.find_element_by_class_name('s_ipt')
        self.assertTrue(by_class.is_enabled())

    def test_by_tag(self):
        u'tag定位'
        by_tag = self.driver.find_elements_by_tag_name('input')
        self.assertEqual(15, len(by_tag))

    def test_by_xpath(self):
        u'xpath定位'
        by_xpath = self.driver.find_element_by_xpath('//*[@id="u1"]/a[5]')
        self.assertTrue(by_xpath.is_displayed())
        by_xpath.click()
        self.assertFalse('百度一下，你就知道' == self.driver.title)

    def test_by_css(self):
        u'CSS选择器定位'
        self.driver.back()
        by_css_f = self.driver.find_element_by_css_selector('#kw')
        by_css_s = self.driver.find_element_by_css_selector('input.s_ipt')
        self.assertTrue(by_css_f == by_css_s)

    def test_by_link(self):
        u'Link定位'
        by_link = self.driver.find_element_by_link_text('贴吧')
        self.assertTrue(by_link.is_displayed())

    def test_by_links(self):
        u'PartialLink定位'
        by_links = self.driver.find_elements_by_partial_link_text('百度')
        self.assertEqual(4, len(by_links))

    @classmethod
    def tearDownClass(cls):
        print('end')
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)