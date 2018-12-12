# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/10  16:20
# @Author : Noob
# @File   : tool.py

import os
import sys
import yaml
import jinja2

# os.path.dirname：去掉文件，获取路径（或者说返回上一级）
# os.path.realpath： 绝对路径
# sys.argv[0] == __file__: 相对路径
cwd_path = os.path.dirname(os.path.realpath(sys.argv[0]))
# 获取定位元素的yaml放置文件夹路径
page_path = os.path.join(cwd_path, 'pageelement')

def yamlElements():
    pageElements = dict()
    # os.walk()遍历yaml文件
    for root, dirs, files in os.walk(page_path):
        # 只读取放置yaml目录下的yaml文件
        for name in files:
            filename = os.path.join(root, name)
            if filename.endswith('.yaml'):
                f = open(filename, 'r', encoding='utf-8')
                d = f.read()
                cfg = yaml.load(d)
                pageElements.update(cfg)
    return pageElements

# 提取yaml数据
def get_page_list(yamlpage):
    """
    function: 把yaml对象转成需要的页面对象数据：页面对象-->list
    args:yaml解析的对象->dict类型
    :param yamlpage:
    :return:
    eg:
        {'HomePage':['城市选择','首页搜索'], 'MyPage':['我的','请点击登录']
    """
    page_object = dict()
    for page, names in yamlpage.items():
        loc_names = []
        # 获取所有的loctors定位方法
        locs = names['locators']
        # 添加定位name到列表
        for loc in locs:
            loc_names.append(loc['name'])
        page_object[page] = loc_names
    return page_object

# 生成pages文件
def create_pages_py(page_list):
    """
    function:用jinja2把templetpage模板生成pages.py文件
    args:传get_page_list返回的内容：
        eg:
            {'HomePage':['城市选择','首页搜索'],'MyPage':['我的','请点击登录]
    :param page_list:
    :return:None
    """
    print(os.path.join(cwd_path, 'templetpage'))
    templet_loader = jinja2.FileSystemLoader(searchpath=cwd_path)
    templet_env = jinja2.Environment(loader=templet_loader)

    templetVars = {
        'page_list': page_list
    }
    templet = templet_env.get_template('templetpage')
    f = open(os.path.join(cwd_path, 'pages.py'), 'w', encoding='utf-8')
    f.write(templet.render(templetVars))

if __name__ == '__main__':
    ye = yamlElements()
    for i in ye['HomePage']['locators']:
        print(i)
    create_pages_py(get_page_list(ye))