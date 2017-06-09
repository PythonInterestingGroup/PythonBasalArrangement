#! /usr/bin/env python3
# -*- coding: utf-8 -*-

##
## __slots__ and @property
##

class Student(object):
	#__slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
	
	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, score):
		if not isinstance(score, int):
			raise ValueError('score must be an integer!')
		if score < 0 or score > 100:
			raise ValueError('score must between 0 ~ 100')
		self._score = score


s = Student()
s.name = 'roni'  # 给实例动态绑定属性
print(s.name)


def set_age(self, age):
	self.age = age
	
from types import MethodType
s.set_age = MethodType(set_age, s)  # 给实例动态绑定方法 -- 其他实例没有

s.set_age(25)
print(s.age)


Student.set_age = set_age  # 给 class 动态绑定方法
                           
s2 = Student()
s2.set_age(233)
print(s2.age)


# __slots__ 限制class 实例能添加的属性  => __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的

s.name = 'mars'
s.age = 30
#s.score = 99 # error

s.score = 80
print(s.score)



class Screen(object):
	@property
	def width(self):
		return self._width

	@width.setter
	def width(self,value):
		self._width = value
		
	@property 
	def height(self):
		return self._height

	@height.setter
	def height(self, value):
		self._height = value

	@property
	def resolution(self):
		return self._width * self._height












class Coordinate(object):
	""" 坐标 """
	def __init__(self, x, y):
		super(Coordinate, self).__init__()
		self.__x = x
		self.__y = y

	def set_x(self, x):
		self.__x = x
	def get_x(self):
		return self.__x

	def set_y(self, y):
		self.__y = y
	def get_y(self):
		return self.__y


# 方向
Direction = {'up': 1, 'right': 2, 'down': 3, 'left': 4}
		

class Robot(object):
	""" Robot move to anywhere if you would like """
	def __init__(self, name, origin, direction):
		super(Robot, self).__init__()
		self.__name = name
		self.__origin = origin
		self.__direction = direction

	def set_direction(self, direction):
		self.__direction = direction
	def get_direciton(self):
		return self.__direction

	def set_origin(self, origin):
		self.__origin = origin
	def get_origin(self, origin):
		return self.__origin

	def changeDirection(self,aimDiretion):
		if self.__direction == aimDiretion:
			return
		else:
			if self.__direction < aimDiretion:
				self.set_direction(self.__direction+1)
				self.changeDirection(aimDiretion)
			else:
				self.set_direction(self.__direction-1)
				self.changeDirection(aimDiretion)

	def goAction(self, aimDiretion):
		if self.__direction == aimDiretion:
			if aimDiretion == 1:
				y = self.__origin.get_y() + self._step
				self.__origin.set_y(y)
			elif aimDiretion == 3:
				y = self.__origin.get_y() - self._step
				self.__origin.set_y(y)
			elif aimDiretion == 2:
				x = self.__origin.get_x() + self._step
				self.__origin.set_x(x)
			else:
				x = self.__origin.get_x() - self._step
				self.__origin.set_x(x)
			self.print_coornate()
		else:
			self.changeDirection(aimDiretion)
			self.goAction(aimDiretion)

	def print_coornate(self):
		print('current coordinate:(%s, %s)' % (self.__origin.get_x(), self.__origin.get_y()))

	
	

	@property
	def step(self):
		return self._step
	@step.setter
	def step(self, value):
		if value > 0 and value < 10:
			self._step = value
		else:
			raise ValueError('step must between 0~10!')
	@property
	def stepCount(self):
		return 0 + self._step


robot = Robot('roni', Coordinate(0, 0), Direction['up'])
robot.step = 2
robot.changeDirection(Direction['down'])
robot.goAction(Direction['right'])
robot.goAction(Direction['up'])


