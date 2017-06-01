import functools
import time

import sys

print(sys.version)
print(sys.getdefaultencoding())
print('我得到的'.encode('utf-8'))

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

#@log
def funcTime():
	pass

#funcTime()

log(funcTime)()

