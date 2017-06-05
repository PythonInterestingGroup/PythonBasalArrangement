#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
	def shout(self):
		print('Animal is shouting')
		
#class Dog(Animal):
#	pass
#	
#class Cat(Animal):
#	pass
#	
#dog = Dog()
#dog.shout()
#
#cat = Cat()
#cat.shout()

class Dog(Animal):
	
	def shout(self):
		print("dog is wangwang")
		
class Cat(Animal):
	
	def shout(self):
		print("cat is mi ao mi ao")
		
dog = Dog()
dog.shout()

cat = Cat()
cat.shout()