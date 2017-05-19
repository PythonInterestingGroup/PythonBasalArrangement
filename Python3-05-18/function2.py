# _*_ coding: utf-8 _*_
def fact(n):
	return fact_item(n , 1)	
def fact_item(num, product):
	if num == 1:
		return product
	return fact_item(num-1,num*product)

num = input("输入数字:")
print("fact (5) = ",fact(5))


def move(n, a, b, c):
	if n == 1:
		print(a,"->",c)
	elif n > 1:
		move(n-1, a, c, b) #前 n-1个移动到 b
		print(a,'->',c) #把 n 移动到 c
		n = n - 1
		move(n, b, a, c) #把 n-1个从 b 移动到 c

move(int(num), 'A', 'B', 'C')













