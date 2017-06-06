#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
	def shout(self):
		print('Animal is shouting')
	
def shout_twice(animal):
	animal.shout()
	animal.shout()
	
class Fox(Animal):
	def shout(self):
		print('what the fox say')
		
class Train(object):
	def shout(self):
		print('kuangchi kuangchi kuangchi wu~~~')
	
shout_twice(Fox())
shout_twice(Train())