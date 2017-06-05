#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('/Users/ursus/Desktop/Python/Github/PythonBasalArrangement/exercise/20170604')
print(sys.path)

import TimeConsuming

@TimeConsuming.cal_method_times
def fibonacci(n):
	a,b,index = 1,1,1
	while n > index :
		a,b = b,a+b
		index += 1
	print('第%s个斐波那契数是%s'%(n,b))
	return b
	
fibonacci(2000)
