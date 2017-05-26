#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = (x * x for x in range(5))
print(s)
for x in s:
    print(x)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)

# call generator manually:
g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


#杨辉三角
'''
          1
        1   1
      1   2   1
    1   3   3   1
  1   4   6   4   1
1   5   10  10  5   1'''

#把每一行看做一个list，试写一个generator，不断输出下一行的list：
def triangles():
    l=[1]
    while True:
        yield l
        l.append(0)  #为数组添加最后一位
        l=[l[i-1]+l[i] for i in range(len(l))]


#L2.insert(i+1,L[i]+L[i+1])   for i in range(len(L)-1))

n=0
for t in triangles():
    print(t)
    n=n+1
    if n==10:
        break

