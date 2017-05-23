# _*_ coding: utf-8 _*_


print("map()函数接收两个参数,一个函数,一个是 Iterable. map依次将Iterable 的每个元素作用在函数")

def f(x):
	return x*x

r = map(f,[x for x in range(1,10)])
print(list(r))

print("reduce把一个函数作用在一个序列[x1, x2, x3, x4]上,这个函数必须接受两个参数")
print("reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)")


from functools import reduce

def fn(x, y):
	return 10*x + y

print(reduce(fn,[1,3,5,7,9]))

print("编写一个 str -> int 的函数")

def str2int(s):
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	return reduce(fn, map(char2num, s))

print("\"12345\" =",str2int("12345"))

