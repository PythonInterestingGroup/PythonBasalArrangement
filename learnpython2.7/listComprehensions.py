# _*_ coding: utf-8 _*_

print range(1,11)

#生成[1x1, 2x2, 3x3, ..., 10x10]

L=[]
for x in range(1,11):
    L.append(x*x)
print L

print [x*x for x in range(1,11)]

#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
print [x*x for x in range(1,11) if x%2==0]

#可以使用两层循环，可以生成全排列

print [m + n for m in 'ABC' for n in 'XYZ']

#列出当前目录下的所有文件和目录名
import os #导入os模块

print [d for d in os.listdir('.')] # os.listdir可以列出文件和目录

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.iteritems():
    print k,'=',v

print [k + '=' + v for k, v in d.iteritems()]

L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]

#使用内建的isinstance函数可以判断一个变量是不是字符串：
x='abc'
y=123
print isinstance (x,str)
print isinstance(y,str)
