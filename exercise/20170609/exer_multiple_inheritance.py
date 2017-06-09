#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
	pass
	
# 功能
class Runnable(object):
	def run(self):
		print('Running...')
		
class Flyable(object):
	def fly(self):
		print('Flying...')
		
# 各种动物
class Dog(Animal,Runnable):
	pass
	
class Bat(Animal,Flyable):
	pass
	
Dog().run()
Bat().fly()  


# Mixln
class RunnableMinIn(object):
	def run(self):
		print('running...')
		
class CarnivorousMixIn(object):
	def eat(self):
		print('eat meat...')
		
class Tiger(Animal,RunnableMinIn,CarnivorousMixIn):
	pass
	
tiger = Tiger();
tiger.run()
tiger.eat()

## 第一个继承是生父，后边的都是继父,所以，父类有重复地方法，首先继承生父的！！！