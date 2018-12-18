# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/17  21:42
# @Author : Noob
# @File   : click.py

from behave import *
import time
from selenium.webdriver.support import expected_conditions as EC

@given('首页')
def step_homepage(context):
    context.driver.get('https://www.baidu.com')

@when('点击贴吧')
def step_clicktieba(context):
    context.driver.find_element_by_xpath('//*[@id="u1"]/a[5]').click()

@then('返回数据')
def step_tiebareuslt(context):
    time.sleep(2)
    assert EC.title_is(context.driver.title)

@when('搜索贴吧{text}')
def step_search(context, text):
    el = context.driver.find_element_by_id('wd1')
    el.clear()
    el.send_keys(text)
    el.submit()

@then('返回数据{text}')
def step_result(context, text):
    els = context.driver.find_elements_by_xpath('//a[contains(text(), "lily")]')
    assert len(els) > int(text)