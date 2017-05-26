# _*_ coding: utf-8 _*_

d={'a':1,'b':2,'c':3}
for key in d:
    print key

for value in d.itervalues():
    print value

for k,v in d.iteritems():
    print k,v

for ch in 'ABC':
    print ch

#当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断

from collections import Iterable
print isinstance('abc',Iterable) # str是否可迭代
print isinstance([1,2,3],Iterable) # list是否可迭代
print isinstance(123,Iterable) #整数是否可迭代

#对list实现类似Java那样的下标循环
#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i,value in enumerate(['A','B','C']):
    print i,value

for x,y in [(1,1),(2,4),(3,9)]:
    print x,y
