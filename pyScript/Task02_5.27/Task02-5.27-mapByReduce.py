# --*-- coding: utf-8 --*--
'''
implement the function of map by reduce
tricks: here reduce used to concatenate x and y
'''

L = [1, 2, 3, 4, 5, 6, 7, 8]

def mapByReduce(x, y):
	if isinstance(x, int):
		return [x * x] + [y * y]
	else:
		return x + [y * y]

print reduce(mapByReduce, L)