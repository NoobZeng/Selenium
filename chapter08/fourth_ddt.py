# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/14  14:14
# @Author : Noob
# @File   : fourth_ddt.py.py

from selenium import webdriver
from ddt import ddt, data, unpack
import os
import xlrd
import unittest

def get_data(filename):
    cwd_path = os.path.dirname(os.path.realpath(__file__))
    xlsx_path = os.path.join(cwd_path, filename)
    rows = []
    book = xlrd.open_workbook(xlsx_path)
    sheet = book.sheet_by_index(0)
    for row_idx in range(1, sheet.nrows):
        rows.append(sheet.row_values(row_idx, 0, sheet.ncols))
        for row in rows:
            row[1] = int(row[1])
    return rows

@ddt
class SearchTest(unittest.TestCase):

    def setUp(self):
        print('……test……')
        self.driver = webdriver.Chrome('E:\program\Python37\Scripts\chromedriver-2.43.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('https://www.baidu.com/')

    @data(*get_data('fourth_data.xlsx'))
    @unpack
    def testSearch(self, search_value, expected_bool):
        self.driver.find_element_by_id('kw').send_keys(search_value)
        self.driver.find_element_by_id('su').click()
        lists = self.driver.find_elements_by_partial_link_text('百度百科')
        self.assertEqual(int(expected_bool), len(lists))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)