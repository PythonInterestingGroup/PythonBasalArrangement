#! /usr/bin/env python3
# -*- coding: utf-8 -*-

'inherit and ...'

__author__ = 'roni'

##
## 继承和多态
##

'''
class Animal(object):
	"""docstring for Animal"""
	def __init__(self):
		super(Animal, self).__init__()
	

	def run(self):
		print('Animal ia running...')

class Dog(Animal):
	"""docstring for Dog"""
	def __init__(self):
		super(Dog, self).__init__()
	
	def run(self):
		print('Dog is running')


animal = Animal()
dog = Dog()

animal.run()
dog.run()

print(isinstance(animal, Animal))
print(isinstance(dog, Animal))

print(isinstance(animal, Dog))
print(isinstance(dog, Dog))


def run_twice(animal):
	animal.run()

run_twice(Animal())
run_twice(Dog())


##
## 获取对象信息
##

# type()
print(type(123))
print(type(dog))

# types模块

import types

def fn():
	pass

print(type(fn) == types.FunctionType)
print(type(lambda x:x) == types.LambdaType)


# isinstance

isinstance([1, 2, 3], (list, tuple))


#　dir() => 获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list

print(dir('asd'))

# getattr()、setattr()以及hasattr()

class MyObject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x

obj = MyObject()

print (hasattr(obj, 'x'))
print(obj.x) 

print(hasattr(obj, 'y'))

setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))

print(getattr(obj, 'y'))

print(getattr(obj, 'z', 404))

print(hasattr(obj, 'power'))

fn = getattr(obj, 'power')
print(fn())
'''


##
## @brief      昨天的作业
##

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

	def goAction(self, aimDiretion, step):
		if self.__direction == aimDiretion:
			if aimDiretion == 1:
				y = self.__origin.get_y() + step
				self.__origin.set_y(y)
			elif aimDiretion == 3:
				y = self.__origin.get_y() - step
				self.__origin.set_y(y)
			elif aimDiretion == 2:
				x = self.__origin.get_x() + step
				self.__origin.set_x(x)
			else:
				x = self.__origin.get_x() - step
				self.__origin.set_x(x)
			self.print_coornate()
		else:
			self.changeDirection(aimDiretion)
			self.goAction(aimDiretion, step)

	def print_coornate(self):
		print('current coordinate:(%s, %s)' % (self.__origin.get_x(), self.__origin.get_y()))

	
	def destinationAction(self, through, destination):
		self.endAction(through)
		self.endAction(destination)
		
	def endAction(self,destination):
		x = self.__origin.get_x()
		y = self.__origin.get_y()
		tx = destination.get_x()
		ty = destination.get_y()
		if y < ty:
			self.goAction(Direction['up'], ty-y)
		elif y > ty:
			self.goAction(Direction['down'], y-ty)
		else:
			pass
		if x < tx:
			self.goAction(Direction['right'], tx-x)
		elif x > tx:
			self.goAction(Direction['down'], x-tx)
		else:
			pass


robot = Robot('roni', Coordinate(0, 0), Direction['up'])
robot.changeDirection(Direction['down'])
robot.goAction(Direction['right'], 1)
robot.goAction(Direction['up'], 2)
robot.destinationAction(Coordinate(2, 6), Coordinate(4, 2))







