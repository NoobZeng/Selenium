# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/6  17:43
# @Author : Noob
# @File   : appium_api_swipe.py

# 上滑
def swipeUp(driver, t=3000, n=1):
    s = driver.get_window_size()

    # x坐标（上滑时x坐标不变）
    x = s['width'] * 0.5
    # 起点y坐标
    ys = s['height'] * 0.75
    # 重点y坐标
    ye = s['height'] * 0.25
    for i in range(n):
        driver.swipe(x, ys, x, ye, t)

# 下滑
def swipeDown(driver, t=3000, n=1):
    s = driver.get_window_size()

    x = s['width'] * 0.5
    ys = s['height'] * 0.25
    ye = s['height'] * 0.75
    for i in range(n):
        driver.swipe(x, ys, x, ye, t)

# 左滑
def swipeLeft(driver, t=3000, n=1):
    s = driver.get_window_size()

    xs = s['width'] * 0.75
    xe = s['width'] * 0.25
    y = s['height'] * 0.5
    for i in range(n):
        driver.swipe(xs, y, xe, y, t)

# 右滑
def swipeRight(driver, t=3000, n=1):
    s = driver.get_window_size()

    xs = s['width'] * 0.25
    xe = s['width'] * 0.75
    y = s['height'] * 0.5
    for i in range(n):
        driver.swipe(xs, y, xe, y, t)