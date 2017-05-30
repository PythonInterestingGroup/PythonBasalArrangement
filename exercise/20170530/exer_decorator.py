# -*- coding: utf-8 -*-
from functools import reduce
import functools
import time

def func_v1(n) :
    print(reduce(lambda x,y : x + y, [i * 2 + 1 for i in range(n)]))
	

print(func_v1.__name__,"(10000):")
func_v1(10000)

def log(func):
	def wrapper(*args, **kw) :
		print('call %s():'%func.__name__)
		return func(*args, **kw)
	return wrapper
	
def log_v2(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print(func.__name__,"begin")
		f = func(*args,**kw)
		print(func.__name__,"end")
		return f
	return wrapper  
	
def log_v3(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		t1 = time.time()
		f = func(*args,**kw)
		t2 = time.time()
		print(func.__name__,"execute with time:",round((t2-t1) * 1000,2),"ms")
		return f
	return wrapper
	
@log
def func_v2(m):
	func_v1(m)

@log_v2
def func_v3(m):
	func_v1(m)

@log_v3
def func_v4(m):
	func_v1(m)

func_v2(10000)
print(func_v3.__name__)
func_v3(10000)

func_v4(10000000)