#!/usr/bin/env python
# -*- coding: utf-8 -*-

print abs  
print abs(-10)

f = abs  #函数本身也可以赋值给变量，变量可以指向函数
print f(10)

#函数名其实就是指向函数的变量

#变量可以指向函数，函数的参数能接收变量
#那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

def add(x,y,f):
    return f(x)+f(y)

print add(-5,6,abs)





