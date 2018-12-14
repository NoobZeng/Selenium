# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/13  19:28
# @Author : Noob
# @File   : third_ddt.py

from selenium import webdriver
import unittest
import os
from ddt import ddt, data, unpack

def get_data(file_name):
    cwd_path = os.path.dirname(os.path.realpath(__file__))
    txt_path = os.path.join(cwd_path, file_name)
    f = open(txt_path, 'r', encoding='utf-8')
    cfg = f.readlines()
    f.close()
    cfg.remove(cfg[0])
    data_list = []
    for i in cfg:
        i = i.split(',')
        # i[1] = i[1].replace('\n', '')
        i[1] = i[1].rstrip('\n')
        data_list.append(i)
    return data_list

@ddt
class SearchTest(unittest.TestCase):

    def setUp(self):
        print('……test……')
        self.driver = webdriver.Chrome('E:\program\Python37\Scripts\chromedriver-2.43.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get('https://www.baidu.com/')

    @data(*get_data('third_data.txt'))
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