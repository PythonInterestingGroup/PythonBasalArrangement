
def dog():
	print("dog wang wang")

dog()


## 1
def dog_decorator_1(func):
	print("dog ready ...")
	func()
	print("dog relax ...")
	return 
	
dog_decorator_1(dog)


## 2
def dog_decorator_2(func):
	def wrapper():
		print("dog ready ...")
		func()
		print("dog relax ...")
	return wrapper;

dog = dog_decorator_2(dog)
dog()

## 3
def dog_decorator_3(func):
	def wrapper():
		print("dog ready ...")
		func()
		print("dog relax ...")
	return wrapper;

@dog_decorator_3
def hashiqi():
	print("hashiqi wu~~~~~")

hashiqi()
print(hashiqi.__name__)

## 4
import functools

def dog_decorator_4(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print("dog ready ...")
		func(*args,**kw)
		print("dog relax ...")
	return wrapper;
	
@dog_decorator_4
def samoye():
	print("samoye war war war")
samoye()
print(samoye.__name__)  

## 5
def dog_decorator_5(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print(func.__name__,text,"ready ...")
			f = func(*args,**kw)
			print(func.__name__,text,"relax ...")
			return f
		return wrapper
	return decorator
	
@dog_decorator_5("already")
def keji():
	print("keji war war war")
keji()
print(keji.__name__) 


	