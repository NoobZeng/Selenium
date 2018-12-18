# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/17  20:56
# @Author : Noob
# @File   : search.py.py

from behave import *
import time

@given('百度搜索首页')
def step_homepage(context):
    context.driver.get('https://www.baidu.com/')

@when('搜索{text}')
def step_search(context, text):
    search_field = context.driver.find_element_by_id('kw')
    search_field.clear()
    search_field.send_keys(text)
    search_field.submit()

@then('返回搜索数据')
def step_dataresult(context):
    time.sleep(3)
    text_values = context.driver.find_elements_by_xpath("//a[contains(text(), 'Lily')]")
    assert len(text_values) > 0