# -*- coding:utf-8 -*-

class StudentSlots(object):
	__slots__ = ('name', 'age')

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def getName(self):
		print self.name

	def getAge(self):
		print self.age

	def setName(self, name):
		self.name = name

	def setAge(self, age):
		self.age = age

jack = StudentSlots('Jack Chen', 78)
jack.getAge()

# jack.score = 89
# print dir(jack)

# class Student(object):
# 	"""dname, agetring for Student"""
# 	def __init__(self, name, score):
# 		self.__name = name
# 		self.__score = score

# 	def getScore(self):
# 		return self.__score

# 	def set_score(self, value):
# 		if not isinstance(value, int):
# 			raise ValueError('score must be integer!')
# 		if value < 0 or value > 100:
# 			raise ValueError('score must between 0 and 100!')

class Student(object):
	"""dname, agetring for Student"""
	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	@property	
	def score(self):
		return self.__score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 and 100!')
		self.__score = value

Stephen = Student('da', 43)
Stephen.score = 80
Stephen.score
