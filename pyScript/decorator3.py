# --*-- coding: utf-8 --*--

def outer(x):
	def inner():
		print x
	return inner

point1 = outer(1)
point2 = outer(2)

print point1()
print point2()


def logging(func):
	def easyDeco(*args, **kw):
		print '%s is running. ' % func.__name__
		#result = func(*args, **kw)
		#print '%s finished!' % func.__name__
		return func(*args, **kw)
	return easyDeco

def loggingNoPara(func):
	print '%s is running. ' % func.__name__
	return func

@loggingNoPara
def sayHello():
	print 'Hello, world!'

#sayHello = logging(sayHello)
#sayHello = loggingNoPara(sayHello)
sayHello()

import functools
def loggingPara(text):
	def _deco(func):
		#@functools.wraps(func)
		def __deco(*args, **kw): # 处理传入的函数的参数
			print '%s %s. ' %(text, func.__name__)
			print func.__doc__
			#result = func(*args, **kw)
			#print '%s has been %s finished!' %(func.__name__, text)
			return func(*args, **kw)
		return __deco
	return _deco


@loggingPara('execute')
def Hello():
	"say hello"
	print 'Hello, rookie!'

Hello()
print Hello.__name__