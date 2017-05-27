#!/usr/bin/env python
# -*- coding: utf-8 -*-

#用 reduce 函数实现 map 函数的功能
#例如: L = [1, 2, 3, 4, 5, 6, 7, 8, 9] => [1, 4, 9, 16, 25, 36, 49, 64, 81]
#要求: 使用 reduce 函数

def f(x):
    return x*x
print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

from functools import reduce

def g(x,y):
    if isinstance(x,list):
        t=x+[y*y]
    else:
        t=[x*x]+[y*y]
    return t
print(reduce(g, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

#[1,2,3,4]
#t1=[1*1]+[2*2]
#t2=t1+[3*3]
#t3=t2+[4*4]
#函数返回值不仅可以是简单的数据类型int,str，也可以是list等


#将一个二维数组内的每个数平方并且展平成一维数组
#例如: ll = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] => [1, 4, 9, 16, 25, 36, 49, 64, 81]
#要求: 使用 map 函数

l1= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def f(x):
    return x*x

def g(s):
    l=[]
    for i in s:
        for j in i:
            l.append(j)
    return l

l2=list(map(f,g(l1)))
print (l2)


'''def g(s):
    l=[]
    for i in s:
        l.append(i*i)
    return l
print(list(map(g,l1)))'''

           
#别人的写法
'''def f(x):
    return x*x
def flatmap(f,S):
    r=[]
    for i in S:
        m=f(f,i)
        r+=list(m)
    return r
l3=flatmap(map,l1)
print(l3)'''
    
#http://www.jianshu.com/p/3595b2924722
#functor:表示范畴A与范畴B之间的映射
#monad:，表示一类能够被压缩的东西,自函子functor范畴上的幺半群
#不懂 搜的都是swift
