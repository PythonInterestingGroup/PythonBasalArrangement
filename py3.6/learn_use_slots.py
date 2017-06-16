# -*- coding: utf-8 -*-
#author dm

#使用__slots__
class Student(object):
    pass

s = Student()
s.name='Bob' #动态的给实例绑定一个属性
print(s.name)


# 给实例绑定方法
def set_age(self, age):
    self.age = age
from types import  MethodType
s.set_age=MethodType(set_age,s)
s.set_age(25)
print(s.age)

#给一个实例绑定变量，对另一个实例是不起作用的
s2=Student()
#s2.set_age(25) #尝试调用方法会报错

#为了给所有实例都绑定方法 可以给class绑定方法：
def set_score1(self,score):
    self.score=score
Student.set_score1=set_score1
s.set_score1(100)
print(s.score)

s2.set_score1(98)
print(s2.score)
#通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。

#__slots__
#Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class Student1(object):
    __slots__ = ('name','age')   # 用tuple定义允许绑定的属性名称

s3=Student1()
s3.name = 'lily'
s3.age = 12
#由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
#s3.score = 90

 #__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class Middlestudent(Student1):
     pass

m=Middlestudent()
m.score = 99

#除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__


####
#1，slots并不能严格限制属性的添加，可通过在方法里定义限制之外的属性来添加本不能添加的属性（当然，前提是方法没有被限制）
#2，类属性是公共属性，所有实例都可以引用的，前提是实例自身没有同名的属性，因此类属性不能随意更改（别的实例可能在引用类属性的值），就是说不能随便用a.set_age()更改age的值（因为调用此方法更改的是类属性age的值，不是实例a自身的age属性值）

def set_age(self,age):
    self.age=age

class Stu(object):
    pass

s=Stu()
a=Stu()

from types import MethodType

Stu.set_age=MethodType(set_age,Stu)

a.set_age(15) #通过set_age方法，设置的类属性age的值
s.set_age(11) #也是设置类属性age的值，并把上个值覆盖掉
print(s.age,a.age) #由于a和s自身没有age属性，所以打印的是类属性age的值

a.age = 10  #给实例a添加一个属性age并赋值为10
s.age = 20  #给实例b添加一个属性age并赋值为20
#这两个分别是实例a和s自身的属性，仅仅是与类属性age同名，并没有任何关系

print(s.age,a.age)  #打印的是a和s自身的age属性值，不是类age属性值






