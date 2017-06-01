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
		j += 1
		return g
	fs = []
	for i in range(1,4):
		fs.append(f(i))
	return fs
	
def count_v3():
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
func1,func2,func3 = test_closure()
print("func1:",func1(),"func2:",func2(),"func3:",func3())
	
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
func4,func5,func6 = test_closure_2()
print("func4:",func4(),"func5:",func5(),"func6:",func6())
	
def test_closure_3():
	f = []
	i = 1
	
	def func():
		j = i
		def g():
			return j * j
		return g
	
	f.append(func())
	i += 1
	f.append(func())
	i += 1
	f.append(func())
	return f
func7,func8,func9 = test_closure_3()
print("func7:",func7(),"func8:",func8(),"func9:",func9())
	
def test_closure_4():
	f = []
	i = [1,2,3]
	
	def func(j):
		def g():
			return j[0] * j[0]
		return g
	
	f.append(func(i))
	i[0] += 1
	f.append(func(i))
	i[0] += 1
	f.append(func(i))
	return f
funcA,funcB,funcC = test_closure_4()
print("funcA:",funcA(),"funcB:",funcB(),"funcC:",funcC())	

	