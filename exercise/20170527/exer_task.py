#--------------------------------------------------------------------------
#
# 用 reduce 函数实现 map 函数的功能
#
# 例如: L = [1, 2, 3, 4, 5, 6, 7, 8, 9] => [1, 4, 9, 16, 25, 36, 49, 64, 81]
#
# 要求: 使用 reduce 函数
#
#
#---------------------------------------------------------------------------
from functools import reduce

L1 = [1,2,3,4,5,6,7,8,9]

def square_item(x , y) :
	if isinstance(x, list) :
		x.append(y * y)
		return x
	else :
		tempL = []
		tempL.append(x * x)
		tempL.append(y * y)
		return tempL

L2 = reduce(square_item, L1)


print("L1 :",L1)
print("L2 :",L2)


#--------------------------------------------------------------------------
#
# 将一个二维数组内的每个数平方并且展平成一维数组
#
# 例如: ll = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] => [1, 4, 9, 16, 25, 36, 49, 64, 81]
#
# 要求: 使用 map 函数
#
#---------------------------------------------------------------------------


ll = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def get_value(x) :
	return  x * x

## ???
## ll2 = list(map(get_value , (j for i in ll for j in i)))


ll3 = list((j * j for i in ll for j in i))

print("ll:",ll)
print("ll2",ll2)
print("ll3",ll3)

