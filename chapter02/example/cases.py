#!/usr/bin/env python
#! _*_ coding:utf-8 _*_
# @TIME   : 2018/11/14  18:59
# @Author : Noob
# @File   : cases.py

import os
import unittest
import HTMLTestRunner

def allcase():
    case_dir = os.getcwd()
    discover = unittest.defaultTestLoader.discover(case_dir, pattern='test*.py', top_level_dir=None)
    return discover

def runcases(file_name):
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(allcase())
    fp = open(file_name, 'wb+')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='自动化测试unittest测试框架报告',
        description='用例执行情况：'
    )
    runner.run(allcase())
    fp.close()

if __name__ == '__main__':
    runcases(os.getcwd() + '\example.html')