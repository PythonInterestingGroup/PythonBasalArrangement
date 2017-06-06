# !/usr/bin/env python3
# -*- coding: utf-8 -*-

class Point(object):
	
	def __init__(self,x,y):
		self.x = x
		self.y = y

class UrsusRobot(object):
	
	__LEFT = 0
	__TOP = 1
	__RIGHT = 2
	__BOTTOM = 3
	
	__direction_str = ['左','上','右','下']
	
	def __init__(self,name,point):
		self.__name = name
		self.__point = point
		self.__direction = self.__TOP
		
	
	def turnLeft(self):
		print('机器人向左转')
		self.__direction = self.__direction - 1 if self.__direction != UrsusRobot.__LEFT else UrsusRobot.__BOTTOM
				
	def turnRight(self):
		print('机器人向右转')
		self.__direction = self.__direction + 1 if self.__direction != UrsusRobot.__BOTTOM else UrsusRobot.__LEFT
		
		
	def moveLeft(self):
		self.__move(UrsusRobot.__LEFT, lambda :  [self.__point.x - 1, self.__point.y])
	
	def moveTop(self):
		self.__move(UrsusRobot.__TOP, lambda :  [self.__point.x, self.__point.y + 1])
					
	def moveRight(self):
		self.__move(UrsusRobot.__RIGHT, lambda :  [self.__point.x + 1, self.__point.y])
		
	def moveBottom(self):
		self.__move(UrsusRobot.__BOTTOM, lambda :  [self.__point.x, self.__point.y - 1])
		
	
	def print_loaction(self):
		print('抵达坐标点(%s,%s)'%(self.__point.x,self.__point.y))

	def print_direction(self):
		print('当前机器人面朝%s'%(UrsusRobot.__direction_str[self.__direction]))
		
		
	def __move(self,direction,func):
		if self.__direction == direction :
			self.__point.x, self.__point.y = func()
			self.__hint_move(direction)
		else :
			self.__hint_direction_error(direction)
					
	def __hint_direction_error(self,direction):
		print("请面朝%s方"%(UrsusRobot.__direction_str[direction]))
		
	def __hint_move(self,direction):
		print("向%s方移动一步"%(UrsusRobot.__direction_str[direction]))

if __name__ == '__main__':
	wall_E = UrsusRobot('wall-E',Point(0, 0))

	for i in range(6):
		wall_E.moveTop()
		
	wall_E.turnRight()
	for i in range(2):
		wall_E.moveRight()
	wall_E.print_loaction()

	for i in range(2):
		wall_E.moveRight()

	wall_E.turnRight()
	for i in range(4):
		wall_E.moveBottom()
	wall_E.print_loaction()
		
		
		
		
		
		
		
		
		
		