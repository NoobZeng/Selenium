# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/17  1:15
# @Author : Noob
# @File   : third_cookie.py

from selenium import webdriver
import unittest
import time

class CookieTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('E:\program\Python37\Scripts\chromedriver-2.43.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def testGetCookies(self):
        driver = self.driver
        # 刚打开浏览器，此时当前会话没有cookie
        print(driver.get_cookies())
        driver.get('https://www.baidu.com/')
        time.sleep(2)
        # 打开页面后，可以获得一堆cookie
        print(driver.get_cookies())
        print('#################################################################')
        # 手动进入登录，查看登录后的cookie
        time.sleep(30)
        print(driver.get_cookies())

    def testGetCookie(self):
        driver = self.driver
        driver.get('https://www.12306.cn/')
        time.sleep(2)
        # 获取指定cookie
        print(driver.get_cookie(name='RAIL_DEVICEID'))

    def testDeleteCookie(self):
        driver = self.driver
        driver.get('https://www.baidu.com')
        time.sleep(2)
        # 手动进入登录，查看登录后的cookie
        time.sleep(30)
        print(driver.get_cookie(name='xxx'))
        # 清楚指定cookie
        driver.delete_cookie(name='xxx')
        # 删除后发现变成了未登录的状态
        time.sleep(5)
        driver.refresh()
        time.sleep(5)

    def testDeleteAllCookies(self):
        driver = self.driver
        driver.get('https://www.baidu.com')
        time.sleep(2)
        driver.delete_all_cookies()
        print(driver.get_cookies())

    def testAddCookie(self):
        driver = self.driver
        driver.get('https://www.baidu.com')
        # 手动登录
        time.sleep(30)
        driver.delete_cookie(name='xxx')
        print(driver.get_cookie(name='xxx'))
        driver.refresh()
        time.sleep(3)
        c = {'domain': '.baidu.com',
             'expiry': 1804184718.61591,
             'httpOnly': True,
             'name': 'xxx',
             'path': '/',
             'secure': False,
             'value': 'xxx'}
        driver.add_cookie(c)
        driver.refresh()
        time.sleep(5)
        print(driver.get_cookie('xxx'))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
