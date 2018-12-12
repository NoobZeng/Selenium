#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/11/23  18:45
# @Author : Noob
# @File   : webdriverwait_conditions.py

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import unittest
import os

class ExConditions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('E:\\program\Python37\Scripts\chromedriver-2.43.exe')
        self.driver.maximize_window()
        self.driver.get('https://account.weibo.com/set/iframe?skin=skin048')

    def tearDown(self):
        self.driver.quit()

    def login(self, user, password):
        user_field = self.driver.find_element_by_xpath('//*[@id="loginname"]')

        # 清除文本框或者文本域的内容：element.clear()
        user_field.clear()

        # 模拟输入文本：element.send_keys(*value)
        user_field.send_keys(user)

        password_field = self.driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input')
        password_field.clear()
        password_field.send_keys(password)

        # 单击元素：element. click()
        self.driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()

    def test_conditions(self):
        self.login('xxx', 'xxx')

        # 判断某个元素是否可见. 可见代表元素非隐藏，并且元素的宽和高都不等于0
        # WebDriverWait(driver, time).until(EC.visibility_of_element_located(locator)
        # locator:一组，（by, locator)
        e_xpath = '//*[@id="pl_content_account"]/div[1]/form/fieldset/div'
        edit_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, e_xpath)))
        edit_button.click()

        # 判断某个元素中是否可见并且是enable的，以便确定元素是可点击的。此方法返回定位到的元素
        # WebDriverWait(driver, time).until(EC.element_to_be_clickable(locator))
        # locator:一组(by, locator)
        hm_xpath = '//*[@id="pl_content_account"]/div[1]/div[2]/div/div[8]/div[3]/div/select/option[3]'
        print(self.driver.find_element_by_xpath(hm_xpath).is_displayed())
        print(self.driver.find_element_by_xpath(hm_xpath).is_enabled())
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, hm_xpath))).click()

        # 判断某个元素是否被选中了,一般用在下拉列表：WebDriverWait(driver, time).until(EC.element_to_be_selected(element)
        # element：是个WebElement
        # hm_xpath_other = '//*[@id="pl_content_account"]/div[1]/div[2]/div/div[8]/div[3]/div/select/option[8]'
        subsciption = self.driver.find_element_by_xpath(hm_xpath)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_selected(subsciption))

        # 判断是否至少有1个元素存在于dom树中
        # 举个例子，如果页面上有n个元素的class都是‘column-md-3‘，那么只要有1个元素存在，这个方法就返回True
        # WebDriverWait(driver, time).until(EC.presence_of_all_elements_located(locator))
        # locator:一组(by, locator)
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'btns')))

        self.driver.find_element_by_xpath(e_xpath).click()

        # 判断某个元素是否被加到了dom树里，并不代表该元素一定可见
        # WebDriverWait(driver, time).until(EC.presence_of_element_located(locator))
        # locator:一组(by, locator)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'woman_radio')))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, 'woman_radio')))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'woman_radio'))).click()
        woman_radio = self.driver.find_element_by_id('woman_radio')
        WebDriverWait(self.driver, 10).until(EC.element_to_be_selected(woman_radio))

        # 判断某个元素中的text是否 包含 了预期的字符串
        # WebDriverWait(driver, time).until(EC.text_to_be_present_in_element(locator, text))
        # locator:一组(by, locator)，即定位方法
        # text:期望的值
        locator = (By.XPATH, '//*[@id="pl_content_account"]/div[1]/div[1]/div[2]/div[2]')
        text = '笙囚'
        print(EC.text_to_be_present_in_element(locator, text))
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(locator, text))

        # 判断当前页面的title是否包含预期字符串，返回布尔值
        # WebDriverWait(driver, time).until(EC.title_contains(title))
        # title:期望的模糊title
        print(EC.title_contains('个人资料'))
        WebDriverWait(self.driver, 10).until(EC.title_contains('个人资料'))

        # 判断当前页面的title是否完全等于（==）预期字符串，返回布尔值
        # WebDriverWait(driver, 10).until(EC.title_is(title))
        # title:期望的精确title
        print(EC.title_is('个人资料页个人信息'))
        WebDriverWait(self.driver, 10).until(EC.title_is('个人资料页个人信息'))

        # 判断某个元素是否可见. 可见代表元素非隐藏，并且元素的宽和高都不等于0
        # WebDriverWait(driver, 10).until(EC.visibility_of(element)
        # element：是个WebElement
        visibility_element = self.driver.find_element_by_id('pl_content_account')
        print(EC.visibility_of(visibility_element))
        WebDriverWait(self.driver, 10).until(EC.visibility_of(visibility_element))

        # 判断某个元素中是否不存在于dom树或不可见
        # WebDriverWait(driver,10).until(EC.invisibility_of_element_located(locator)
        # locator:一组（by, locator)
        print(EC.invisibility_of_element_located((By.ID, 'btns')))
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.ID, 'btns')))

        # 判断页面上是否存在alert
        # WebDriverWait(driver, 10).until(EC.alert_is_present())
        self.driver.get('file:///' + os.path.abspath('alert_prompt.html'))
        self.driver.find_element_by_xpath('/html/body/button').click()
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        print(alert.text)
        alert.dismiss()

if __name__ == '__main__':
    unittest.main(verbosity=2)