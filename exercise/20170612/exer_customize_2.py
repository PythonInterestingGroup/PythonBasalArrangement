#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __getitem__ 

class Fib(object):
	def __getitem__(self,n):
		a,b = 1,1
		for x in range(n):
			a,b = b,a+b
		return a
	
f = Fib()
print(f[10],f[15])

class Fib2(object):
	def __getitem__(self,n):
		if isinstance(n, int):
			a,b = 1,1
			for x in range(n):
				a,b = b,a+b
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
				a,b = b,a+b
			return L
			
f2 = Fib2()
print(f2[0:6])
print(f2[5])

# __getattr__

class Student(object):
	
	def __init__(self):
		self.name = 'Michael'
			
	def __getattr__(self,attr):
		if attr == 'name':
			return 'Mike'
		if attr == 'score':
			return 99
		if attr == 'age':
			return lambda:25
			
s = Student()
print(s.name,s.score,s.age())
			
class Student_v2(object):
	def __getattr__(self,attr):
		if attr == 'age':
			return lambda:25
		raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
		
s2 = Student_v2()
print(s2.age())


class Chain(object):
	
	def __init__(self,path = ''):
		self.__path = path
	
	def __getattr__(self,path):
		return Chain('%s/%s' % (self.__path,path))
		
	def __str__(self):
		return self.__path
		
	__repr__ = __str__
	
ch = Chain().status.user.timeline.list
ch2 = Chain().status
print(ch)
print(ch2.user)

class Api_Url(object):
	
	def __init__(self,path = ''):
		self.__path = path
		
	def __getattr__(self,attr):
		if attr == 'user':
			return lambda path : Api_Url('%s/%s' % (self.__path,path))
		return Api_Url('%s/%s' % (self.__path,attr))
		
	def __str__(self):
		return self.__path
		
	__repr__ = __str__

url = Api_Url().status.user('ursus').timeline.list
print(url)

# __call__

class Student_v3(object):
	def __init__(self,name):
		self.name = name
	
	def __call__(self):
		print('My name is %s '% self.name)
	
s3 = Student_v3('Jack')
s3()
