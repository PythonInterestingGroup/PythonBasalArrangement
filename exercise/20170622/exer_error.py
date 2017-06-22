#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
	print('try')
	r = 10 / 0
	print('result:',r)
except ZeroDivisionError as e:
	print('except:',e)
finally:
	print('finally')
print('END')

x = 'a'
#x = '0'

try:
	print('try...')
	r = 10 / int(x)
	print('result:',r)
except ValueError as e:
	print('ValueError:',e)
except ZeroDivisionError as e:
	print('ZeroDivisionError:',e)
finally:
	print('finally')
print('END')

## 记录错误
import logging

def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2
	
def main():
	try:
		bar('0')
	except Exception as e:
		logging.exception(e)

main()
print('END')
	
	
	
	
	