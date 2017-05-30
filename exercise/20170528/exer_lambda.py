
print(list(map(lambda x: x * x, [1,2,3,4,5,6,7,8,9])))

def count():
	def f(j):
		return lambda : j * j
	fs = []
	for i in range(1,4):
		fs.append(f(i))
	return fs
	
f1,f2,f3 = count()


def count_v2():
	
	fs = []
	
	for i in range(1,4):
		fs.append(lambda : i * i)
		
	return fs;
	
f4,f5,f6 = count_v2();

print("f1:",f1())
print("f2:",f2())
print("f3:",f3())

print("f4:",f4())
print("f5:",f5())
print("f6:",f6())
