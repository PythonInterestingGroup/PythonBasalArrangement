#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Python内建了map()和reduce()函数
#map()函数接收两个参数，一个是函数，一个是序列
#map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。

def f(x):
    return x*x
a=map(f,[1,2,3,4,5,6,7,8,9])
print a

l=[]
for n in [1,2,3,4,5,6,7,8,9]:
    l.append(f(n))
print l

#把这个list所有数字转为字符串
print map(str,[1,2,3,4,5])

#reduce把一个函数作用在一个序列[x1, x2, x3...]上，
#这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，
#其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

#求和
def add(x,y):
    return x+y
a=reduce(add,[1,3,5,7,9])
print a

#把序列[1, 3, 5, 7, 9]变换成整数13579
def fn(x,y):
    return x*10+y
a=reduce(fn,[1,3,5,7,9])
print a

#把str转换为int的函数
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print reduce(fn,map(char2num,'13579'))

#整理成一个str2int的函数
def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn,map(char2num,s))

#用lambda函数简化
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2int(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))
        
#练习1
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
#输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']

l=['adam', 'LISA', 'barT']
def f(s):
    return s[0].upper()+s[1:].lower()
print map(f,l)

#练习2
#Python提供的sum()函数可以接受一个list并求和
#请编写一个prod()函数，可以接受一个list并利用reduce()求积。

def f(x,y):
    return x*y

def prod(s):
    return reduce(f,s)
s=input('please input a list:')
#s=[1,2,3]
print prod(s)

