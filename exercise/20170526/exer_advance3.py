## 生成器

L1 = [ x * x for x in range(10)]
print(L1)

g1 = ( x * x for x in range(10))
print(g1)
for n in g1 :
	print(n)


## 斐波那契数列

def fib(max):
	n,a,b = 0,0,1
	while n < max :
		print(b)
		a,b = b,a+b
		n = n + 1
	return 'done'

def fib_g(max):
	n,a,b = 0,0,1
	while n < max :
		yield b
		a,b = b,a+b
		n = n + 1
	return 'done'
	
print("fib:",fib,"\nfib_g:",fib_g)

for n in fib_g(6):
	print(n)



