#!/usr/bin/env python
#! _*_ coding:utf-8 _*_
# @TIME   : 2018/11/22  19:16
# @Author : Noob
# @File   : alert_test.py

import unittest
from selenium import webdriver
import time
import os

class AlertTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('E:\\program\Python37\Scripts\chromedriver-2.43.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('https://www.douban.com/group/jiaoluoyinyue/')
        print(self.driver.title)

    def tearDown(self):
        self.driver.quit()

    def login(self, user, password):
        self.driver.find_element_by_xpath('//*[@id="db-global-nav"]/div/div[1]/a[1]').click()

        userfield = self.driver.find_element_by_xpath('//*[@id="email"]')
        userfield.clear()
        userfield.send_keys(user)

        passfield = self.driver.find_element_by_xpath('//*[@id="password"]')
        passfield.clear()
        passfield.send_keys(password)

        # 验证码通过手动登陆（屏蔽掉该功能，或者识别出该验证码）
        time.sleep(10)

        self.driver.find_element_by_xpath('//*[@id="lzform"]/div[7]/input').submit()


    def test_alert(self):
        self.login('xxx', 'xxx')

        # 点击加入小组按钮
        # self.driver.find_element_by_xpath('//*[@id="group-info"]/div/div').click()

        # 验证是否加入成功
        # msg = self.driver.find_element_by_xpath('//*[@id="group-info"]/div/div').text
        # self.assertTrue('我是这个小组的成员' in msg)

        # 点击退出小组按钮
        self.driver.find_element_by_xpath('//*[@id="group-info"]/div/div/a').click()

        # 获取alert弹窗并返回实例：driver.switch_to.alert
        # 绝对不能写成driver.switch_to.alert()
        # 报错：TypeError: 'Alert' object is not callable
        alert = self.driver.switch_to.alert

        # 获取警告窗口的文本：alert.text
        alert_text = alert.text

        print(alert_text)
        self.assertEqual('真的要退出小组?', alert_text)

        # 驳回JavaScript警告信息，单击取消按钮：alert.dismiss()
        alert.dismiss()

        # 验证是否驳回成功
        msg = self.driver.find_element_by_xpath('//*[@id="group-info"]/div/div').text
        self.assertTrue('我是这个小组的成员' in msg)

        # 接受JavaScript警告信息，单击OK按钮：alert.accept()
        self.driver.find_element_by_xpath('//*[@id="group-info"]/div/div/a').click()
        self.driver.switch_to.alert.accept()

        # 验证是否接受成功
        msg = self.driver.find_element_by_xpath('//*[@id="group-info"]/div/div').text
        self.assertFalse('我是这个小组的成员' in msg)

    def test_prompt(self):
        self.driver.get('file:///' + os.path.abspath('alert_prompt.html'))
        self.driver.find_element_by_xpath('/html/body/button').click()
        alert = self.driver.switch_to.alert
        text_value = 'noob'
        alert.send_keys(text_value)
        alert.accept()

        # 验证信息时是否正确
        out_text = self.driver.find_element_by_id('demo').text
        self.assertEqual('你好 ' + text_value + '! 今天感觉如何?', out_text)


if __name__ == '__main__':
    unittest.main(verbosity=2)