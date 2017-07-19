#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 写一个方法返回 *斐波那契数列* 的第n个数

def f(x):
    index, a, b = 0, 0, 1
    if max == 1:
        print 1
    else:
        while index < x:
            if index == x - 1:
                return b
            a, b = b, a + b
            index +=1
print f(7)

# 将那次[装饰器那次的作业]中第二个任务封装成的模块，然后导入该模块，测试刚才写的 *斐波那契数列* 方法的运行耗时
import task09
fuctionA=task09.mylog_text('dengjx')(f)
fuctionA(8)




