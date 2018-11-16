#!/usr/bin/env python
#! _*_ coding:utf-8 _*_
# @TIME   : 2018/11/9  16:52
# @Author : Noob
# @File   : test02.py

from selenium import webdriver
import unittest

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('start')
        cls.driver = webdriver.Chrome('E:\program\Python37\Scripts\chromedriver-2.43.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get('http://192.168.30.185:8011/index/index.html')
        cls.driver.title

    def test01(self):
        "测试0201"
        print("执行测试用例0201")

    def test02(self):
        "测试0202"
        print("执行测试用例0202")

    @classmethod
    def tearDownClass(cls):
        print('end')
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)