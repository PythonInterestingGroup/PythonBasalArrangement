#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module' # 一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = "roni" # 使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名

import sys

def test():
	args = sys.argv # argv变量，用list存储了命令行的所有参数,argv至少有一个元素，因为第一个参数永远是该.py文件的名称
	if len(args) == 1:
		print("hello world")
	elif len(args) == 2:
		print("Hello, %s" % args[1])
	else:
		print(" too many arguments")


if __name__ == '__main__':
	test()


from PIL import Image

im = Image.open("runloop.png")
print(im.format, im.size, im.mode)
im.thumbnail((200, 200))
im.save('thumb.jpg', 'JPEG')

import sys
print(sys.path)
sys.path.append("/modules") # 修改模块路径, 运行完失效
print(sys.path)


import functools
import time

def decorator_fib(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print(func(*args, **kw))
	return wrapper

@decorator_fib
def fibonacci(n):
	if n < 1:
		return
	a,b = 1,1
	l = []
	for i in range(1, n+1):
		if i == 1:
			l = l + [a]
		elif i == 2:
			l = l + [b]
		else:
			a,b = b,a+b
			l = l + [b]
		i += 1
	return l[-1]


fibonacci(6)



'''
def fib02(n,a=1,b=1,l=[]):
	if n == 1:
		l = l + [a]
		return l
	elif n == 2:
		l = l + [b]
		return l
	else:
		a,b = b, a+b
		l = l+[b]
		return fib02(n-1, a,b,l)

print(fib02(6)[-1])



def fact(n):
	return fib03(n, 1)

def fib03(num,pro=1,a=1,b=1,l=[]):
	if num == 1:
		l = l+[a]
		pro = 1
		return l
	elif num == 2:
		l = l + [b]
		pro = 1
		return l
	else:
		a,b = b,a+b
		l = l + [b]
		pro = b
		return fib03(num-1,pro,a,b,l)

print(fact(6)[-1])
'''

import decorator

f0 = decorator.log(fibonacci)
f0(7)





