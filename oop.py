#! /usr/bin/env python3
# -*- coding: utf-8 -*-


'Object Oriented Programming'

__author__  = 'roni'

##
## 在Python中，所有数据类型都可以视为对象
##

class Student(object):
	""" a student class """
	def __init__(self, name, score):  # self 指创建的实例本身
		super(Student, self).__init__()
		self.__name = name
		self.__score = score

	def get_name(self):
		return self.__name
	def get_svore(self):
		return self.__score
	def set_name(self, name):
		self.__name = name
	def set_score(self, score):
		self.__score = score
		
	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))


	def getGrade(self):
		if isinstance(self.__score, int):
			if self.__score >= 90:
				return 'A'
			elif self.__score >= 60:
				return 'B'
			else:
				return 'C'
		else:
			return 'score type error'

roni = Student('roni', 999)
roni.print_score()


grade = roni.getGrade()
print(grade)

##
## 在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量
##


from enum import Enum

class Coordinate(object):
	""" Coordinate include x and y """
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



Direction = Enum('Direction', ('up', 'down', 'left', 'right'))
		

class Robot(object):
	""" Robot move to anywhere if you would like """
	def __init__(self, name, coordinate, direction):
		super(Robot, self).__init__()
		self.__name = name
		self.__coordinate = coordinate
		self.__direction = direction

	def set_direction(self, direction):
		self.__direction = direction
	def get_direciton(self):
		return self.__direction

	def set_coordinate(self, coordinate):
		self.__coordinate = coordinate
	def get_coordinate(self, coordinate):
		return self.__coordinate

	def changeDirection(self,aimDiretion):
		self.set_direction(aimDiretion)

	def clockwiseRotation(self,currentDirection):
		if currentDirection == Direction.up:
			return Direction.right
		elif currentDirection == Direction.right:
			return Direction.down
		elif currentDirection == Direction.down:
			return Direction.left
		else:
			return Direction.up

	def changeCoordinate(self, direction, step):
		if direction == Direction.up:
			y = self.__coordinate.get_y() + step
			self.__coordinate.set_y(y)
			return
		elif direction == Direction.down:
			y = self.__coordinate.get_y() - step
			self.__coordinate.set_y(y)
			return
		elif direction == Direction.left:
			x = self.__coordinate.get_x() - step
			self.__coordinate.set_x(x)
			return
		else: 
			x = self.__coordinate.get_x() + step
			self.__coordinate.set_x(x)
			return

	def move(self, direction, step):
		if self.__direction == direction:
			self.changeCoordinate(direction, step)
		else:
			self.changeDirection(direction)
			self.changeCoordinate(direction, step)
			

	def print_coordinate(self):
		print('your coordinate: (%s, %s)' % (self.__coordinate.get_x(), self.__coordinate.get_y()))




robot = Robot("roni", Coordinate(0, 0), Direction.up)
robot.changeDirection(Direction.left)
di = robot.get_direciton()
print(di)
robot.move(Direction.up, 2)
robot.move(Direction.right, 2)
robot.move(Direction.left, 2)
robot.print_coordinate()













