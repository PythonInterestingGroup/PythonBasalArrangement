#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

print('OS NAME:',os.name)
print('-----------------------------------------------------------')
print(os.uname())
print('-----------------------------------------------------------')
print(os.environ)
print('-----------------------------------------------------------')
print(os.environ.get('PATH'))
print('----------------------当前目录绝对路径------------------------')
print(os.path.abspath('.'))
print('-----------------------------------------------------------')
os.mkdir(os.path.join(os.path.abspath('.'), 'temp'))
os.rmdir(os.path.join(os.path.abspath('.'), 'temp'))

filename = '/Users/ursus/Desktop/Python/Github/PythonBasalArrangement/exercise/20170613/exer_enum.py'
print(os.path.split(filename))