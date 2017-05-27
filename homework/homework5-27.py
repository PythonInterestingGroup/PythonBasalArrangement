# _*_ coding:utf-8 _*_

from functools import reduce

def qartt(x,y):
	if isinstance(x, int):
		return [x**2,y**2]
	else :
		l = list(x)
		l.append(y**2)
		return l
		

L = range(1, 10)
print(reduce(qartt,L))

ll = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
r = []
for l in ll:
	m = map(lambda x : x, l)
	print(" m = %s"%m)
	r += list(m)
print(r)

#错误方法
ll = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def extend_list(x):
	r = []
	r += list(x)
	yield r

print(list(map(extend_list, ll)))


