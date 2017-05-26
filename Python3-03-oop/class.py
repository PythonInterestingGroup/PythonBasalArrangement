#usr/bin/python3
#_*_ coding:utf-8 _*_


class Student(object):
	"""docstring for Student"""
	def __init__(self, name, score):
		super(Student, self).__init__()
		self.__name = name
		self.__score = score

	def print_score(self):
		print("%s:%s"%(self.__name,self.__score))
#直接在类里绑定的属性是类属性,可以直接通过类名访问
	nike = "jesscia"
		


bart = Student("jiankang",98)
bart.print_score()

class MiddleStu(Student):
	"""docstring for middleStu"""


middle = MiddleStu("cc",70)
middle.print_score()

print(middle.nike,MiddleStu.nike)

import types

def fn():
	pass
print("使用 type()判断函数类型::::")
print(type(123),type("abs"),type(middle))
print("type(fn)==types.FunctionType:",type(fn)==types.FunctionType)

print("使用isinstance()判断函数类型::::")
print(isinstance(b'a', bytes),isinstance(123, int))

print("使用dir()方法获取一个对象的所有属性个方法,返回一个 list")
print("使用getattr()、setattr()以及hasattr()，可以获取,设置,添加对象属性")

print(getattr(bart,'x',404))

