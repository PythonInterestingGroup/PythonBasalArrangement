#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 文档注释
'exercise module'

# 作者
__author__ = 'Ursus'

import sys

def test():
	args = sys.argv
	if len(args) == 1:
		print('Hello World!')
	elif len(args) == 2:
		print('Hello, %s!' % args[1])
	else:
		print('too many arguments')
		
if __name__ == '__main__':
	test()
