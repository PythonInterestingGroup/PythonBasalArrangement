#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。

和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
'''


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_name(self):  # 获取
        return self.name

    def get_score(self):
        return self.score

    def set_name(self, name):  # 修改
        self.name = name

    def set_score(self, score):
        self.score = score

    def print_score(self):
        print('%s:%d' % (self.name, self.score))

    def get_grade(self):
        if self.score > 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


pei = Student('lipeipei', 99)  # 创建Student的实例
gmy = Student('gumingyong', 80)
yan = Student('yanyan', 56)
print('name:%s' % pei.name + '\nscore:%d' % pei.score + '\ngrade:%s' % pei.get_grade())
gmy.print_score()
print('yan grade is %s' % yan.get_grade())


# 继承和多态
# 当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。
class Animal(object):
    def run(self):
        print('animal is running........')


class Dog(Animal):
    def run(self):
        print('dog is running.........')


class Cat(Animal):
    def run(self):
        print('cat is running..............')


def run_twice(animal):
    animal.run()
    animal.run()


a = run_twice

dog = Dog()
dog.run()
cat = Cat()
cat.run()
animal = Animal()
animal.run()

print('animal is a Cat？', isinstance(animal, Cat))
print('dog is a Dog？', isinstance(dog, Dog))
print('cat is a Animal？', isinstance(cat, Animal))

run_twice(cat)
run_twice(dog)
run_twice(animal)
# 获取对象信息
# 基本类型都可以用type()判断
print(type('123'))
# 如果一个变量指向函数或者类，也可以用type()判断
print(type(cat))
print(type(a))
if type(123) == type('456'):
    print('true')
else:
    print('flase')
# 判断基本数据类型可以直接写int，str等，如果要判断一个对象是否是函数,可以使用types模块中定义的常量
import types


def fn():
    pass


if type(fn) == types.FunctionType:
    print('true')

if type(abs) == types.BuiltinFunctionType:
    print('true')

if type(lambda x: x) == types.LambdaType:
    print('true')

if type(x for x in range(10)) == types.GeneratorType:
    print('true')
# 使用dir():获取一个对象的所有属性和方法，它返回一个包含字符串的list
print(dir(Student))


# 实例属性和类属性
class Student(object):
    name = 'Stu'  # 定义了一个类属性


s = Student()
s.name = 'peipei'  # 给实例绑定name属性
print(s.name)
print(Student.name)
del s.name  # 删除实例的name属性
print(s.name)
