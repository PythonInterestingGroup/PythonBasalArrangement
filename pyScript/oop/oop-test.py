# -*- coding: utf-8 -*-
'An example printing the student score for oop '

std1 = {'name': 'Michael', 'Score': 98}
std2 = {'name': 'Bob', 'Score': 81}

class Student(object):
	"""create a Student object"""
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print '%s: %s' % (self.name, self.score)

	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
print "bart's grade is: ", bart.get_grade()
print "lisa's grade is: ", lisa.get_grade()

bart.age = 8 # 动态添加变量
print bart.age

print '--'*8 + 'New Student Object' + '--'*8

class StudentNew(object):
	"""Create a new Student object"""
	def __init__(self, name, score):
		self.__name = name   #私有化
		self.__score = score

	def getName(self):
		return self.__name

	def getScore(self):
		return self.__score

	def setScore(self, score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')

	def print_score(self):
		print '%s: %s' %(self.__name, self.__score)

shawn = StudentNew('Shawn', 81)
print '%s: %d' %(shawn.getName(), shawn.getScore())
shawn.setScore(89)
print '%s: %d' %(shawn.getName(), shawn.getScore())
