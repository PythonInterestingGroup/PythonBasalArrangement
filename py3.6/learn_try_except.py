# -*- coding: utf-8 -*-
#author dm
'''
def some_function():
    r=-1
def foo():
    r=some_function()
    if r==(-1):
        return (-1)
    return r
def bar():
    r=foo()
    if r==(-1):
        print('error')
    else:
        pass
'''

try:
    print('try....')
    r=10/0  #r=10/2
    print('result:',r)
except ZeroDivisionError as e:
    print('except',e)
finally:
    print('finally')  #finally如果有，则一定会被执行（可以没有finally语句）。
print('END')

#如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:   #int()函数可能会抛出ValueError
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

#Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”

#第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了。
try:
    pass
    #foo()
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')

#https://docs.python.org/3/library/exceptions.html#exception-hierarchy 常见错误类型

def foo(s):
    return  10/int(s)
def bar(s):
    return foo(s)*2
def main():
    try:
        bar(0)
    except Exception as e:
        print('Error:',e)
    finally:
        print('finally...')
main()

#Python内置的logging模块可以非常容易地记录错误信息
#同样是出错，但程序打印完错误信息后会继续执行，并正常退出：
import logging

def foo1(s):
    return 10 / int(s)

def bar1(s):
    return foo1(s) * 2

def main1():
    try:
        bar1('0')
    except Exception as e:
        logging.exception(e)
main1()
print('END')
'''
#抛出错误：
#如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：
print('#####')
class FooError(ValueError):
    pass
def foo2(s):
    n=int(s)
    if n==0:
        raise FooError('invalid value:%s'%s)
    return 10/n
foo2('0')
'''
'''
#在bar()函数中捕获了错误，打印一个ValueError!后，把错误通过raise语句抛出去了
print('********')
def foo3(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar3():
    try:
        foo3('0')
    except ValueError as e:
        print('ValueError!')
        raise
bar3()
'''
print('@@@@@')
try:
    a=10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')