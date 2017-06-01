#!/usr/bin/env python
# -*- coding: utf-8 -*-

def count_v1():
	fs = []
	for i in range(1,4):
		def f():
			return i * i
		fs.append(f)#[f()]
		#fs.append(f())f函数会立即被执行f[f(1)]
	return fs
	
f1,f2,f3 = count_v1()#[f,f,f]
print("f1:",f1(),"f2:",f2(),"f3:",f3())
	
def count_v2():
	def f(j):
		def g():
			return j*j
		#j=j+1 加一行 结果4,9，16
		return g  #返回g函数并未立刻执行输出j*j的结果
	fs = []
	for i in range(1,4):
		fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
		#f[1],f[2],f[3]
	return fs

f4,f5,f6 = count_v2()
print("f4:",f4(),"f5:",f5(),"f6:",f6())

#貌似是这样的，count里面，for循环每次会把值传给g里面，所以f(1), f(2), f(3)的值里面j分别是1,2,3；而errorCount里面，每次返回函数，当时先未调用，最后三个s1，s2，s3返回的函数中参数的值都是3


#等价
def test_closure_1():
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
func1,func2,func3 = test_closure_1()
print("func1:",func1(),"func2:",func2(),"func3:",func3())
#返回函数，只是返回了函数并没有执行，等到函数被调用的时候，才执行了，此时i=3了

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



def count_2():
        fs=[]
        for i in range(1,4):
                def f(j):
                        def g():
                                print(i,j)
                                return i*j
                        return g
                fs.append(f(i))
        return fs

f1,f2,f3=count_2()
print (f1(),f2(),f3())
#3*1 3*2 3*3



def test_closure_4():
        f=[]
        i=[1,2,3]
        def func(i):
                def g():
                        return i[0]*i[0]
                return g

        f.append(func(i))
        i[0]+=1
        f.append(func(i))
        i[0]+=1
        f.append(func(i))
        return f
funca,funcb,funcc=test_closure_4()
print('funca:',funca(),'funcb:',funcb(),'funcc:',funcc()) #999


#用匿名函数代替，lamdba表达式
#不会
