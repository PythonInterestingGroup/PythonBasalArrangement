# _*_ coding: utf-8 _*_

#Python 内建的 filter()函数用于过滤序列
#filter()和 map() 一样 把序列的每个元素用于函数 ,
#但根据返回值 TRUE FALSE 决定保留还是丢弃改元素

def is_odd(n):
	return n % 2 == 1

print(list(filter(is_odd,[x for x in range(1,10)])))

#filter()返回的也是一个惰性序列Iteator

#产生一个从3开始的无限奇数序列
def _odd_iter():
	n = 1
	while  True:
		n = n + 2
		yield n
# for q in _odd_iter():
# 	if q < 1000:
# 		print(q)
# 	else :
# 		break 
#筛选器
def _not_divisible(n):
	return lambda x: x % n >0

#生成器不断生成下一个素数
def primes():
	yield 2 	# 2也是素数
	it = _odd_iter()
	while True:
		n = next(it)
		yield n 
		it = filter(_not_divisible(n), it)

for n in primes():
	if n < 1000:
		print(n)
	else :
		break 

print("找出1-1000内的回数:")
def is_palindrome(n):
	s = str(n)
	return s == s[::-1] #Itrable 对象倒叙输出用切片方法 [::-1] 123 -> 321

print(list(filter(is_palindrome, range(1, 1000))))













		