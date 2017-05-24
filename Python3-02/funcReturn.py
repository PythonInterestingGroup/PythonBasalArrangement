# _*_ coding: utf-8 _*_

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

l = [1, 3, 5, 7, 9]
f = lazy_sum(1, 3, 5, 7, 9) # = lazy_sun(*l)
print(f())

def count():
	def f(j):
		def g():
			return j * j
		return g
	fs = []
	for i in range(1, 4):
		fs.append(f(i))
	return fs

# 此时 fs 列表内保存的是 f(1),f(2),f(3), 即g()的起始地址 

f1, f2, f3 = count()
print(f1(), f2(), f3())

def errorCount():
	fs = []
	for i in range(1, 4):
		def f():
			return i * i
		fs.append(f)
	return fs 
s1, s2, s3 = errorCount()
print(s1(), s2(), s3())

# 此时 fs 列表内保存的是 f, 即f()的起始地址 调用时 i 已经全部是3了 所以结果都是9
# 返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。
des = '''Python的问题就在于，当循环结束以后，循环体中的临时变量i不会销毁，\n而是继续存在于执行环境中。还有一个python的现象是，\npython的函数只有在执行时，才会去找函数体里的变量的值。'''
print(des)
