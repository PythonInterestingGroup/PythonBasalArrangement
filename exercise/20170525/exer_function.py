# -*- coding: utf-8 -*-
import math
## 函数

## hex()方法
print(hex(1000))

## 定义函数

def my_abs(x):
	if x >= 0 :
		return x;
	else :
		return -x
print(my_abs)
print(my_abs(20))  

## 空函数
## pass用来作为占位符，让程序先运行起来
def pop():
	pass
print(pop())
	
##  函数参数检查
def my_abs_v2(x):
	if not isinstance(x, (int,float)):
		raise TypeError("bad operand type")
	if x >= 0 :
		return x
	else :
		return -x

print (my_abs_v2(-121))
# print (my_abs_v2('211'))

def move(x,y,step,angle = 0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx , ny

print(move(2,2,20,math.pi / 6))

p1, p2 = move(10, 10, 6,math.pi / 3)
print(round(p1,2),round(p2,2))

r = move(10, 10, 6, math.pi / 3)
print(r)

r1,r2 = r
print(round(r1,2),round(r2,2))


## 解二元一次方程组
def quadratic(a = 1,b = 1,c = 1):
	delta = math.pow(b, 2) - 4 * a * c
	if a == 0 :
		raise TypeError("a can't be zero")
	if delta < 0 :
		raise TypeError("this binary equation has no solution")
	else :
		x1 = (-b + math.sqrt(delta)) / (2 * a)
		x2 = (-b - math.sqrt(delta)) / (2 * a)
	return x1 , x2

s1 , s2 = quadratic(1,-6,9)
print( s1 , s2 )
print(quadratic(3,-10,4))
print(quadratic(-1,-12,-2))  




	









