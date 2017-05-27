from functools import reduce

def add(x , y):
	return x + y

def add_v2(x , y):
	return x * 10 + y

def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	
	
print(reduce(add, [1,2,3,4,5,6,7,8,9]))
print(reduce(add_v2,[1,2,3]))
print(reduce(add_v2, map(char2num, "291485")))


def str2int(s):
	def add_by10(x , y):
		return x * 10 + y

	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	
	return reduce(add_by10, map(char2num, s))
	
	
print(str2int("123244231"))


## lamdba

def str2int_v2(s):

	return reduce(lambda x,y : x * 10 + y, map(char2num, s))
	
	
print(str2int("1234245"))	
