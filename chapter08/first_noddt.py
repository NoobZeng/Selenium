# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/13  18:32
# @Author : Noob
# @File   : first_noddt.py

from selenium import webdriver

print('……test……')
test_data = [['大角虫', True], ['Lily love', False], ['SQ', True]]
for i in test_data:
    driver = webdriver.Chrome('E:\program\Python37\Scripts\chromedriver-2.43.exe')
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get('https://www.baidu.com')
    driver.find_element_by_id('kw').send_keys(i[0])
    driver.find_element_by_id('su').click()
    lists = driver.find_elements_by_partial_link_text('百度百科')
    expected_bool = (len(lists) >= 1)
    if expected_bool == i[1]:
        print('Actual = Expected')
    else:
        print('Actual != Expected')
    driver.quit()