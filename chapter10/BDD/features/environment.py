# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/17  21:18
# @Author : Noob
# @File   : environment.py

from selenium import webdriver

def before_all(context):
    context.driver = webdriver.Chrome('E:\program\Python37\Scripts\chromedriver-2.43.exe')
    driver = context.driver
    driver.maximize_window()
    driver.implicitly_wait(10)

def after_all(context):
    context.driver.quit()