# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/14  15:02
# @Author : Noob
# @File   : fourth_noddt.py

import os
import xlrd
from selenium import webdriver

cwd_path = os.path.dirname(os.path.realpath(__file__))
xlsx_path = os.path.join(cwd_path, 'fourth_data.xlsx')
book = xlrd.open_workbook(xlsx_path)
sheet = book.sheet_by_index(0)
for i in range(1, sheet.nrows):
    print(sheet.row_values(i, 0, sheet.ncols))
    driver = webdriver.Chrome('E:\program\Python37\Scripts\chromedriver-2.43.exe')
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://www.baidu.com')
    driver.find_element_by_id('kw').send_keys(sheet.row_values(i, 0, sheet.ncols)[0])
    driver.find_element_by_id('su').click()
    lists = driver.find_elements_by_partial_link_text('百度百科')
    print(len(lists))
    if len(lists) == int(sheet.row_values(i, 0, sheet.ncols)[1]):
        print('Actual = Expected')
    else:
        print('Actual != Expected')
    driver.quit()