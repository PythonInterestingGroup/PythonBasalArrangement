#-*-coding:utf-8-*-
#函数

import math

print "abs(-10)",abs(-10)
print "abs(10)",abs(10)

print "cmp(1,2)",cmp(1,2)
print "cmp(1,1)",cmp(1,1)
print "cmp(3,2)",cmp(3,2)

print "int('123')",int('123')
print "int(12.34)",int(12.34)
print "float('12.34')'",float('12.34')
print "str(1.23)",str(1.23)
print 'unicode(10)',unicode(10)
print 'bool(1)',bool(1)
print 'bool()',bool()

def my_abs(x):
	if x>=0:
		return x
	else:
		return -x

print 'my_abs(10)',my_abs(10)
print 'my_abs(10)',my_abs(-10)

#空函数
def nop():
	pass

#zuobiao
def move(x,y,step,angle=0):
        nx=x+step*math.cos(angle)
        ny=y-step*math.sin(angle)
        return nx,ny
x,y=move(100,100,60,math.pi/6)
print x,y

r=move(100,100,60,math.pi/6)
print r

#x的n次方
def power(x,n=2):
        s=1
        while n>0:
                n=n-1
                s=s*x
        return s
print 'power(5,2)',power(5,2)
print 'power(5,3)',power(5,3)
print 'power(5)',power(5)

#默认参数
def enroll(name,gender,age=6,city='shanghai'):
        print 'name:',name
        print 'gender:',gender
        print 'age:',age
        print 'city:',city
print "enroll('Jim','F')\n",enroll('Jim','F')
print "enroll('Dave','F',7)",enroll('Dave','F',7)

def add_end(L=None):
        if L is None:
                L=[]
        L.append("END")
        return L

#请计算a2 + b2 + c2 + …
def calc(numbers):
        sum=0
        for n in numbers:
                sum=sum+n*n
        return sum

print 'calc([1,2,3])',calc([1,2,3])

#可变参数，在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple
def calc(*numbers):
        sum=0
        for n in numbers:
                sum=sum+n*n
        return sum
print 'calc(1,2,3)',calc(1,2,3)

#关键字参数，关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name,age,**kw):
        print 'name:',name,'age:',age,'other:',kw
print "person('milk',30)",person('milk',30)
print "person('jack',30,city='sh')",person('jack',30,city='sh')
print "person('jack',30,city='sh',gender='m')",person('jack',30,city='sh',gender='m')

kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=kw['city'], job=kw['job'])

kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **kw)

#在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，或者只用其中某些，但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。

def func(a, b, c=0, *args, **kw):
        print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

func(1,2)
func(1,2,c=3)
func(1,2,3)
func(1,2,3,'a','b')
func(1,2,'a','b',x=9)

args=(1,2,3,4,5,6,'a')
kw={'y':11}
func(*args,**kw)

args=(1,2,'b',4,5,6,'a')
kw={'y':11}
func(*args,**kw)

#计算阶乘n! = 1 x 2 x 3 x ... x n
def fact(n):
        if n==1:
                return 1
        return n*fact(n-1)
print fact(5)

def fact1(n):
        return fact_iter(n,1)
def fact_iter(num,product):
        if num==1:
                return product
        return fact_iter(num-1,num*product)
print fact_iter(5,1)


