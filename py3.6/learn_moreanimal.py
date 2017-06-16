# -*- coding: utf-8 -*-
#author dm

#多重继承
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
class Bat(Mammal):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass

#我们要给动物再加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类：
class Runnable(object):
    def run(self):
        print('running.....')

class Flyable(object):
    def fly(self):
        print('fly.....')

#对于需要Runnable功能的动物，就多继承一个Runnable，例如Dog：
class Dog(Mammal,Runnable):
    pass

class Bat(Mammal, Flyable):
    pass
#通过多重继承，一个子类就可以同时获得多个父类的所有功能

#在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。
# 但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。

#class Dog(Mammal, RunnableMixIn, CarnivorousMixIn) 可以同时拥有几个Mixin
#MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。

#Python自带的很多库也使用了MixIn。举个例子，Python自带了TCPServer和UDPServer这两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由ForkingMixIn和ThreadingMixIn提供。通过组合，我们就可以创造出合适的服务来。
#编写一个多进程的TCP服务：
#class MyTCPServer(TCPServer,ForkinMixIn):
#    pass

#编写一个多线程模式的UDP服务，定义如下：
#class MyUDPServer(UDPServer, ThreadingMixIn):
#    pass

#更先进的协程模型，可以编写一个CoroutineMixIn：
#class MyTCPServer(TCPServer, CoroutineMixIn):
#    pass

#多继承时，多个父类定义相同方法，并不会冲突,定义类时的继承关系是有序的

class A(object):
    def run(self):
        print('A run!')

class B(object):
    def run(self):
        print('B run!')

class C(A, B):
    pass
c = C()
c.run() #A run

class C1(B,A):
    pass
c1=C1()
c1.run() #B run

