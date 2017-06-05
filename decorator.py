#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'time count'

__author__ = 'roni'


import functools
import time

import sys

'''
print(sys.version)
print(sys.getdefaultencoding())
print('我得到的'.encode('utf-8'))
'''

'''
def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('begin call')
		return func(*args, **kw)
	return wrapper

@log
def new():
	print("end call")

f = new

print(new.__name__)
print(f.__name__)

# 装饰器”（Decorator）: 在代码运行期间动态增加功能的方式 => 本质上，decorator就是一个返回函数的高阶函数

f()


def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wapper(*args, **kw):
			print("begin call")
		    return func(*args, **kw)
		return wrapper
'''



def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		b = time.time()
		func(*args, **kw)
		e = time.time()
		r = e-b
		print("%s" % func.__name__,"use time:%.10f" % r)
	return wrapper

'''
@log
def funcTime(des):
	print(des)

funcTime("i zui shuai")
'''

#log(funcTime)()

'''
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单
int2 = functools.partial(int, base = 2)
print(int2('10'))
'''

'''
print("========")

b = time.time()
funcTime()
e = time.time()
r = e-b
print("%s" % funcTime.__name__,"use time:%.10f" % r)
'''

if __name__ == '__main__':
	log(func)