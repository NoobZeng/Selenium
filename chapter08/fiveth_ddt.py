# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/14  15:13
# @Author : Noob
# @File   : fiveth_ddt.py

from selenium import webdriver
from ddt import ddt, data, unpack
import unittest
import csv
import xlrd
import os
import yaml

def get_data(filename):
    cwd_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(cwd_path, filename)

    if file_path.endswith('.txt'):
        f = open(file_path, 'r', encoding='utf-8')
        cfg = f.readlines()
        cfg.remove(cfg[0])
        rows = []
        for i in cfg:
            i = i.split(',')
            i[1] = int(i[1].rstrip('\n'))
            rows.append(i)
        return rows
    elif file_path.endswith('.csv'):
        f = open(file_path, 'r', encoding='utf-8')
        cfg = csv.reader(f)
        next(cfg, None)
        rows = []
        for i in cfg:
            i[1] = int(i[1])
            rows.append(i)
        return rows
    elif file_path.endswith('.xlsx' or '.xls'):
        book = xlrd.open_workbook(file_path)
        sheet = book.sheet_by_index(0)
        rows = []
        for row_idx in range(1, sheet.nrows):
            rows.append(sheet.row_values(row_idx, 0, sheet.ncols))
            for i in rows:
                i[1] = int(i[1])
        return rows
    elif file_path.endswith('.yaml'):
        cfg = yaml.load(open(file_path, 'r', encoding='utf-8'))
        cfg.remove(cfg[0])
        return cfg

@ddt
class SearchTest(unittest.TestCase):

    def setUp(self):
        print('……test……')
        self.driver = webdriver.Chrome('E:\program\Python37\Scripts\chromedriver-2.43.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('https://www.baidu.com/')

    @data(*get_data('five_data.yaml'))
    @unpack
    def testSearch(self, search_value, expected_bool):
        self.driver.find_element_by_id('kw').send_keys(search_value)
        self.driver.find_element_by_id('su').click()
        lists = self.driver.find_elements_by_partial_link_text('百度百科')
        self.assertEqual(expected_bool, len(lists))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)