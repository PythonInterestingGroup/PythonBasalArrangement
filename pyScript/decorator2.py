# --*-- coding: utf-8 --*--
def deco(func):
    '''
    新函数只在第一次被调用，且原函数多调用一次
    '''
    print 'before myfunc() called.'
    func()
    print ' after myfunc() called. '
    return func


def deco1(func):
    '''
    使用内嵌包装函数，确保每次新函数被调用，与deco执行的顺序不同
    '''
    def _deco():
        print 'before myfunc() called.'
        func()
        print ' after myfunc() called. '
        # don't need to return func
    return _deco

def deco2(func):
    '''
    对带参数的函数进行装饰
    '''
    def _deco(a, b):
        print 'before myfunc() called.'
        ret = func(a, b)
        print ' after myfunc() called. '
        return ret
    return _deco

def deco3(func):
    '''
    参数不确定的函数进行装饰
    '''
    def _deco(*args, **kwargs):
        print 'before myfunc() called.'
        ret = func(*args, **kwargs)
        print ' after myfunc() called. '
        return ret
    return _deco

def deco4(arg):
    '''
    让装饰器带参数，多一层嵌套
    '''
    def _deco(func):
        def __deco():
            print 'before %s called [%s].' %(func.__name__, arg)
            func()
            print ' after %s called [%s].' %(func.__name__, arg)
        return __deco
    return _deco

@deco1 # 使用语法糖，等价于myfunc = deco(myfunc) 
def myfunc():
    print 'myfunc() called. '
    return 'OK'
#myfunc = deco(myfunc) # true function
myfunc()
print '\n' + '*'*32 + '\n'
myfunc()


print '\n' + '*'*8 + '  deco2  '+ '*'*8 + '\n'
@deco2
def myfunc(a, b):
    print ' myfunc(%s, %s) called.' % (a, b)
    return a+b
myfunc(1, 2)
myfunc(3, 4)


print '\n' + '*'*8 + '  deco3  '+ '*'*8 + '\n'
@deco3
def myfunc(a, b):
    print ' myfunc(%s, %s) called.' % (a, b)
    return a+b

@deco3
def myfunc1(a, b, c):
    print ' myfunc(%s, %s, %s) called.' % (a, b, c)
    return a+b
myfunc(1, 2)
myfunc1(3, 4, 5)

print '\n' + '*'*8 + '  deco4  '+ '*'*8 + '\n'
@deco4('mymodule')
def myfunc():
    print ' myfunc() called. '

@deco4('mymodule2')
def myfunc2():
    print ' myfunc2() called. '

myfunc()
myfunc2()
