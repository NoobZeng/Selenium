# !/usr/bin/env python
# ! _*_ coding:utf-8 _*_
# @TIME   : 2018/12/10  14:53
# @Author : Noob
# @File   : test.py

import os
import sys
import yaml

cwd_path = os.path.dirname(os.path.realpath(sys.argv[0]))
yaml_path = os.path.join(cwd_path, 'pageelement/OpenPage.yaml')

f = open(yaml_path, 'r', encoding='utf-8')
cfg = f.read()

d = yaml.load(cfg)
print(type(d))
print(d)