# --*-- coding: utf-8 --*--
"convert a 2D array into a 1D array with the element be the square of those in 2D array"

ll = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def convert(l):	
	return map(lambda x: x * x, l)

s = []
for i in range(0, len(ll)):
	for j in convert(ll[i]):
 		s.append(j)

print s