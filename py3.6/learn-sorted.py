#!/usr/bin/env python
# -*- coding: utf-8 -*-

#sorted 对list进行排序
#1
print(sorted([36, 5, -12, 9, -21]))

#2：sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
#key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序
print(sorted([36, 5, -12, 9, -21], key=abs))

#默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
print(sorted(['bob', 'about', 'Zoo', 'Credit']))

#忽略大小写排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

#3：第三个参数reverse=True，反向排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

#练习
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name)
print(L2)

def by_score(t):
    return t[1]
L2 = sorted(L, key=by_score,reverse=True)
print(L2)

