#! usr/bin/env python3
# -*- codeing: utf-8 -*-

##
## 函数式编程
##

# Higher-order function

f = abs
f(-10)

'''
import builtins; builtins.abs = 10
print(abs)
'''

def add(x, y, f):
	return f(x) + f(y)

a = add(5, -10, abs)
print(a)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def f(x):
	return x*x
m = map(f, l) # r: Iterator
print(m)
print(list(m))

from functools import reduce

def fn(x, y):
	return x + y
r = reduce(fn, l)
print(r)


l1 = ['adam', 'LISA', 'barT']
def upp(x):
	s = ""
	for index,value in enumerate(x):
		if index == 0:
			s += value.upper()
		else:
			s += value.lower()
	return s
u = map(upp, l1)
print(list(u))

# 用 reduce 实现以 map 函数的功能
def rmap(x, y):
	if isinstance(x, list):
		t = x + [y*y]
	else:
		t = [x*x] + [y*y]
	return t
rm = reduce(rmap, l)
print(rm)

# 

ll = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def square(x):
	return x*x

def flatMap(f, ll):
	r = []
	for l in ll:
		m = f(square, l)
		r += list(m)
	return r
 
nll = flatMap(map, ll)
print('nll = ', nll)

print("---------")

'''
def fff(arr):
	r = []
	for i in arr:
		r.append(i*i)
	return r


sss = map(fff, ll)
print(list(sss))
'''



