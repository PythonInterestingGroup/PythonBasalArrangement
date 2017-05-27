## 

## 筛选奇数
def is_odd(n):
	return n % 2 == 1

print(list(filter(is_odd, range(1,20))))

## 去除空字符

def not_empty(s):
	return s and s.strip()

print (list(filter(not_empty,['','   ','Q','c','zz'])))

## 计算素数

def is_prime(s):
	
	def smallest_divisor(n):
		return find_divisor(n,2)
		
	def find_divisor(n,divisor):
		if  divisor ** 2 > n :
			return n
		elif n % divisor == 0 :
			return divisor
		else :
			return find_divisor(n, divisor + 1)

	if s == 1 :
		return False;
	elif smallest_divisor(s) == s :
		return True
	else :
		return False
		
print (list(filter(is_prime, range(1,100))))
		



