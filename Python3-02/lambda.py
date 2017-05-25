# _*_ coding: utf-8 _*_
f = lambda x : x * x
print(f(10))

print("匿名函数 lambda 只能有一个表达式")

print("\n\n装饰器:")
print("不修改函数的定义.在代码运行期间动态的增加功能的方式叫装饰器")

def now():
	print('2017-5-24')
f = now
f()
print(f.__name__)
print(now.__name__)

def log(func):
	def wrapper(*args, **kw):
		print('call %s():'%func.__name__)
		return func(*args, **kw)
	return wrapper

@log  # current = log(current)
def current():
	print('2017-05-25')

current()
print(current.__name__) #wrapper

def log2(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print('%s %s():'%(text,func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log2("execute") #log2('execute')now2()
def now2():
	print('2017-05-25-now2')

now2()
print(now2.__name__) #wrapper

print("上面两个装饰器的定义都没有问题,但是原来函数对象的属性已经变了")
print("只需记住在定义wrapper()的前面加上@functools.wraps(func)即可")
import functools

def log3(func):
	@functools.wraps(func)
	def wapper(*args, **kw):
		print("call %s():"%func.__name__)
		func(*args, **kw)
		print("call - end")
	return wapper

@log3
def now3():
	print('2017-05-25-now3')

now3()
print(now3.__name__) #wrapper



















