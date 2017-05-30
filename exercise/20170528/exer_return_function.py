## 

def calc_sum(*args):
	ax = 0
	for n in args:
		ax += n
	return ax
	
print(calc_sum(1,2,3,4,5,6))
print(calc_sum(*range(0,10)))

def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args :
			ax += n
		return ax
	return sum
	
f1 = lazy_sum(*range(1,20))

print(lazy_sum(*range(1,20)))
print(f1())

## 闭包 Closure  
def count():
	fs = []
	for i in range(1,4):
		def f():
			return i * i
		fs.append(f)
	print("count: i =",i)
	return fs
	
def count_v2():
	def f(j):
		def g():
			return j*j
		print("count_v2 j =",j)
		return g
	fs = []
	for i in range(1,4):
		fs.append(f(i))
	return fs
	
f1,f2,f3 = count()
f4,f5,f6 = count_v2()

print("f1:",f1())
print("f2:",f2())
print("f3:",f3())

print("f4:",f4())
print("f5:",f5())
print("f6:",f6())


##

def test_closure():
	f = []
	i = 1
	
	def func():
		return i * i
	
	f.append(func)
	i += 1
	f.append(func)
	i += 1
	f.append(func)

	return f
	
def test_closure_2():
	f = []
	i = 1
	
	def func(i):
		def g():
			return i * i
		return g
	
	f.append(func(i))
	i += 1
	f.append(func(i))
	i += 1
	f.append(func(i))
	return f
	
	
func1,func2,func3 = test_closure()

func4,func5,func6 = test_closure_2()

print("func1:",func1())
print("func2:",func2())
print("func3:",func3())

print("func4:",func4())
print("func5:",func5())
print("func6:",func6())


	