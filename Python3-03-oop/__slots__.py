# _*_ coding:utf-8 _*_


class Student(object):
	pass

print("创建一个 class 后可以动态添加属性和方法:")

s = Student
s.name = "Xu"    # 动态给实例绑定一个属性
print(s.name)

def set_age(self, age):	# 定义一个函数作为实例方法
	self.age = age
	print("age=%s"%self.age)

from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法 仅仅对此实例有效
s.set_age(25)

def  set_score(self, score):
	self.score = score
	# print("score = %s"%self.score)

# 给所有实例绑定方法
Student.set_score = MethodType(set_score, Student) 
s2 = Student
s2.set_score(99)
print(s2.score)

# 使用__slotes__ 限制允许绑定的属性名称

class Animal(object):
	__slots__ = ('foot','eye') # 用tuple定义允许绑定的属性名称

dog = Animal()
dog.foot = 4
dog.eye = 2
#此处会报错 'Animal' object has no attribute 'brother'
# dog.brother = 4   
print("使用__slotes__限制允许属性仅对当前类有效,对其子类无效")
#子类实例允许定义的属性就是自身的__slots__加上父类的__slots__