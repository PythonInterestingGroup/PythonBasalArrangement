
'counting time'

__author__ = "JKangTan"


import functools
import time
import sys

def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		s = time.time()
		result = func(*args, **kw)
		e = time.time()
		print("%s"%func.__name__,"cost time:%.10f"%(e-s))
		return result
	return wrapper

@log
def test():
	pass
if __name__ == "__main__":
	test()