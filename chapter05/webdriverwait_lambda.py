#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/11/23  17:54
# @Author : Noob
# @File   : webdriverwait_lambda.py

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.implicitly_wait(30)
driver.maximize_window()
driver.get('https://account.weibo.com/set/iframe?skin=skin048')

# 登录
user_field = driver.find_element_by_xpath('//*[@id="loginname"]')
user_field.clear()
user_field.send_keys('xxx')
password_field = driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input')
password_field.clear()
password_field.send_keys('xxx')
driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()

modify_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="pl_content_account"]/div[1]/form/fieldset/div')))
modify_button.click()
# driver.find_element_by_xpath('//*[@id="pl_content_account"]/div[1]/form/fieldset/div').click()

realname_path = '//*[@id="pl_content_account"]/div[1]/div[2]/div/div[4]/div[3]/input'
WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(realname_path).get_attribute('class') == 'W_input W_input_focus')

driver.quit()
