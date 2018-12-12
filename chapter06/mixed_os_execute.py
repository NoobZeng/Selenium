#!/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/1  18:07
# @Author : Noob
# @File   : mixed_os_execute.py

import os

# 封装gridfunction
# 定义node_hub与浏览器对应关系
def grid():
    wr = [
        ['192.168.0.103:8091', 'WINDOWS', 'chrome'],
        ['192.168.0.103:8091', 'WINDOWS', 'firefox'],
        ['192.168.0.103:8091', 'WINDOWS', 'internet explorer'],
        ['192.168.0.103:8090', 'WINDOWS', 'chrome'],
        ['192.168.0.103:8090', 'WINDOWS', 'firefox']
    ]
    return wr

# os.system('python ' + os.getcwd() + '\mixed_os_grid.py 192.168.0.103:8091 WINDOWS chrome')
for grids in grid():
    nodeURL = grids[0]
    PLATFORM = grids[1]
    browserName = grids[2]
    os.system('python ' + os.getcwd() + '\mixed_os_grid.py ' + nodeURL + ' ' + PLATFORM + ' ' + browserName)