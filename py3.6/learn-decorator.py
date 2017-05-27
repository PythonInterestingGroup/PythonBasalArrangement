#!/usr/bin/env python
# -*- coding: utf-8 -*-

def now():
    print('2017-05-27')

f=now
print(f())

#函数对象有一个__name__属性，可以拿到函数的名字
print(now.__name__)   #now
print(f.__name__)     #now

#我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义
#在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
#本质上，decorator就是一个返回函数的高阶函数

#log函数是一个decorator，接受一个函数作为参数，并返回一个函数。
def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2017-05-27')

#调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志
print (now())
    
#把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
#由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
#在wrapper()函数内，首先打印日志，再紧接着调用原始函数。

#要自定义log的文本
def log(txt):
    def decorator(func):
        def wrapper(*args,**kw):
            print("%s%s():"%(txt,func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute ')
def now():
    print('2017-05-27')

print(now())  #now
print(now.__name__)  #wrapper 经过decorator装饰之后的函数name已经变了
#为什么不一致...因为因为返回的那个wrapper()函数名字就是'wrapper'
#需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
#3层嵌套的效果:now = log('execute')(now)

#完整版decorator
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

#带参数的decorator
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

#练习
#编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
#能否写出一个@log的decorator，支持@log 和@log('execute')
#可用默认参数text=''或者可变参数*args
def log(str=''):
    def decorater(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
                if str != '':
                    print('text = %s,begin call = %s' % (str,func.__name__))
                    func(*args,**kwargs)
                    print('text = %s,end call = %s' % (str,func.__name__))
                else:
                    print('begin call = %s' % (func.__name__))
                    func(*args,**kwargs)
                    print('end call = %s' % (func.__name__))
        return wrapper
    return decorater

@log('today')
def now():
    print('2017-5-11')
print(now())

@log()
def now():
    print('2017-5-11')
print(now())

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s begin call %s()" % (text, func.__name__))
            ret = func(*args, **kw)
            print("%s end call %s()" % (text, func.__name__))
            return ret
        return wrapper
    if isinstance(text, str):
        return decorator
    else:
        f = text
        text = ''
        return decorator(f)


def log2(*text):
    def decorator(func):
        def wrapper(*args, **kw):
            if text:
                print(''.join(text)+':'+str(func.__name__)+'()')
            return func(*args,**kw)
        return wrapper
    return decorator
