#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

try:
	path = '../20170622/'
	fileName = 'exer_error.py'
	f = open(path+fileName,'r')
	print('path:%s'%path)
	print('----------------------------%s-----------------------------'%fileName)
	print(f.read())
	print('----------------------------END-----------------------------')
except IOError as e:
	print('expert:',e)
finally:
	if f:
		f.close()
	
# 简洁写法
path = '/Users/ursus/Desktop/Python/Github/PythonBasalArrangement/exercise/20170613/'
fileName = 'exer_enum.py'
with open(path+fileName,'r') as f:
	print('path:%s'%path)
	print('----------------------------%s-----------------------------'%fileName)
	exer_enum = f.read()
	print(exer_enum)
	print('----------------------------END-----------------------------')
	
# 二进制文件
path = '/Users/ursus/Desktop/Python/Github/Resource/PythonResource/image/'
fileName = '001.png'
with open(path+fileName,'rb') as f:
	print('path:%s'%path)
	print('----------------------------%s-----------------------------'%fileName)
	print(f.read())
	print('----------------------------END-----------------------------')
	
# 写文件
path = '/Users/ursus/Desktop/Python/Github/PythonBasalArrangement/exercise/20170630/'
fileName = 'test.txt'
with open(path+fileName,'w') as f:
	f.write(exer_enum)