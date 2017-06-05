#!/usr/bin/env python
#-*- coding:utf-8 -*-
'a test module'
__authon__ = 'djx'
import sys
def f():
    args = sys.argv
    if len(args) == 1:
        print 'Hello,World!'
    elif len(args) == 2:
        print 'Hello,%s' % args[1]
    else:
        print 'Too many arguments'

if __name__ == '__main__':
   f()