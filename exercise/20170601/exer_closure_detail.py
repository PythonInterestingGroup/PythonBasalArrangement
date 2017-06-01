i = 1

def child():
	return i * i

ch1 = child;

i += 1

print("ch1:",ch1())


i = 1

def child_2(j):
	return j * j

ch2 = child_2(i)

i += 1

print("ch2:",ch2)


a = 1
b = a
a += 2
print("a:",a,"b:",b)  

c = [1]
d = c
c[0] += 2
print("c:",c[0],"d:",d[0])


def Fib(max):
	n,a,b = 0,0,1
	while n<max:
		yield b
		a,b = b,a+b
		n  += 1
n = int(input('please enter a number:'))
for s in Fib(n): 
	print(s)
