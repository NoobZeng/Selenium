# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/8  12:12
# @Author : Noob
# @File   : android_uiautomator.py

from appium import webdriver
import unittest
import warnings
import time

class UiautomatorTest(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        print('start')
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '5.1',
            'deviceName': 'Y15QKCP7226TB',
            'appPackage': 'com.baidu.yuedu',
            'appActivity': '.splash.SplashActivity',
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                                       desired_capabilities=desired_caps)

    def testUiautomator(self):
        print('……test……')
        # 前面的操作手动进行
        time.sleep(10)

        # 1. id+text属性组合
        id_text = 'resourceId("com.baidu.yuedu:id/tv_search").text("搜索")'
        id_text_tag = self.driver.find_element_by_android_uiautomator(id_text).tag_name
        print('1. id+text：%s'%id_text_tag)

        # 2. class+text属性组合
        class_text = 'className("android.widget.TextView").text("搜索")'
        class_text_tag = self.driver.find_element_by_android_uiautomator(class_text).tag_name
        print('2. class+text：%s'%class_text_tag)

        # 3. id+class属性组合
        id_class = 'resourceId("com.baidu.yuedu:id/tv_search").className("android.widget.TextView")'
        id_class_tag = self.driver.find_element_by_android_uiautomator(id_class).tag_name
        print('3. id+class：%s'%id_class_tag)

        # 4. class+description属性组合
        desc_text = 'className("android.widget.FrameLayout").description("前往购物车")'
        desc_text_tag = self.driver.find_element_by_android_uiautomator(desc_text).tag_name
        print('4. class+description：%s'%desc_text_tag)

        # 5. 父子定位childSelector
        son = 'resourceId("com.baidu.yuedu:id/mti_online").childSelector(className("android.widget.LinearLayout").index(4))'
        son_tag = self.driver.find_element_by_android_uiautomator(son).tag_name
        print('5. childSelector：%s'%son_tag)

        # 6. 兄弟定位fromParent
        brother = 'resourceId("com.baidu.yuedu:id/rl_shop_card").fromParent(text("分类"))'
        brother_text = self.driver.find_element_by_android_uiautomator(brother).text
        print('6. fromParent：%s'%brother_text)

        # 7. text
        print('7. ' + self.driver.find_element_by_android_uiautomator('text("搜索")').text)

        # 8. textContains
        print('8. ' + self.driver.find_element_by_android_uiautomator('textContains("免费")').text)

        # 9. textStartWith
        print('9. ' + self.driver.find_element_by_android_uiautomator('textStartsWith("免")').text)

        # 10. textMatches
        # print('10. ' + self.driver.find_element_by_android_uiautomator('textMatches("女")').text)

        # 11. classNameMatches
        self.driver.find_element_by_android_uiautomator('classNameMatches(".*TextView$").text("女生")').click()

        self.driver.back()
        time.sleep(2)

        # 12. resourceIdMatches
        self.driver.find_element_by_android_uiautomator('resourceIdMatches(".*id/iv_yuedu_classify$")').click()

    def tearDown(self):
        print('end')
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)