#--*-- coding: utf-8 --*--
'''
The usage of decorator
'''
# no parameter
'''
def deco(func):
    print func
    return func
@deco
def foo():pass
foo()
'''
def deco_functionNeedDoc(func):
    if func.__doc__ == None:
        print func, 'has no __doc__, it''s a bad habbit!'
    else:
        print func, ':', func.__doc__, '.'
    return func
@deco_functionNeedDoc
def f():
    print 'f() Do something'
@deco_functionNeedDoc
def g():
    'I have a __doc__'
    print 'g() Do something'
f()
g()
