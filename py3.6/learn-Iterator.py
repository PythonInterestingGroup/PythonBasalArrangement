#!/usr/bin/env python
# -*- coding: utf-8 -*-

#迭代器
#可以直接作用于for循环的对象统称为可迭代对象：Iterable
#可以使用isinstance()判断一个对象是否是Iterable对象：

from collections import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable)) #False

#生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了
#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

from collections import Iterator
print (isinstance((x for x in range(10)), Iterator)) #T
print(isinstance([], Iterator)) #F
print(isinstance({}, Iterator)) #F
print(isinstance('abc', Iterator)) #F

#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator

#把list、dict、str等Iterable变成Iterator可以使用iter()函数：
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))

#Iterator对象表示的是一个数据流,可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
#Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。


#for循环本质上就是通过不断调用next()函数实现的
for x in [1, 2, 3, 4, 5]:
    pass

#等价于：
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
