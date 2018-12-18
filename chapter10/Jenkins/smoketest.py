#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/11/4  22:10
# @Author : Noob
# @File   : smoketest.py

import unittest
from Selenium.chapter10.Jenkins.searchtest_modify import SearchTests
from Selenium.chapter10.Jenkins.sina_test import SinaTest
from xmlrunner import xmlrunner

search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
sina_tests = unittest.TestLoader().loadTestsFromTestCase(SinaTest)

# smoke_tests = unittest.TestSuite([search_tests,sina_tests])
smoke_tests = unittest.TestSuite()
smoke_tests.addTest(search_tests)
smoke_tests.addTest(sina_tests)

# unittest.TextTestRunner(verbosity=2).run(smoke_tests)
xmlrunner.XMLTestRunner(verbosity=2, output='test-reports').run(smoke_tests)