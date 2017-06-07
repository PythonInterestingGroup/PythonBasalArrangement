#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
	
	def get_score(self):
		return self._score
		
	def set_score(self,value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100 :
			raise ValueError('score must between 0 ~ 100!')
		self._score = value
		
s = Student()
#s.set_score(101)
s.set_score(99)
print(s.get_score())

class Teacher(object):
	
	@property
	def age(self):
		return self._age
	
	@age.setter
	def age(self,age):
		if not isinstance(age, int):
			raise ValueError('age must be an integer')
		if age < 15 or age >70:
			raise ValueError('age must between 12 ~ 70')
		self._age = age
		
t = Teacher()
t.age = 30
print(t.age)
#t.age = 10