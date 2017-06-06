# _*_ coding:utf-8 _*_

class Coordinare(object):

	def __init__(self, x, y):
		self._x = x
		self._y = y

	@property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x = value

	def output(self):
		print(self.x, self._y)

from enum import Enum,unique

class Direct(Enum):
	up = 0
	left = 1
	down = 2
	right = 3


class Robot(object):
	"""docstring for Robot"""
	def __init__(self, name):
		self.__name = name
		self.__coor = Coordinare(0, 0)
		self.__dir = Direct.up

	def moveToDestination(self):
		print(self.__coor.__x)


c = Coordinare(1,1)
c.output()
print(c.__x)
r = Robot("john")
# r.moveToDestination()