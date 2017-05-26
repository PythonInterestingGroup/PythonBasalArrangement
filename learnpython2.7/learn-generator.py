# _*_ coding: utf-8 _*_

#要创建一个generator，有很多种方法。
#第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
#创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
L = [x * x for x in range(10)]
print L

g = (x * x for x in range(10))
print g

print g.next()
print g.next()

for n in g:
	print n
#著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
#1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def fib(max):
	n,a,b=0,0,1
	while n<max:
			print b
			a,b=b,a+b
			n=n+1
print fib(6)

#要把fib函数变成generator，只需要把print b改为yield b就可以了
def fib(max):
	n,a,b=0,0,1
	while n<max:
		yield b
		a,b=b,a+b
		n=n+1
print fib(6)
l=[x  for x in fib(10)]
print l[1:3]

#generator和函数的执行流程不一样。
#函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#而变成generator的函数，在每次调用next()的时候执行，
#遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
#odd不是普通函数，而是generator，在执行过程中，遇到yield就中断，下次又继续执行。执行3次yield后，已经没有yield可以执行了，所以，第4次调用next()就报错。
def odd():
    print 'step1'
    yield 1
    print 'step2'
    yield 3
o=odd()
print o.next()
print o.next()

for n in fib(6):
    print n

#def fibslice(a,b):
    #print [x for i,x in enumerate fib(b) if i>=a]





def fib():
    a,b=0,1
    while 1:
        yield b
        i=b
        b=a+6
        a=i       

def gnext(x=0,y=1):
    g=fib()
    max=y+1
    n=1
    l=[]
    while n<=max:
        l.append(g.next())
        n=n+1
    print l[x:y]

print gnext(3,10)

