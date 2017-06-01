
'''
def count():
    fs = []
    for i in range(1, 4):
        def f():

            return i*i
        print("closure:", id(f.__closure__[0]))
        print("closureValue:", f.__closure__[0].cell_contents)
        fs.append(f)
    return fs


it = iter([1, 2, 3])

def count():
    fs = []
    while True:
    	try:
    		i = next(it)
    		print(id(i))
    		def f():
    			return i*i
    		print("f:",id(f))
    		fs.append(f)
    	except StopIteration:
    		break
       
    return fs



f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


f7, f8, f9 = count()
print(f7())
print(f8())
print(f9())

def count02():
    def f(j):
        def g():
            return j*j
        print("closure:", id(g.__closure__[0]))
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f4, f5, f6 = count02()
print(f4())
print(f5())
print(f6())
'''

'''

def test_closure_1():
	f = []
	i = 1

	def func():
		return i*i

	f.append(func)
	i+=1
	f.append(func)
	i+=1
	f.append(func)

	return f	
func1 ,func2, func3 = test_closure_1()
print("func1:", func1(), "func2:", func2(), "func3:", func3())


def test_closure_2():
	f = []
	i = 1

	def func(i):
		def g():
			return i*i
		return g

	f.append(func(i))
	i+=1
	f.append(func(i))
	i+=1
	f.append(func(i))
	return f

func4 ,func5, func6 = test_closure_2()
print("func4:", func4(), "func5:", func5(), "func6:", func6())
'''

'''
c = {"h":1}
d = c
c["h"] += 2

print("cAddress:",id(c), "dAddress:",id(d))
print("c = ",c, "d= ",d)
'''
'''
a = 288
print(id(a))
#b = a
#print(id(b))
a += 2

print("aAddress:",id(a))
#print("bAddress:",id(b))
print("a = ",a)
#print("b= ",b)
'''



a = 23333333333
b = 23333333333
print("a:", id(a))
print("b:",id(b))





