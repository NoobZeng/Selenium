# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/14  22:07
# @Author : Noob
# @File   : loginpage.py

from selenium.webdriver.common.by import By
from Selenium.chapter08.page_object.basepage import BasePage

# 继承BasePage类
class LoginPage(BasePage):
    # 定位器，通过元素属性定位元素对象
    login_loc = (By.CSS_SELECTOR, 'a[href="/login"]')

    username_loc = (By.ID, 'login_field')
    password_loc = (By.ID, 'password')
    dologin_loc = (By.XPATH, "//input[@name='commit']")
    span_loc = (By.XPATH, "//div[@class='flash flash-full flash-error']/div")
    filename = 'data.yaml'

    # 操作
    # 通过集成覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法
    # 打开网页
    def open(self):
        # 调用page中的_open打开链接
        self._open(self.base_url, self.pagetitle)

    # 点击登录，打开登录iframe
    def click_login(self):
        self.find_element(*self.login_loc).click()

    # 输入用户名：调用send_keys对象，输入用户名
    def input_username(self, username):
        # self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    # 输入密码：调用send_keys对象，输入密码
    def input_password(self, password):
        # self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    # 点击登录
    def click_dologin(self):
        self.find_element(*self.dologin_loc).click()

    # 用户名或密码不合理提示
    def show_span(self):
        el = self.driver.find_elements(*self.span_loc)
        if len(el) != 0:
            self.shot_screen()
            return self.find_element(*self.span_loc).text
        else:
            pass

    # 截图
    def shot_screen(self):
        self.screenshot(self.span_loc)

    def test_data(self):
        return self.get_data(self.filename)

if __name__ == '__main__':
    lp = LoginPage(browser_driver=None, base_url=None, pagetitle=None)
    print(lp.test_data())