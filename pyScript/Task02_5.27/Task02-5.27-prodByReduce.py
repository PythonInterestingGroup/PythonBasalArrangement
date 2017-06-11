# --*-- coding: utf-8 --*--
"implement prod by reduce()"

listExample = [1, 2, 3, 4, 5, 6]

def prod(x, y):
	return x * y

print reduce(prod, listExample)