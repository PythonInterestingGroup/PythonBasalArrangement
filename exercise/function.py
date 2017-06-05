#!/usr/bin/env python
#-*- coding:utf-8 -*-
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x
a = raw_input('please input x:')
print a
print my_abs(int(a))
#pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来
def my_fuction():
    pass

y=20
if y>=10:
    pass
c = raw_input('c:')
def my_fuction1(x):
    if not isinstance(x,(int,float)):
        raise  TypeError('you input type is bad')
    if x>=0:
        return x
    else:
        return -x

print my_fuction1(int(c))

import math
def move(x,y,step,angle=0):
    nx = x+step * math.cos(angle)
    ny = y-step * math.sin(angle)
    return nx,ny
x,y = move(100,100,60,math.pi/6)
r = move(100,100,60,math.pi/6)
print x
print y
print r
a
