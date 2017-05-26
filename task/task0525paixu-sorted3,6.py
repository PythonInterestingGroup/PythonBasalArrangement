#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import itemgetter

#对第二列进行从小到大排序，在对第三列从大到小排序
students =[('john','B',15),('jane','A',12),('dave','B',10),('ethan','C',20),('peter','B',20),('mike','C',16)]

def by_degree(t):
    return t[1]
def by_score(t):
    return t[2]
def by_cj(t):
    return t[1],t[2]


print("原序列")
print(students)

print('按第二列排序,从大到小')
print(sorted(students, key=by_degree,reverse=True))

print("第二列从小到大")
print(sorted(students, key=by_degree))


print("按第一列排序，顺序从小到大")
print(sorted(students, key=itemgetter(0)))

print("按第二列排序，顺序从小到大")
print(sorted(students, key=lambda t: t[1]))
#sorted(students, cmp=lambda x,y : cmp(x[1], y[1])) py3移除了cmp函数 

print("按第二列排序，倒叙序从大到小")
print(sorted(students, key=itemgetter(1), reverse=True))
#sorted(students, key=itemgetter(1,2))多级排序

print("先按第二列排序，在按第三列排序，从小到大")
print(sorted(students, key=by_cj))

#print(sorted(students, key=by_cj),reverse1=True)报错

#多级排序，顺序不同，不知怎么调用




