#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
	
	def __init__(self,name,score):
		self.name = name
		self.score = score
		
	def print_score(self):
		print('%s:%s'%(self.name,self.score))
		
	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else :
			return 'C'
		

timor = Student("timor",60)

timor.print_score()
print('rank:',timor.get_grade())

## 访问限制
class Teacher(object):
	
	def __init__(self,name,score):
		self.__name = name
		self.__score = score
		
	def print_score(self):
		print('%s:%s'%(self.__name,self.__score))
		
hanzo = Teacher("hanzo",70)
## print(hanzo.__score)
hanzo.print_score()

		
	