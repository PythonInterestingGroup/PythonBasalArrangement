#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 递归函数：在函数内部调用自己
# 计算n!
# 使用循环语句while
def fact(n):
    sum = 1
    i = 1
    while (i < n):
        i = i + 1
        sum = sum * i
    return sum


# 使用递归
def fact1(n):
    if n == 1:
        return 1
    return n * fact1(n - 1)


a = fact(10)
print(a)

a = fact1(100)  # 使用递归，当参数值过大时，会导致栈溢出
print(a)


# practice :汉诺塔


def move(n, a, b, c):
    if n == 1:
        print('%s-->%s' % (a, c))
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


move(3, 'A', 'B', 'C')
