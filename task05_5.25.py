# -*- codeing: utf-8 -*-
#! usr/bin/env python3

# system function
# 

import math

abs(100)
abs(-20)

# 'TypeError' : 传参数量不对, 参数类型不对

max(1, 2, 3, 4, -2, -100)

int('100')
int(11.444)
float('2')
str(100)
bool(1)

a = abs
a(-1) # 参数做变量

# 定义函数

def myAbs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x > 0:
		return x
	else:
		return -x

myAbs(100)
myAbs(-200)

def  empty(): 
	pass # pass 占位符

def move(x, y, step, angle = 0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny
  


x,y = move(10, 20,math.pi / 6)  # tuple
print("x= %s, y = %s" % (x,y))


def quadratic(a, b, c):
	x  = -b
	y = b*b - 4*a*c
	return (x + math.sqrt(y)) / (2*a), (x - math.sqrt(y)) / (2*a)

print(quadratic(2, 3, 1))


#

def power(x, n = 2): # 默认参数卸载后
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s
power(2, 3)
power(4)


# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# 所以，定义默认参数要牢记一点：默认参数必须指向不变对象！

def add_end(L = None):
	if L is None:
		L = []
	L.append("END")
	return L

print(add_end())
print(add_end())
print(add_end([1, 2, 3]))

def calc(*numbers):
	sum = 0
	for n in numbers:
		sum += n
	return sum

print(calc(1, 2, 3, 4))

# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：

nums = [1, 2, 3, 4, 5]
print(calc(*nums))


# 关键字参数

def person(name, age, **kw):
	print('name:', name, 'age:', age, 'other', kw)

print(person('roni', '25'))
print(person('mars', '30', city='sh'))

extra = {'city': 'sh', 'job': 'engineer'}
print(person('roni', '35', **extra))


def person2(name, age, *, city, job) # 命名关键字参数
                                    
# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了

# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的


def fn(n):
	if n > 1:
		return n * fn(n-1)
	else:
		return 1

print(fn(10))


# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况
# 



# 见 5.22 提交
# 
students =[('john','B',15),('jane','A',12),('dave','B',10),('ethan','C',20),('peter','B',20),('mike','C',16)]
result = sorted(students, key=lambda student:(student[1],-student[2]))
print(result)