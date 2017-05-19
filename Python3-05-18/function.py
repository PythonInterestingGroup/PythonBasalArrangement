# _*_ coding: utf-8 _*_

#函数名其实就是指向一个函数对象的引用, 完全可以吧函数名赋给一个变量.

a = abs #变量 a 指向 abs 函数
print(a(-110))


print("255 = ",hex(255))
print("1000 = ",hex(1000))

#定义函数 def 函数名 (参数) : 函数实现 return 
def my_abs(x):
	if x>0:
		return x
	else :
		return -x

print("my_abs(-5) =",my_abs(-5))

#定义一个空函数 pass
def nop():
	pass 

import math

def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny

R  = move(100, 100, 60, math.pi/6)
print("R = ",R )


def clac(*numbers):
	sum = 0
	for n in numbers:
		sum += n**2
	return sum

print("1,2,3 的平方和等于",clac(1,2,3))
list1 = [1,2,3,4,5]
print("clac(*list1) = ",clac(*list1))
#关键字参数
def person (name, age, **kw):
	print('name :',name,'age :',age,'other :',kw)

extra = {'job':'engineer','sex':'man','city':'peiking'}
person('jack',24,**extra)

#命名关键字参数
def personal(name, age, *, job = "BOSS", city="lu'an"):
	print(name, age, job, city)
personal('Jack', 24, city="shanghai", job="engineer")

def personal2(name, age, *args, job = "BOSS", city="lu'an"):
	print(name, age, job, city,args)
personal2('Jack', 24, city="shanghai", job="engineer",*extra)

print("Python 定义函数,可以用必选,默认,可变,关键字,命名关键字参数")
des = r'''def f1(a,b,c=0,*args,**kw)'''
print(des)

def f1(a, b, c = 0, *args, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c = 0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
args = (1, 2)
kw = {'x': '#', 'd': 88, 's' : 'x'}
f1(*args, **kw)
f2(*args, **kw)
print("默认参数,必选参数和命名关键字参数的区别在我理解是:\n命名关键字参数可以在字典里,而默认参数只能放在 tuple 或者 list")