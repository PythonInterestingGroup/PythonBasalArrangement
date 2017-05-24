# _*_ coding: utf-8 _*_
f = lambda x : x * x
print(f(10))

print("匿名函数 lambda 只能有一个表达式")

print("\n\n装饰器:")

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

def log2(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print('%s %s():'%(text,func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log2("execute")
def now2():
	print('2017-05-25')

now2()