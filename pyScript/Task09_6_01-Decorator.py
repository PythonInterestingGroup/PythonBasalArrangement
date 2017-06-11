#--*-- coding: utf-8 --*--
'''
The usage of decorator
'''
import time
from functools import wraps

def testTime(func):
	@wraps(func)
	def decorator(*args, **kw):
		t1 = time.time()
		test = func(*args, **kw)
		t2 = time.time()
		print '%s costs %s seconds' %(func.__name__, str(t2-t1))
		return test
	return decorator


@testTime
def random_sum(n):
	return sum([x for x in range(0, n)])

#@testTime
def sumList(m, n):
	return sum([x*y for x in range(0, m) for y in range(0, n)])

if __name__ == "__main__":
	#L = [12, 32, 43, 5, 0, -2, -56, 5, 57]
	#sumList(L)
	n = 10000000
	random_sum(n)

	j = 2000; k = 1000
	#sumList(j, k)
	sumList = testTime(sumList)
	sumList(j, k)

