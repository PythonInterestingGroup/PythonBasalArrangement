#! usr/bin/env python3
# -*- codeing: utf-8 -*-


##
## 高级特性
##

# slice
# 
import os

'''
l = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print(l[:3])
print(l[-3:])  # 左边的 index 必须比右边的小

L01 = list(range(100))
print(L01[11:20])
print(L01[0:20:2])

t = tuple(range(100))
print(t[20:30])

s = 'ASDFGHJK'
print(s[:3])

# 迭代 -- Iterable & Iterator
# 
# 可以通过 for 循环遍历的就是 Iterable
 
d = {'a': 1, 'b': 2, 'c': 3}
for key, value in d.items(): # d.values() d.keys()
 	print('key = ', key, 'value = ', value)
 
from collections import Iterable

print(isinstance('abc', Iterable))
print(isinstance([], Iterable))
print(isinstance(123, Iterable))

for index, value in enumerate(l):
	print('index = ', index, 'value = ', value)


# 列表生成式 List comprehensions

lc01 = [ x * x for x in range(1, 11) if x % 2 == 0]
print('lc01 = ',lc01)

lc02 = [ m + n for m in 'ASD' for n in 'ZXC']
print('lc02 = ',lc02)



od = [d for d in os.listdir('.')] # os.listdir 可以列出文件和目录
print(os)


dl = [k + '=' + str(v) for k,v in d.items()]
print(dl)


print([s.lower() for s in l])

el = ['Hello', 'World', 18, 'Apple', None]
re = [s.lower() for s in el if isinstance(s, str)]
print('re = ', re)
'''

# generator - 一边循环一边计算

# lc01 = [ x * x for x in range(1, 11) if x % 2 == 0]

g01 = ( x * x for x in range(1, 11) if x % 2 == 0 )  # () replace []
print(g01)
# print(next(g01))
for x in g01:
	print(x)

def fib(max):
	n, a, b = 0, 1, 1
	while  n < max:
		print(b)
		a, b = b, a+b
		n = n + 1
	return 'done'
#fib(5)

def gFib(max):
	n, a, b = 0, 1, 1
	while  n < max:
		yield b      # yield => 执行到这里结束, 下次 next(g) 从上次返回的 yield 语句出继续执行
		a, b = b, a+b
		n = n + 1
	return 'done'

'''
for x in gFib(5):
	print(x)
'''

g = gFib(6)
while True:
	try:
		x = next(g)
		print('g:', x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break

# 杨辉三角

def triangles(max):
	n, L = 0, [1]
	while n < max:
		if n == 0:
			res = L
		elif n == 1:
			res = L
			res.append(1)
		else:
			res = [L[x-1] + L[x] for x in range(1, n)]
			res.insert(0, 1)
			res.append(1)
		yield res
		L = res
		n = n + 1

for i in triangles(10):
	print(i)


from collections import Iterator

isinstance([], Iterator)
isinstance((x for x in range(1,10)), Iterator)


# Iterator

isinstance((x for x in range(1,10)), Iterator)

it = iter([1, 2, 3])
while True:
	try:
		x = next(it)
		print(x)
	except StopIteration as e:
		break



