# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/14  23:02
# @Author : Noob
# @File   : logintestcase.py

from .basetestcase import BaseTestCase
from .loginpage import LoginPage
from ddt import ddt, data, unpack

@ddt
class LoginTestCase(BaseTestCase):

    # @data(*(['xxx', 'xxx'], [111, 111]))
    @data(*LoginPage(None, None, None).test_data())
    @unpack
    def test_login(self, userfiled, password):
        # 声明LoginPage类对象
        login_page = LoginPage(self.driver, self.url, u'GitHub')
        # 调用打开页面组件
        login_page.open()
        # 打开登录框
        login_page.click_login()
        # 调用用户名输入组件
        login_page.input_username(userfiled)
        # 调用密码输入组件
        login_page.input_password(password)
        # 调用登录按钮组件
        login_page.click_dologin()
        login_page.show_span()

if __name__ == '__main__':
    BaseTestCase.unittest.main(verbosity=2)