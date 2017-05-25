# _*_ coding: utf-8 _*_

print("偏函数")
print("用于把某些函数的参数固定住")

import functools 
int2 = functools.partial(int, base = 2)
print(int2('10000'))

import module

module.test()