# _*_ coding:utf-8 _*_

class Coordinare(object):
	# __slots__ = ('x','y') # 用tuple定义允许绑定的属性名称
	def __init__(self, x, y):
		self.__x = x
		self.__y = y

	@property
	def x(self):
		return self.__x
	@x.setter
	def x(self, value):
		self.__x = value

	@property 
	def y(self):
		return self.__y
	@y.setter
	def y(self, value):	
		self.__y = value

	def output(self):
		print(self.__x, self.__y)

from enum import Enum,unique

class Direct(Enum):
	up = 0
	left = 1
	down = 2
	right = 3


class Robot(object):
	"""point move step by step"""
	def __init__(self, name):
		self.__name = name
		self.__coor = Coordinare(0, 0)
		self.__dir = Direct.up

	def set_dir(self, value):
		self.__dir = value

	def moveToDestination(self, coor):
		while True:
			dx = coor.x - self.__coor.x
			dy = coor.y - self.__coor.y
			# print(dx,dy,self.__dir)
			if dx == 0 and dy == 0:
				print("arrive to destination")
				break ;
			if self.__dir == Direct.up:	#向上
				if dy > 0:
					self.forwardY()
				elif dy < 0:
					self.turn_right()  # 两次右转 改变方向
					self.turn_right()
				elif dy == 0:
					if dx > 0:
						self.turn_right()
					elif dx < 0:
						self.turn_left()
			elif self.__dir == Direct.right:	#向右
				if dx > 0 :
					self.forwardX()	
				elif dx < 0:
					self.turn_right()  # 两次右转 改变方向
					self.turn_right()
				elif dx == 0:
					if dy > 0:
						self.turn_left()
					elif dy < 0:
						self.turn_right()
			elif self.__dir == Direct.down:		#向下
				if dy < 0:
					self.backY()
				elif dy > 0:
					self.turn_right()  # 两次右转 改变方向
					self.turn_right()
				elif dy == 0:
					if dx > 0:
						self.turn_right()
					elif dx < 0:
						self.turn_left()
			elif self.__dir == Direct.left:		#向左
				if dx < 0 :
					self.backX()	
				elif dx > 0:
					self.turn_right()  # 两次右转 改变方向
					self.turn_right()
				elif dx == 0:
					if dy > 0:
						self.turn_left()
					elif dy < 0:
						self.turn_right()

			print("%s arrive at:"%self.__name,self.__coor.x,self.__coor.y)

	def turn_left(self):
		if self.__dir == Direct.up:
			self.__dir = Direct.left
		elif self.__dir == Direct.left:
			self.__dir = Direct.down
		elif self.__dir == Direct.down:
			self.__dir = Direct.right
		elif self.__dir == Direct.right:
			self.__dir = Direct.up
		print("turn left.current dir:",self.__dir)

	def turn_right(self):
		if self.__dir == Direct.up:
			self.__dir = Direct.right
		elif self.__dir == Direct.right:
			self.__dir = Direct.down
		elif self.__dir == Direct.down:
			self.__dir = Direct.left
		elif self.__dir == Direct.left:
			self.__dir = Direct.up
		print("turn right.current dir:",self.__dir)

	def forwardX(self):
		if self.__dir == Direct.right:
			self.__coor.x += 1
		else :
			print("方向错误")
	def backX(self):
		if self.__dir == Direct.left:
			self.__coor.x -= 1
		else :
			print("方向错误")
	def forwardY(self):
		if self.__dir == Direct.up:
			self.__coor.y += 1
		else :
			print("方向错误")
	def backY(self):
		if self.__dir == Direct.down:
			self.__coor.y -= 1
		else:
			print("方向错误")
		


c = Coordinare(2,6)
r = Robot("john")
r.moveToDestination(c)
c.x = -4
c.y = -2
r.moveToDestination(c)










