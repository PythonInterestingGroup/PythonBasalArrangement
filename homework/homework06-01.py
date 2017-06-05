# _*_  coding: utf-8 _*_

import functools
import time
import sys

def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		s = time.time()
		func(*args, **kw)
		e = time.time()
		print("%s"%func.__name__,"time :%.10f"%(e-s))
	return wrapper

@log
def test():
	pass

test()

s = time.time()
test()
e = time.time()
print('time:%.10f'%(e-s))