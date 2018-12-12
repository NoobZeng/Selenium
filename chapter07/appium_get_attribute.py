# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/6  22:05
# @Author : Noob
# @File   : appium_get_attribute.py

from appium import webdriver
import unittest
import warnings

class GetA(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        print('start')
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '5.1',
            'deviceName': '127.0.0.1:62001',
            'appPackage': 'com.baidu.yuedu',
            'appActivity': '.splash.SplashActivity',
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)

    def testGetAttribute(self):
        print('……test……')
        title = self.driver.find_element_by_id('com.baidu.yuedu:id/tv_title')
        # text属性
        title_text = title.text
        print('第一种text属性获取方法：%s' %title_text)
        # text属性另一种获取方法
        title_text = title.get_attribute('text')
        print('第二种text属性获取方法：%s' %title_text)
        # tag_name属性获取，实质上是获取class属性
        title_tag_name = title.tag_name
        print('tag_name=class属性获取：%s' %title_tag_name)
        # tag_name属性另一种获取方式
        title_tag_name = title.get_attribute('className')
        print('tag_name=class另一种获取方式：%s' %title_tag_name)
        # content-desc属性的获取
        tushu = self.driver.find_element_by_accessibility_id('图书')
        tushu_content_desc = tushu.get_attribute('name')
        print('content-desc属性获取：%s' %tushu_content_desc)
        tushu_content_desc = tushu.get_attribute('contentDescription')
        print('content-desc的另一种获取方式：%s' %tushu_content_desc)
        # 当content-desc属性值为空时获取的是text属性
        title_content_desc = title.get_attribute('name')
        print('当content-desc属性值为空时获取的是text属性：%s' %title_content_desc)
        # id属性获取
        title_id = title.get_attribute('resourceId')
        print('id属性获取：%s' % title_id)
        # 其他属性获取
        print('checkable:' + title.get_attribute('checkable'))
        print('clickable:' + title.get_attribute('clickable'))
        print('enabled:' + title.get_attribute('enabled'))
        # size属性获取
        title_size = title.size
        print('size属性的获取：%s' %title_size)
        # location属性获取
        title_location = title.location
        print('location属性获取：%s' %title_location)

    def tearDown(self):
        print('end')
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)