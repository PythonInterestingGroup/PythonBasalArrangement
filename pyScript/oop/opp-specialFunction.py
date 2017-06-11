# -*- coding: utf-8 -*-
'Usage of some special functions'

## __str__: 返回用户看到的信息
## __repr__: 返回开发人员看到的信息
print '\n1. Usage of __str__:'
class Student(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return 'Student object (name: %s)' % self.name
	__repr__ = __str__ # redefine

print Student('Michael')
s = Student('Kevin')
s


## __iter__
print '\n2. Usage of __iter__:'
class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1

	def __iter__(self):
		return self

	def next(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 100:
			raise StopIteration()
		return self.a

for n in Fib():
	print n


## __getitem__
print '\n3. Usage of __getitem__:'
class FibRe(object):
	def __getitem__(self, n):
		if isinstance(n, int):
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a

		if isinstance(n, slice):
			start = n.start
			stop = n.stop
			#step = n.step
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a+b
			return L

f = FibRe()
print f[0:30:2]

## __getattr__
print '\n4. Usage of __getattr__:'
class Student1(object):
	def __init__(self):
		self.name = 'Kevin'
	def __getattr__(self, attr):
		if attr == 'score':
			return lambda:98

curry = Student1()
print curry.score()

## __call__
print '\n5. Usage of __call__:'
class Student2(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

Tom = Student2('Tom')
Tom()