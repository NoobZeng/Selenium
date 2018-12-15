# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/14  22:58
# @Author : Noob
# @File   : basetestcase.py

from selenium import webdriver
import unittest
from ddt import ddt

@ddt
class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('E:\program\Python37\Scripts\chromedriver-2.43.exe')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.url = 'https://github.com/'

    def tearDown(self):
        self.driver.quit()