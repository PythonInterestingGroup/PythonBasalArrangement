#!/usr/bin/env python
# -*- coding: utf-8 -*-

#偏函数
#int函数默认按十进制转换，提供base参数，默认值10，可做N进制转换
print(int('12345'))
print(int('12345',base=8))  #字符串是8进制，'9'会报错
print(int('12345',16))

#转换2进制，默认字符串是二进制的，定义一个int2()的函数，默认把base=2传进
def int2(x,base=2):
    return int(x,base)
print(int2('1000'))

#functools.partial可创建一个偏函数,把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数
import functools
int2=functools.partial(int,base=2)
print(int2('1000'))
print(int2('1000000', base=10))  #也可以传入其他base值

