# _*_ coding:utf-8 _*_

def count_1():
	fs = []
	for i  in range(1,4):
		fs.append(lambda : i * i)
	return fs

f1,f2,f3 = count_1()
print(f1(),f2(),f3())

def count_2():
	def f(j):
		return lambda : j * j
	fs = []
	for i in range(1, 4):
		fs.append(f(i))
	return fs
f4,f5,f6 = count_2()
print(f4(),f5(),f6())