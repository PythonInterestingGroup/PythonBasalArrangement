# -*- coding: utf-8 -*-
#author dm
#元类

class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)
h = Hello()
h.hello()
print(type(Hello)) #<class 'type'>
print(type(h)) #<class '__main__.Hello'>
#ype()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。
#们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。
#type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：
def fn(self,name='world'):
    print('Hello,%s.'%name)

Hello1 = type('Hello1', (object,), dict(hello1=fn)) # 创建Hello class
h1 = Hello1()
h1.hello1()
print(type(Hello1))    #<class 'type'>
print(type(h1))    #<class '__main__.Hello'>

#要创建一个class对象，type()函数依次传入3个参数：
#1class的名称；
#2继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
#3class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

#通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
