#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
	
	def __init__(self,name):
		self.__name = name
	
	def shout(self):
		print('animal shouting')
		
		
class Dog(Animal):
	
	def shout(self):
		print('wangwang')
		
		
class Husky(Dog):
	
	age = 5
	
	def shout(self):
		print('wu~~~~')
		

animal = Animal('animal')
dog = Dog('dog')
husky = Husky('husky')


print('type(animal):%s'%animal)
print('isinstance(husky,Animal):%s'%(isinstance(husky, Animal)))
print('isinstance(animal,Husky):%s'%(isinstance(animal, Husky)))
print('isinstance(animal,(Husky,Animal)):%s'%(isinstance(animal, (Husky,Animal))))

print('dir(husky):%s'%dir(husky))

print('hasatter(husky,"age"):%s'%(hasattr(husky,'age')))
print('setattr(husky,"color","black and white")):%s'%(setattr(husky,'color','black and white')))
print('getattr(husky,"color"):%s'%(getattr(husky,'color')))
print('getattr(husky,"character"):%s'%(getattr(husky,'character','22222')))
getattr(husky,'shout')()

