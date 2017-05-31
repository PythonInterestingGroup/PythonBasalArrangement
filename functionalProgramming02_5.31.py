
'''
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
'''

it = iter([1, 2, 3])

def count():
    fs = []
    while True:
    	try:
    		i = next(it)
    		print(id(i))
    		def f():
    			return i*i
    		fs.append(f)
    	except StopIteration:
    		break
       
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


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
