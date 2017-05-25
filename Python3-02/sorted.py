# _*_ coding:utf-8 _*_
l = [36, 5, -12, 9, -21]

print("sorted() 也是个高阶函数,还可以接受一个 key函数来实现自定义排序")
print(sorted(l, key = abs))
print("若实现反向排序,可以传入第三个参数reverse=True:")

L = [('john','B',15),('jane','A',12),('dave','B',10),('ethan','C',20),('peter','B',20),('mike','C',16)]


def by_name(t):
	return t[0]
def by_score(t):
	return t[1],t[2]

L2 = sorted(L, key=by_name)
print(L2)
print(sorted(L, key=by_score, reverse = False))