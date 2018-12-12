# -*- coding: utf-8 -*-

from chapter07.yaml import tool

yamls = tool.yamlElements()

def get_locater(clazz_name, method_name):
    locators = yamls[clazz_name]['locators']
    for locator in locators:
        if locator['name'] == method_name:
            return locator


class HomePage:
    搜索框 = get_locater('HomePage', '搜索框')
    输入内容框 = get_locater('HomePage', '输入内容框')
    删除文本框文字按钮 = get_locater('HomePage', '删除文本框文字按钮')
    搜索按钮 = get_locater('HomePage', '搜索按钮')

    
class LoginPage:
    选择账号登录 = get_locater('LoginPage', '选择账号登录')
    选择其他账号登录 = get_locater('LoginPage', '选择其他账号登录')
    选择账号密码登录 = get_locater('LoginPage', '选择账号密码登录')
    账号输入框 = get_locater('LoginPage', '账号输入框')
    密码输入框 = get_locater('LoginPage', '密码输入框')
    登录按钮 = get_locater('LoginPage', '登录按钮')

    
class MyPage:
    我的 = get_locater('MyPage', '我的')
    进入登录页面 = get_locater('MyPage', '进入登录页面')

    
class OpenPage:
    图书 = get_locater('OpenPage', '图书')
    小说 = get_locater('OpenPage', '小说')
    协议复选框 = get_locater('OpenPage', '协议复选框')
    提交按钮 = get_locater('OpenPage', '提交按钮')

if __name__ == '__main__':
    print(MyPage.我的)
    print(MyPage.我的['name'])
    print(MyPage.我的['type'])
    print(MyPage.我的['value'])