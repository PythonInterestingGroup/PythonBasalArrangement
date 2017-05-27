
## 求 1 到 100 的和

def sum_v1(start,end):
	total = 0;
	for i in range(start,end+1):
		total += i
	return total;

print("1 到 100 的和：",sum_v1(1, 100))
	
## 求 1 到 100 每项平方加一 的和

def sum_v2(start,end):
	total = 0;
	for i in range(start,end+1):
		total += i * i + 1
	return total;	

print("1 到 100 每项平方加一的和：",sum_v2(1, 100))

## 将每次累加的项抽取成函数

def sum_v3(start,end,handle):
	total = 0;
	for i in range(start,end+1):
		total += handle(i)
	return total
	
def handle_v1(x):
	return x * x + 1
def handle_v2(x):
	return 2 * x * x + 4 * x + 32
	
print("1 到 100 每项平方加一的和：",sum_v3(1, 100, handle_v1))  
print("1 到 100 每项为(2n^2 + 4n + 32)的累加和",sum_v3(1, 100, handle_v2))


def is_prime(n):
	
	def smallest_divisor(n):
		return find_divisor(n,2)
	
	def find_divisor(n,divisor):
		
		if pow(divisor , 2)> n:
			return n
		elif n % divisor == 0:
			return divisor
		else:
			return find_divisor(n, divisor + 1)
			
	if 1 == n :
		return 0
	elif smallest_divisor(n) == n :
		return n
	else :
		return 0
		
print("1到100内所有素数的累加和：",sum_v3(1,100,is_prime))
		
		
