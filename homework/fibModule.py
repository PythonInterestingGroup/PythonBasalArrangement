# _*_ coding:utf-8 _*_


import  decoratorModule

@decoratorModule.log
def count_fib(n):
	i, a, b = 0, 0, 1
	while i < n:
		a, b = b, a+b
		i += 1
	return a

print('fib:',count_fib(10))