#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/11/4  18:29
# @Author : Noob
# @File   : sina_test.py

from selenium import webdriver
import unittest
from selenium.common.exceptions import NoSuchElementException

class SinaTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('E:\program\Python37\Scripts\chromedriver-2.43.exe')
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get('https://weibo.com/')
        cls.driver.title

    def test_assert_username(self):
        print('第一个测试用例；')
        self.assertTrue(self.is_element_present('name', "username"))

    def test_assert_css(self):
        print('第二个测试用例；')
        self.assertTrue(self.is_element_present('css', 'a[href="/?category=10005"]'))

    def test_tanjiu_message(self):
        print('第三个测试用例；')
        search_field = self.driver.find_element_by_xpath('//*[@id="weibo_top_public"]/div/div/div[2]/input')
        search_field.clear()
        search_field.send_keys('坛九')
        self.driver.find_element_by_xpath('//*[@id="weibo_top_public"]/div/div/div[2]/a').click()
        search_weibo = self.driver.find_element_by_xpath('//*[@id="pl_feedlist_index"]/div[1]/div[2]/div[2]/div[1]/div[2]/p[1]').text
        self.assertEqual('恭喜我！', search_weibo)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

if __name__ == '__main__':
    unittest.main(verbosity=2)