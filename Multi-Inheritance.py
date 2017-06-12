#! /usr/bin/env python3
# -*- coding: utf-8 -*-

##
## { multi-inheritance }
##

# MixIn的目的就是给一个类增加多个功能


# 定制类

class Student(object):
	def __init__(self, name):
		self.name = name
	
	def __str__(self): # 返回用户看到的字符串
		return 'Student object (name: %s)' % self.name

	__repr__ = __str__  # __repr__()返回程序开发者看到的字符串, 是为调试服务的
	
	def __getattr__(self, attr):
		if attr == 'score':
			return 99
		if attr == 'age':
			return lambda: 25

		raise AttributeError('\'Student\' object has no attribite \'%s\'' % attr)

	def __call__(self):  # 直接对实例进行调用
		print('My name is %s.' % self.name)
	                    
	              


print(Student('roni'))
s = Student('dev')
print(s.score)
print(s.age())
print(s())

print(callable(Student('dec'))) # 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
print(callable(max))



class Fib(object):
	def __init__(self):
		self.a = 0
		self.b = 1

	def __iter__(self): # 该方法返回一个迭代对象
		return self

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 8:
			raise StopIteration()

		return self.a

	def __getitem__(self, n):
		if isinstance(n, int):
			a, b = 1, 1
			for x in range(n):
				a,b = b, a+b
			return a
		if isinstance(n, slice):
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a,b = 1,1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a,b = b, a+b
			return L



for n in Fib():
	print(n)


f = Fib()
print(f[0])
s = f[:4]
print(s)



from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


for name,member in Month.__members__.items(): # value属性则是自动赋给成员的int常量，默认从1开始计数。
	print(name, '=>', member, ',', member.value)


from enum import Enum, unique

@unique # 装饰器,用来检查保证没有重复值
class Weekend(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

day01 = Weekend.Mon
print(day01)

print(Weekend["Fri"])

print(Weekend.Sat.value)

print(Weekend(4))

for name,member in Weekend.__members__.items(): # value属性则是自动赋给成员的int常量，默认从1开始计数。
	print(name, '=>', member, ',', member.value)



class Hello(object):
	def hello(self, name: 'World'):
		print('Hello, %s.' % name)


def fn(self, name='world'):
	print('Hello, %s' % name)

he = type('Hel', (object,), dict(hello=fn))
h = he()
h.hello()























