#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'A module that calculates the execution time of a method'

__author__ = 'Ursus'

import functools
import time

def cal_method_times(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		t1 = time.time()
		f = func(*args,**kw)
		t2 = time.time()
		print("method < %s >"%func.__name__,"execute with time:",round((t2-t1) * 1000,2),"ms")
		return f
	return wrapper

@cal_method_times	
def _test():
	print("I'm test method")
	for i in range(1000000):
		pass
	
if __name__ == '__main__':
	_test()
	
