#!/usr/bin/env python
# -*- coding: utf-8 -*-

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
l=['adam', 'LISA', 'barT']
def normalize(name):
    return name[0].upper()+name[1:].lower()
l2=list(map(normalize,l))  #list转换类型
print (l2)

print(list(map(lambda x:x.capitalize(),['adam','LISA','barT'])))  

def normalize(name):
    return name.capitalize()
names = list(map(normalize, l))
print(names)


#编写一个prod()函数，可以接受一个list并利用reduce()求积
from functools import reduce
def f(x,y):
    return x*y
def prod(s):
    return reduce(f,s)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))



#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
q='123.456'
l=list(q)
l.pop(3)

def str2float(a):
    def lpl(x,y):
        return x*10+y
    def str1float(a):
        return {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6}[a]
    return reduce(lpl,map(str1float,a))
print(str2float(l)/1000)

q='123.456'
l=list(q)

def str2float(a):
    def lpl(x,y):
        return x+y
    def str1float(a):
        return {'1':100,'2':20,'3':3,'4':0.4,'5':0.05,'6':0.006,'.':0}[a]#百度了一下这个用法后面加个[a]的意思是：a的值必须是这个dict中sr所对应的值！  固定用法 记住就好…………严重抗议老廖这个解释不到位，增加游戏难度
    return reduce(lpl,map(str1float,a))
print(str2float(l))

from functools import reduce
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2float(s):
    # 找到小数点索引位置
    dotIndex = s.find('.')
    # 移除小数点
    s = s.replace('.', '')
    # 需要缩小的倍数
    dotTimes = len(s) - dotIndex

    return reduce(lambda x, y: x*10+y, map(int, s)) / pow(10, dotTimes)

print('str2float(\'123.4567\') =', str2float('123.45670'))

def str2float(s):
    l = s.split('.')
    def char2num(s):    
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    n1 = reduce(lambda x, y: x * 10 + y, map(char2num, l[0]))
    n2 = reduce(lambda x, y: x * 10 + y, map(char2num, l[1])) * (10 ** -(len(l[1])))
    return n1 + n2

print('str2float(\'123.456\') =', str2float('123.456'))

def str2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
def str2float(s):
    s = s.split('.')
    if s.__len__() > 1:
        s1 = reduce(lambda a,b:10 * a + b,map(str2num,s[0]))
        s2 = reduce(lambda a,b:10 * a + b,map(str2num,s[1]))/10 ** s[1].__len__()
        return s1 + s2
    else:
        return reduce(lambda a,b:10*a+b,map(str2num,s[0]))
print(str2float('12.34'))

#有待理解先记着
