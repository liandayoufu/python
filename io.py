#!/usr/bin/env python
# coding = utf-8

import os
# shutil 模块提供copyfile()函数
import shutil

[ x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
['adv_func.py', 'excise.py', 'funcs.py', 'hello.py', 'oop.py', 'setup.py']