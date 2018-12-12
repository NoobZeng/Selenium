# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/8  14:43
# @Author : Noob
# @File   : adb_shell.py

import os
import time

class AdbShell:

    """常用keyevent事件"""
    KEYCODE_HOME = 3
    KEYCODE_MENU = 82
    KEYCODE_BACK = 4
    KEYCODE_POWER = 26
    KEYCODE_DPAD_UP = 19
    KEYCODE_DPAD_DOWN = 20
    KEYCODE_DPAD_LEFT = 21
    KEYCODE_DPAD_RIGHT = 22
    KEYCODE_NOTIFICATION = 83

    def adbKeyEvent(self, keyname):
        """执行keyevent事件"""
        shell_key = 'adb shell input keyevent %s'%keyname
        os.system(shell_key)

    def adbText(self, text):
        """向当前页面文本框输入text文本内容"""
        shell_text = 'adb shell input text %s'%text
        os.system(shell_text)

if __name__ == '__main__':

    # tap命令启动百度阅读
    shell_tap1 = 'adb shell input tap 600 600'
    os.system(shell_tap1)

    time.sleep(10)

    # tap命令打开分类页面
    shell_tap2 = 'adb shell input tap 650 100'
    os.system(shell_tap2)

    time.sleep(3)

    # swipe命令上滑分类页面
    shell_swipe = 'adb shell input swipe 200 200 200 -400'
    os.system(shell_swipe)

    time.sleep(3)

    # 执行back键操作
    adbs = AdbShell()
    adbs.adbKeyEvent(adbs.KEYCODE_BACK)

    time.sleep(3)

    os.system('adb shell input tap 200 100')

    adbs.adbText('what')