# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/14  19:26
# @Author : Noob
# @File   : basepage.py

"""
Project:基础类BasePage，封装所有页面都公用的方法；
定义open函数，重定义find_element,switch_frame,send_keys等函数；
在初始化方法中定义驱动driver,基本url，title；
WebDriverWait提供了显示等待方式；
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import yaml
import csv
import xlrd

class BasePage(object):

    """
    1. 初始化driver、url、pagetitle等；
    2. 实例化BasePage类时，最先执行的就是__init__方法，该方法的入参，其实就是BasePage类的入参；
    3. __init__方法不能有返回值，只能返回None；
    4. self指实例本身，相较于类BasePage而言
    """

    def __init__(self, browser_driver, base_url, pagetitle):
        self.driver = browser_driver
        self.base_url = base_url
        self.pagetitle = pagetitle

    """
    1. 通过title断言进入的页面是否正确；
    2. 使用title获取当前窗口title，检查输入的title是否在当前title中，返回比较结果（True or False）
    """
    def on_page(self, pagetitle):
        return pagetitle in self.driver.title

    """
    1. 打开页面，并校验页面链接是否加载正确
    2. 以单下划线_开头的方法，在使用import *时，该方法不会被导入，保证该方法为类私有的；
    """
    def _open(self, url, pagetitle):
        # 使用get打开访问链接地址
        self.driver.get(url)
        self.driver.maximize_window()
        # 使用assert进行校验，打开的窗口title是否与配置的title一致。调用on_page方法。
        assert self.on_page(pagetitle), u'打开页面失败%s' % url

    # 定义open方法，掉用_open()进行打开链接
    def open(self):
        self._open(self.base_url, self.pagetitle)

    # 重写元素定位方法
    def find_element(self, *loc):
        # return self.driver.find_element(*loc)
        try:
            # 确保元素是可见的；
            # 注意：以下入参为元祖的元素，需要加*。Python存在这种特性，就是讲入参放在元祖里；
            # WebDriverWait(self.driver, 10).untli(lamba driver: driver.find_element(*loc).is_displayed())
            # 注意：以下入参本身是元祖，不需要加*
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print(u'%s 页面中未能找到%s元素' % (self, loc))

    # 重写switch_frame方法
    def switch_frame(self, loc):
        loc = self.find_element(loc)
        return self.driver.switch_to.frame(loc)

    # 定义scrip方法，用于执行js脚本，范围执行结果
    def scirpt(self, src):
        self.driver.execute_script(src)

    # 重写定义send_keys方法
    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            # getattr相当于实现self.loc
            loc = getattr(self, '_%s' % loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print(u'%s页面中未能找到%s元素' % (self, loc))

    # 重写截图
    def screenshot(self, loc):
        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        try:
            # 获取当前脚本的路径
            cwd_path = os.path.dirname(os.path.realpath(__file__))
            # self.__class__.__name__：当前运行文件的类名
            screenshot_path = os.path.join(cwd_path, 'screenshot_' + self.__class__.__name__)
            # 判断放置运行测试脚本的截图文件夹是否存在，如果不存在则创建
            if not os.path.exists(screenshot_path):
                os.makedirs(screenshot_path)
                print('截图目录新建成功：%s' % screenshot_path)
            else:
                print('该目录已存在！')
            error_text = self.find_element(*loc).text
            if 'Incorrect' in error_text:
                self.driver.get_screenshot_as_file(screenshot_path + '\\' + picture_time + '.png')
        except BaseException as msg:
            print('新建截图目录失败：%s' % msg)

    # 外部数据
    def get_data(self, filename):
        cwd_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(cwd_path, 'data\\' + filename)
        try:
            assert os.path.isfile(file_path), filename
        except AssertionError as msg:
            if filename == '':
                list_data = (['000', '000'], ['111', '111'])
                return list_data
            else:
                print('该文件不存在：%s' % msg)
        if file_path.endswith('.txt'):
            f = open(file_path, 'r', encoding='utf-8')
            cfg = f.readlines()
            cfg.remove(cfg[0])
            rows = []
            for i in cfg:
                i = i.split(',')
                i[1] = i[1].rstrip('\n')
                rows.append(i)
            return rows
        elif file_path.endswith('.csv'):
            cfg = csv.reader(open(file_path, 'r', encoding='utf-8'))
            next(cfg, None)
            rows = []
            for i in cfg:
                rows.append(i)
            return rows
        elif file_path.endswith('.xlsx'):
            book = xlrd.open_workbook(file_path)
            sheet = book.sheet_by_index(0)
            rows = []
            for idx in range(1, sheet.nrows):
                i = sheet.row_values(idx, 0, sheet.ncols)
                rows.append(i)
            rows[1][0] = int(rows[1][0])
            rows[1][1] = int(rows[1][1])
            return rows
        elif file_path.endswith('.yaml'):
            f = open(file_path, 'r', encoding='utf-8')
            cfg = yaml.load(f)
            f.close()
            cfg.remove(cfg[0])
            return cfg
        else:
            return '不能使用该类型的文件！'

if __name__ == '__main__':
    bp = BasePage(None, None, None)
    i = bp.get_data('data')
    print(i)