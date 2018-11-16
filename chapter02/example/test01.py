#!/usr/bin/env python
#! _*_ coding:utf-8 _*_
# @TIME   : 2018/11/8  22:38
# @Author : Noob
# @File   : test01.py

import unittest
from selenium import webdriver
import time
import os
from utx import *

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('开始测试')
        cls.driver = webdriver.Chrome('E:\program\Python37\Scripts\chromedriver-2.43.exe')
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get('https://weibo.com/')

    # 登陆
    def login(self, username, password):
        username_field = self.driver.find_element_by_id('loginname')
        username_field.clear()
        username_field.send_keys(username)
        passeord_field = self.driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input')
        passeord_field.clear()
        passeord_field.send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()

    # 判断元素是否存在
    def isElementExist(self, attr, value, xp):
        x = self.driver.find_element_by_xpath(xp)
        if x.get_attribute(attr) == value:
            return False
        elif x.get_attribute(attr) != value:
            return True

    def test_login_success(self):
        u"用户名和密码正确"
        self.login('xxx','xxx')
        time.sleep(10)
        name_text = self.driver.find_element_by_xpath('//*[@id="plc_top"]/div/div/div[3]/div[1]/ul/li[5]/a/em[2]').text
        self.assertEqual('xx',name_text)
        self.driver.get_screenshot_as_file(os.getcwd() + '\login_success.png')
        time.sleep(10)
        menu = self.driver.find_element_by_xpath("//em[@class='W_ficon ficon_set S_ficon']")
        menu.find_element_by_xpath("//li[@class='gn_func']/a")
        webdriver.ActionChains(self.driver).move_to_element(menu).perform()
        self.driver.find_element_by_xpath("//li[@class='gn_func']/a").click()

    def test_login_pwd_error(self):
        u"密码错误"
        self.login('xxx','pwderror')
        time.sleep(10)
        error_message = self.driver.find_element_by_xpath("//p[@class='main_txt']/span[2]").text
        flag = Test.isElementExist(self, 'src', 'about:blank', '//*[@id="pl_login_form"]/div/div[3]/div[3]/a/img')
        print(flag)
        if flag:
            self.assertIn('请填写验证码', error_message)
        else:
            self.assertIn('用户名或密码错误',error_message)
        self.driver.get_screenshot_as_file(os.getcwd() + '\login_pwd_error.png')

    def test_login_pwd_null(self):
        u'密码为空'
        time.sleep(10)
        self.login('xxx','')
        time.sleep(10)
        error_message = self.driver.find_element_by_xpath("//p[@class='main_txt']/span[2]").text
        flag = Test.isElementExist(self, 'src', 'about:blank', '//*[@id="pl_login_form"]/div/div[3]/div[3]/a/img')
        print(flag)
        if flag:
            self.assertIn('请输入验证码', error_message)
        else:
            self.assertIn('请输入密码', error_message)
        self.driver.get_screenshot_as_file(os.getcwd() + '\login_pwd_null.png')

    def test_login_user_error(self):
        u'用户名错误'
        self.driver.refresh()
        time.sleep(10)
        self.login('erroruser','xxx')
        time.sleep(10)
        error_message = self.driver.find_element_by_xpath("//p[@class='main_txt']/span[2]").text
        flag = Test.isElementExist(self, 'src', 'about:blank', '//*[@id="pl_login_form"]/div/div[3]/div[3]/a/img')
        print(flag)
        if flag:
            self.assertIn('请输入验证码', error_message)
        else:
            self.assertIn('用户名或密码错误', error_message)
        self.driver.get_screenshot_as_file(os.getcwd() + '\login_user_error.png')

    def test_login_user_null(self):
        u'用户名为空'
        time.sleep(10)
        self.login('','xxx')
        time.sleep(10)
        error_message = self.driver.find_element_by_xpath("//p[@class='main_txt']/span[2]").text
        flag = Test.isElementExist(self, 'src', 'about:blank', '//*[@id="pl_login_form"]/div/div[3]/div[3]/a/img')
        print(flag)
        if flag:
            self.assertIn('请输入登录名', error_message)
        else:
            self.assertIn('用户名或密码错误', error_message)
        self.driver.get_screenshot_as_file(os.getcwd() + '\login_user_null.png')

    @classmethod
    def tearDownClass(cls):
        print('结束测试')
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)