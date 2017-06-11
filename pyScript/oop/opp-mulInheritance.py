# -*- coding:utf-8 -*-
'multiple inheritance'

class Animal(object):
	pass

# level 1
class Mammal(Animal):
	pass

class Bird(Animal):
	pass

# level 2 different function
class Runnable(object):
	def run(self):
		print 'Running ... '

class Flyable(object):
	def fly(self):
		print 'Flying ... '

# level 3 different animals
class Dog(Animal, Runnable):
	pass

class Bat(Animal, Runnable):
	pass

class Parrot(Bird, Flyable):
	pass

class Ostrich(Bird, Flyable):
	pass

# Mixin
		