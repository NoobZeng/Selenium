# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/16  16:17
# @Author : Noob
# @File   : first_action_chains.py

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import unittest
import time

class ActionChainsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('E:\program\Python37\Scripts\chromedriver-2.43.exe')
        driver = self.driver
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get('https://www.baidu.com/')

    def testActionChains(self):
        driver = self.driver
        el_filed = driver.find_element_by_id('kw')
        el_button = driver.find_element_by_id('su')
        el_mv = driver.find_element_by_id('u')
        el_music = driver.find_element_by_xpath("//div[@class='s_tab_inner']/a[5]")
        ac = ActionChains(driver)
        ac.send_keys('Lily')
        ac.send_keys(Keys.CONTROL, 'a')
        ac.click(el_button)
        ac.move_to_element(el_mv)
        ac.send_keys_to_element(el_filed, '大角虫')
        ac.move_to_element(el_music)
        ac.context_click(el_music)
        ac.perform()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
