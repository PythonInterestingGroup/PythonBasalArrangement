# -*- coding: utf-8 -*-

#author dm

#继承多态

class Animal(object):
    def run(self):
        print("Animal is runnning.....")

#从animal继承
class Dog(Animal):
    def run(self):
        print("dog is running..")
    def eat(self):
        print("eating meat...")

class Cat(Animal):
    def run(self):
        print("cat is running..")

#子类继承父类所有方法,
# 当子类与父类有相同的方法时，子类实例调用此方法已子类为准，这就是多态
dog=Dog()
dog.run()

cat=Cat()
cat.run()

a=list()
b=Animal()
c=Dog()

#true 一个class 相当于一个数据类型
print(isinstance(a,list))
print(isinstance(b,Animal))
print(isinstance(c,Dog))
print(isinstance(c,Animal))

print(isinstance(b, Dog)) #false

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

run_twice(Tortoise())

#继承还可以一级一级地继承下来,任何类，最终都可以追溯到根类object
#对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
#对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：

class Timer(object):
    def run(self):
        print('Start...')
run_twice(Timer())

class Province(object):
    def __init__(self,proname):
        self.proname=proname
    def ps(self):
        print("i an in %s"%self.proname)

class City(Province):
    def __init__(self,proname,cityname):
        self.proname=proname
        self.cityname=cityname
    def ps1(self):
        print('i an in %s-%s'%(self.proname,self.cityname))

class Other(object):
    def ps(self):
        print('我不属于Province类或其子类，但我有ps方法我同样可以被调用')
    def ps1(self):
        print('我不属于Province类或其子类，但我有ps1方法我同样可以被调用')

def pro(pro):
    pro.ps()
    pro.ps1()

pro(City('上海','浦东'))
#pro(Province('上海')) 无ps1方法
pro(Other())
