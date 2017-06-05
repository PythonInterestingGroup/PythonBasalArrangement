#!/usr/bin/env python
#--*-- coding:UTF-8 --*--
#调用函数
#abs函数 求绝对值函数
a = -100
print '%d的绝对值为%d' % (a,abs(a))

#cmp函数 比较函数
print cmp(1,2)
print cmp(2,2)
print cmp(3,2)

#数据类型转换
print int('123')
print int(12.133)
print float('12.35')
print str(12345)
print unicode(100)
#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量
functionA =abs
print functionA(-20)

#定义函数
def fuctionB(x):
    return x*x
print fuctionB(20)

