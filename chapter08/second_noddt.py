# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/13  19:00
# @Author : Noob
# @File   : second_noddt.py

from selenium import webdriver
import os
import csv

print('……test……')

cwd_path = os.path.dirname(os.path.realpath(__file__))
data_path = os.path.join(cwd_path, 'second_data.csv')
f = open(data_path, 'r', encoding='utf-8')
f_csv = csv.reader(f)
next(f_csv, None)
print(f_csv)
for i in f_csv:
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