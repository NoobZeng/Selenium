# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/12  19:08
# @Author : Noob
# @File   : second_ddt.py

from selenium import webdriver
from ddt import ddt, data, unpack
import unittest
import csv
import os

def get_data(file_name):
    rows = []
    cwd_path = os.getcwd()
    data_path = os.path.join(cwd_path, file_name)
    data_file = open(data_path, 'r', encoding='utf-8')
    reader = csv.reader(data_file)
    # 跳过首行
    next(reader, None)
    for row in reader:
        rows.append(row)
    return rows

@ddt
class SearchDDT(unittest.TestCase):

    def setUp(self):
        print('start')
        self.driver = webdriver.Chrome(executable_path='E:\program\Python37\Scripts\chromedriver-2.43.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('https://www.baidu.com/')

    @data(*get_data('second_data.csv'))
    @unpack
    def testSearch(self, search_value, expected_bool):
        print('……test……')
        self.driver.find_element_by_id('kw').send_keys(search_value)
        self.driver.find_element_by_id('su').click()
        lists = self.driver.find_elements_by_partial_link_text('百度百科')
        self.assertEqual(int(expected_bool), len(lists))

    def tearDown(self):
        print('end')
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)