#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__='djx'
#使用模块
import  sys
def test():
    args = sys.argv
    if len(args)==1:
        print 'Hello World!'
    elif len(args)==2:
        print  'Hello %s!' % args[1]
    else:
        print 'Too many arguments'

if __name__ == '__main__':
     test()