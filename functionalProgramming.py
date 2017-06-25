#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce
from django.template.defaultfilters import upper, lower

print(abs)
f = abs  # 把函数赋值给变量，通过变量调用函数,函数名本身也是一个变量
print(f(-10))


# 传入函数：函数的参数是函数
def add(x, y, f):
    return f(x) + f(y)


print(add(-5, -6, abs))


# map和reduce函数
# map()函数接受两个参数，一个函数，一个序列Iterable,map()把函数作用于序列的每一个元素，并把新的序列作为Iterator返回
def f(x):
    return x * x


l = map(f, [1, 2, 3, 4, 5, 6])
print(list(l))

l1 = map(upper, ['a', 'c'])
print(list(l1))

l2 = map(lower, ['A', 'c', 'j', 'K'])
print(list(l2))


# reduce函数 传入两个参数：一个函数，一个序列，reduce把结果继续和序列的下一个元素做累积计算
def add(x, y):
    return x + y


a = reduce(add, [1, 2, 3, 4, 5])
print(a)


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 2, 3, 4, 5]))


# 字符串转化成数字
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


print(reduce(fn, map(char2num, '12345')))


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(fn, map(char2num, s))


print(str2int('14215535'))

q = int('1234')
print(q)


def normalize(name):
    return name.capitalize()


l = list(map(normalize, ['abc', 'AATTT', 'yvfh']))
print(l)


def prod(x, y):
    return x * y


print(reduce(prod, map(char2num, '1357')))

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456



