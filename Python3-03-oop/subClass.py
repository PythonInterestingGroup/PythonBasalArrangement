# _*_ coding:utf-8 _*_

class Animal(object):
	pass

#大类
class Mammal(Animal):
	pass

class Bird(Animal):
	pass

#各种动物
class Dog(Mammal):
	pass


class Bat(Animal):
	pass

class Parrot(Bird):
	pass

class Ostrich(Bird):
	pass

BirdMixIn = Bird
class Goldfish(BirdMixIn):
	pass 

class Runable(object):
	def run(self):
		print("runing...")

class Flyable(object):
	def fly(self):
		print("Flying...")

class Dog(Mammal,Runable):
	pass

class Bat(Mammal, Flyable):
	pass

i = 1
print(++i)




