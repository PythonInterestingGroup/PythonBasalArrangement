#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
sys.path.append('/Users/ursus/Desktop/Python/Github/PythonBasalArrangement/exercise/20170604')
print(sys.path)


import exer_module_used
import TimeConsuming



@TimeConsuming.cal_method_times
def test():
	for i in range(10000000):
		pass
		
@TimeConsuming.cal_method_times
def test_thumbnail_image():
	exer_module_used.test()

test()
test_thumbnail_image()

