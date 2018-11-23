#!/usr/bin/env python
#! _*_ coding:utf-8 _*_
# @TIME   : 2018/11/16  13:41
# @Author : Noob
# @File   : webdriver_principle.py

from selenium import webdriver
import re
import time
from selenium.common.exceptions import TimeoutException

# 打开浏览器
# driver = webdriver.Chrome('E:\program\Python37\Scripts\chromedriver-2.43.exe')

# 不打开浏览器的测试
option = webdriver.ChromeOptions()
option.add_argument("headless")
# headles：在Chrome在headless模式下运行；
# disable-gpu：作用是针对现有bug的work around；
# remote-debugging-port=9222：作用则是允许我们可以在另外一个浏览器中debug；
# option.add_argument('--headless')
# option.add_argument('--disable-gpu')
# option.add_argument('--remote-debugging-port=9222')
driver = webdriver.Chrome(chrome_options=option, executable_path='E:\program\Python37\Scripts\chromedriver-2.43.exe')

# 窗口最大化
# driver.maximize_window()

# 输入网址
driver.get('https://www.baidu.com/')
driver.get('https://www.weibo.com/')

# 设置一个页面完全加载完成的超时等待时间
driver.set_page_load_timeout(5)

# 设置脚本执行的超时时间，应该在execute_async_script抛出错误之前
driver.set_script_timeout(10)

# 捕获超时异常
'''
try:
    driver.get('https://sohu.com')
except TimeoutException:
        print('Message: Timed out waiting for page to load.')
        # 当页面加载时间超过设定时间，通过执行Javascript来stop加载，即可执行后续动作
        driver.execute_script('window.stop()')
'''

driver.implicitly_wait(10)
# 向后退
# driver.back()
# 向前进
# driver.forward()
# 刷新页面
# driver.refresh()

# 获取坐标位置
print('坐标位置：%s' %driver.get_window_position())

# 设置浏览器坐标
driver.set_window_position(x=200, y=300)
print('新坐标位置：%s' %driver.get_window_position())

# 获取x轴位置
print('x轴位置：%s' %driver.get_window_position()['x'])

# 获取y轴位置
print('y轴位置：%s' %driver.get_window_position()['y'])

# 获取浏览器窗体的大小
print('浏览器窗体的大小：%s' %driver.get_window_size())

# 获取浏览器的宽度
print('浏览器的宽度：%s' %driver.get_window_size()['width'])

# 获取浏览器的高度
print('浏览器的高度：%s' %driver.get_window_size()['height'])

# 设置浏览器窗体的大小
driver.set_window_size(100, 200)
print('设置好的浏览器窗体大小：%s' %driver.get_window_size())

# 获取当前页面的URL地址：current_url
print('当前页面的URL地址：' + driver.current_url)

# 获取当前窗口的句柄：current_window_handle
print('当前窗口的句柄：' + driver.current_window_handle)

# 获取该实例底层的浏览器名称：name
print('该实例底层的浏览器名称：' + driver.name)

# 获取当前设备的方位：orientation（暂时不知道怎么使用）
# print(driver.orientation)

# 获取当前页面的标题：title
print('当前页面的标题：' + driver.title)

# 获取当前session里所有窗口的句柄：window_handles
print('当前session里所有窗口的句柄：%s' %driver.window_handles)

# 获取当前页面的源代码：page_source
# print(driver.page_source)

pageSource = driver.page_source
if 'weibo' in pageSource:
    print('源码中有weibo')
else:
    print('源码中没有weibo')
pattern = re.compile(r'href = \"(.*?)\"')
print(pattern.findall(pageSource))

# 返回当前页面唯一焦点所在的元素或者元素体：switch_to.active_element
print(driver.switch_to.active_element)
#   switch_to.active_element后不带括号
#   driver.find_element_by_id('kw').click().switch_to.active_element.send_keys('hello')

# 把焦点切换至当前页面弹出的警告：switch_to.alert()
#   driver.switch_to.alert()

# 切换焦点至默认框架内（或说：切换到最上层页面）：switch_to.default_content()
#   driver.switch_to.default_content()

# 通过索引、名称和王爷元素将焦点切换到指定的框架，这种方法也适用于IFRAMES：switch_to.frame(frame_reference)
#   frame_reference：要切换的目标窗口的名称‘整数类型的索引或者要切换的目标框架的网页元素
#   driver.switch_to.frame('frame_name')

# 切换焦点到指定的窗口：switch_to.window(window_name)
#   window_name：要切换的目标窗口的名创或者句柄
#   driver.switch_to.window('main')

driver.quit()