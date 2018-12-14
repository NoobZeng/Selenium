# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/13  22:59
# @Author : Noob
# @File   : third_noddt.py

from selenium import webdriver
import os

print('start')

cwd_path = os.path.dirname(os.path.realpath('__file__'))
txt_path = os.path.join(cwd_path, 'third_data.txt')
cfg = open(txt_path, 'r', encoding='utf-8').readlines()
cfg.remove(cfg[0])
for i in cfg:
    i = i.split(',')
    i[1] = i[1].rstrip('\n')
    print(i)
    driver = webdriver.Chrome('E:\program\Python37\Scripts\chromedriver-2.43.exe')
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://www.baidu.com')
    driver.find_element_by_id('kw').send_keys(i[0])
    driver.find_element_by_id('su').click()
    lists = driver.find_elements_by_partial_link_text('百度百科')
    print(len(lists))
    if len(lists) == int(i[1]):
        print('Actual = Expected')
    else:
        print('Actual != Expected')
    driver.quit()