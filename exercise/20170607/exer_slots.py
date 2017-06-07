#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
	pass
	
## 绑定属性
s = Student()
s.name = 'Michael'

print(s.name)

## 绑定方法

def set_age(self,age):
	self.age = age

#s.set_age = set_age
#s.set_age(25)
#print(s.age)

from types import MethodType
s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)

## 上面的绑定只对一个实例生效
s2 = Student()
#s2.set_age(25)

## 给所有实例绑定方法
def set_score(self,score):
	self.score = score

Student.set_score = set_score
s.set_score(80)
print(s.score)

s2.set_score(60)
print(s2.score)

## 限制属性
class Dog(object):
	__slots__ = ('name','shout','set_age','age')
	
husky = Dog()
husky.name = 'Husky'
husky.shout = 'Wu~~'
#husky.talk = "i'm husky"

husky.set_age = MethodType(set_age,husky)
husky.set_age(25)
print(husky.age)

## 注意：使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
## 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__



