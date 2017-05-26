#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Python内建的filter()函数用于过滤序列。
#filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

#在一个list中，删掉偶数，只保留奇数
def is_odd(n):
    return n%2==1 #取余数
print filter(is_odd,[1,2,3,4,5,6,7,8,9])

#把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()
print filter(not_empty,['a','',None,'c','','d'])

#练习
#用filter()删除1~100的素数
def not_sushu(n):
    for i in range(2,n):
        if n%i==0:
            #i=i+1
            return True
    return False
                 
#l=range(1,11) #[1,2,3,4,5,6,7,8,9,10]
l=range(1,101)
print filter(not_sushu,l)

print range(2,2) #空[]



