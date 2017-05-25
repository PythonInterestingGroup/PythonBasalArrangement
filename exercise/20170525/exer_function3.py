## 递归函数

def fact(n):
	if n == 1 :
		return 1
	return n * fact(n - 1)

print("5! =",fact(5))

## 尾递归 : 解决栈溢出

def fact_v2(n):
	return fact_iter(n,1)

def fact_iter(num,result):
	if num == 1 :
		return result
	return fact_iter(num - 1, num * result)

print("5! =",fact_v2(5))

## 汉诺塔

def move(n,a,b,c):
	if n == 1 :
	 	print(a,"-->",c)
	else:
		move(n-1, a, c, b)
		print(a,"-->",c)
		move(n-1, b, a, c)

move(4, 'A', 'B', 'C')