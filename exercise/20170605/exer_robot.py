#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools
	
class Robot(object):
	
	def __init__(self,name):
		self.__x = 0
		self.__y = 0
		self.__name = name
		
	def __log_move(direction):
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args,**kw):
				f = func(*args,**kw)
				print('向%s移动了一步'%(direction))
				return f
			return wrapper
		return decorator
		
	@__log_move('左')
	def moveLeft(self):
		self.__x -= 1
	
	@__log_move('上')	
	def moveTop(self):
		self.__y += 1
	
	@__log_move('右')
	def moveRight(self):
		self.__x += 1
	
	@__log_move('下')	
	def moveBottom(self):
		self.__y -= 1
		
	def printPosition(self):
		print("%s当前所处位置(%s,%s)"%(self.__name,str(self.__x),str(self.__y)))

#genji = robot('genji')
#for i in range(3):	
#	genji.moveLeft()
#genji.printPosition()
#
#for i in range(4):
#	genji.moveTop()
#genji.printPosition()

#DIRECTOR = (['W','A','S','D'])
#STOP = (['Q',])
#
#def createRobot():
#	return Robot(input("请输入机器人姓名："))
#	
#def controlRobot(robot):
#	input("请输入移动指令：")
#	
	


		
		