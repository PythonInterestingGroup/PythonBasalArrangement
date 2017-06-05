#!/usr/bin/env python3
# -*- coding:utf-8 -*-

L = ['peipei', 15, 'anhuisuzhou', 'shopping', 'shopping']
Li = list(range(100))  # range(100）：表示0—99
print(Li)
Li = list(range(1, 100, 2))  # range(1,100,2):表示1-99，间隔2
print(Li)
# 切片
print(Li[0:3])
print(Li[-1])
print(Li[0])
print(Li[1:30])
print(Li[4:6])
print(Li[0:10])
print(Li[-10:])
print(Li[:])

# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
tu = tuple(range(10))
print(tu)
print(tu[0:6])

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串
st = 'abcdefg'
print(st[0:2])

# 迭代:如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
list1 = ['123', 12, 'sefccf', 768.789]
for i in list1:
    print(i)
tuple1 = (1, 2, 3, '12fdff', 'edwevv')
for i in tuple1:
    print(i)
dict1 = {'12': 235, 12: '32663', 78: 'frhcvh'}
for key in dict1:
    print(key)
for values in dict1.values():
    print(values)
for key, values in dict1.items():
    print(key, values)

str1 = '1234twqdyvshb'
for s in str1:
    print(s)
from collections import Iterable

a = isinstance('abc', Iterable)
print(a)
b = isinstance(123, Iterable)
print(b)
c = isinstance((1, 2, 3), Iterable)
print(c)
d = isinstance({12: 'a', 23: 'b'}, Iterable)
print(d)
l = isinstance(['1f', 712, 'hcsdhvfh'], Iterable)
print(l)

d = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
for key, values in d.items():
    print(key, values)
l = ['a', 'b', 'c', 'd']
for i, values in enumerate(l):
    print(i, values)
a = isinstance([(1, 2), (2, 4), (3, 9)], Iterable)
print(a)
ll = [(1, 2), (2, 4), (3, 9)]
for x, y in ll:
    print(x, y)

# 列表生成式：list comprehensions
l = list(range(0, 11))
print(l)
# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
l = list(x * x for x in range(1, 11))
print(l)
l = list(x * x for x in range(1, 11) if x % 2 == 0)
print(l)
l = list(x for x in range(1, 11) if x % 2 != 0)
print(l)
# 两层循环:全排列
l = list(m + n for m in 'ABCD' for n in 'EFGH')
print(l)

import os

l = list(d for d in os.listdir('.'))
print(l)
d = {'x': 'A', 'y': 'B', 'z': 'C'}
l = list(k + '=' + v for k, v in d.items())
print(l)
l = ['a', 'b', 'c', 'd']
l = list(s.upper() for s in l)
print(l)

# practice:如果list中既包含字符串，又包含整数，
# 由于非字符串类型没有lower()方法，所以列表生成式会报错,请修改列表生成式，通过添加if语句保证列表生成式能正确地执行

L = ['Hello', 'World', 18, 'Apple', None]
L = list(l.lower() for l in L if isinstance(l, str) == True)
print(L)

# generator:生成器
g = (x * x for x in range(10))
for i in g:
    print(i)

