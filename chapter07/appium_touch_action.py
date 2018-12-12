# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/7  19:55
# @Author : Noob
# @File   : appium_touch_action.py

from appium import webdriver
import unittest
import warnings
import time
import chapter07.appium_api_swipe as SA
from appium.webdriver.common.touch_action import TouchAction

class TouchTest(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        print('start')
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '5.1',
            'deviceName': 'Y15QKCP7226TB',
            'appPackage': 'com.tencent.mobileqq',
            'appActivity': 'com.tencent.mobileqq.activity.SplashActivity',
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)

    def testTouch(self):
        print('……test……')

        # 进入qq手势锁页面
        time.sleep(30)
        self.driver.wait_activity(self.driver.current_activity, 30, 2)
        self.driver.find_element_by_xpath('//android.widget.Button[@text="登 录"]').click()
        self.driver.find_element_by_accessibility_id('请输入QQ号码或手机或邮箱').send_keys('xxx')
        self.driver.find_element_by_accessibility_id('密码 安全').send_keys('xxx')
        self.driver.find_element_by_accessibility_id('登录').click()
        time.sleep(10)
        SA.swipeRight(self.driver, t=800, n=1)
        self.driver.find_element_by_accessibility_id("设置").click()
        self.driver.find_element_by_xpath('//android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//android.widget.TextView[@content-desc="未设置"]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//android.widget.Button[@text="创建手势密码"]').click()
        time.sleep(10)

        # 开始定位手势锁九宫格
        jiu = 'resourceId("com.tencent.mobileqq:id/name").index(5)'
        loc = self.driver.find_element_by_android_uiautomator(jiu).location
        print('获取手势锁位置：%s'%loc)
        s = self.driver.find_element_by_android_uiautomator(jiu).size
        print('获取手势锁宽和高：%s'%s)

        # 给九个格编号
        # s['width'] == s['height']
        offset = s['width']/6
        print(offset)
        g11 = (None, loc['x'] + offset, loc['y'] + offset)
        g12 = (None, loc['x'] + offset*3, loc['y'] + offset)
        g13 = (None, loc['x'] + offset*5, loc['y'] + offset)
        g21 = (None, loc['x'] + offset, loc['y'] + offset*3)
        g22 = (None, loc['x'] + offset*3, loc['y'] + offset*3)
        g23 = (None, loc['x'] + offset*5, loc['y'] + offset*3)
        g31 = (None, loc['x'] + offset, loc['y'] + offset*5)
        g32 = (None, loc['x'] + offset*3, loc['y'] + offset*5)
        g33 = (None, loc['x'] + offset*5, loc['y'] + offset*5)
        g = [g11, g12, g13, g21, g22, g23, g31, g32, g33]
        print(g)

        def pianyi(a, b):
            """计算a点到b点的偏移量"""
            x = g[b][1]-g[a][1]
            y = g[b][2]-g[a][2]
            r = (None, x, y)
            return r

        ta = TouchAction(self.driver)
        # x=168, y=492
        ta.press(x=loc['x'] + offset, y=loc['y'] + offset).wait(2000)
        # x=360, y=492
        ta.move_to(x=offset*2, y=0).wait(2000)
        # x=552, y=492
        ta.move_to(x=offset*2, y=0).wait(2000)
        # x=360, y=684
        ta.move_to(x=-offset*2, y=offset*2).wait(2000)
        # x=168, y=876
        ta.move_to(x=-offset*2, y=offset*2).wait(2000)
        # x=360, y=876
        ta.move_to(x=offset*2, y=0).wait(2000)
        # x=552, y=876
        ta.move_to(x=offset*2, y=0).wait(2000)
        ta.release().perform()

        time.sleep(5)

    def tearDown(self):
        print('end')
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)