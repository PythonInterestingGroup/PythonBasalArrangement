import functools

print(int('100001',2))

def int2 (x,base = 2):
	return int(x,base)
	
print(int2("10101001"))

int2 = functools.partial(int, base = 2)

print(int2("11110001"))